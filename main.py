import sys
import socket
import time
from datetime import datetime

import mainFunctions, rsaFunctions, Diffie_Hellman

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from testInterfaceTab_ui import Ui_MainWindow  # Importez votre classe UI généré


#Tab1 
##sendButton
##radioText
##radioImage
##radioNone_3
##radioShift_3
##radioXor_3
##radioVigenere_3
##messageInput
##valueEditor
##submitButton
##clearTab1Button
##messageDisplay
##submitButton_2

#Tab2
##sendServer
##radioNone
##radioShift
##radioXor
##radioVigenere
##serverDisplay
##serverInput
##AutoSendButton
##comboEncode
##comboTask
##spinBox

# Configuration du socket
HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

from PyQt5.QtCore import QThread, pyqtSignal
import socket

class ReceiverThread(QThread):
    received = pyqtSignal(str)  # Signal pour les messages normaux
    receivedServer = pyqtSignal(str)  # Signal pour les messages du serveur

    def __init__(self, app, sock):
        super().__init__()
        self.app = app
        self.sock = sock

    def run(self):
        """Exécuté dans un thread séparé; écoute les messages entrants du serveur."""
        while True:
            try:
                rcv_msg = self.sock.recv(65536)  # 64Ko, réception de données du serveur
                if rcv_msg:
                    # Log pour débogage
                    #print(f"Message reçu (brut): {rcv_msg}")

                    # Distinguer entre messages du serveur et autres messages
                    if b"ISCs" in rcv_msg:
                        now = datetime.now()
                        time_string = now.strftime("%H:%M")


                        # Traiter le message si c'est un message du serveur
                        processed_msg = self.app.receive_message(rcv_msg)
                        
                        self.receivedServer.emit(f">>> [{time_string}] Received from server: " + processed_msg)
                    else:
                        # Traiter comme un message normal
                        now = datetime.now()
                        time_string = now.strftime("%H:%M")
                        processed_msg = self.app.receive_message(rcv_msg)
                        self.received.emit(f">>> [{time_string}] Message received: " + processed_msg)
                else:
                    # Aucune donnée reçue, peut indiquer que le serveur a fermé la connexion
                    print("Aucun message reçu, socket fermé peut-être.")
                    break  # Sortie de la boucle si aucun message n'est reçu
            except socket.error as e:
                # Une exception socket.error peut survenir si des problèmes de réseau surviennent
                print(f"Erreur socket lors de la réception des données: {e}")
                continue
            except Exception as e:
                # Autres exceptions générales
                print(f"Erreur générale lors de la réception des données: {e}")
                continue

    def stop(self):
        """Fonction pour arrêter le thread proprement."""
        self.sock.close()  # Fermer le socket peut induire une exception dans recv qui stoppe le thread
        self.quit()  # Termine l'exécution de la boucle d'événements
        self.wait()  # Attend que le thread finisse


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

        # Configuration du socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, port))

        # Initialisation du thread de réception
        self.receiverThread = ReceiverThread(self, self.sock)

        # Connexion des signaux aux slots de l'interface utilisateur
        self.receiverThread.received.connect(self.update_message_display)
        self.receiverThread.receivedServer.connect(self.update_server_message_display)

        # Démarrage du thread
        self.receiverThread.start()

        # Connexion des autres signaux de l'interface utilisateur
        self.sendButton.clicked.connect(self.prepare_messageAll)
        self.submitButton.clicked.connect(self.getExtraValue)
        self.submitButton_2.clicked.connect(self.getExtraValue)
        self.sendServer.clicked.connect(self.prepare_messageServer)
        self.clearTab1Button.clicked.connect(self.clearTab1)
        self.clearTab2Button.clicked.connect(self.clearTab2)
        self.AutoSendButton.clicked.connect(self.AutoSend)

        self.previous_message = None
        self.second_last_message = None

    #Stores last message received from server
    def on_message_received(self, message):
        self.second_last_message = self.previous_message
        self.previous_message = message

    @staticmethod
    def convert_to_int(value, base=10):
        if isinstance(value, str) and value.isdigit():
            print("qqqqqqqq")
            return int(value, base)
        elif isinstance(value, int):
            print("wwwwwwww")
            return value
        elif isinstance(value, str) and value.lstrip('-').isdigit():
            print("eeeeeeee")
            return int(value, base)
        else:
            raise ValueError(f"Cannot convert {value} to int")

    def closeEvent(self, event):
        """Arrête le thread de réception et ferme la fenêtre proprement."""
        self.receiverThread.stop()
        event.accept()  # Accepte l'événement de fermeture
    #split message to get the last element
    def splitServerMessage(self, message):
        #shift vigenere 
        messageSplit = message.split(" ")
        print("Message split:", messageSplit)
        #retorune le dernier element
        return messageSplit[-1]
    #get RSA key
    def getRSAKey(self, message):
        messageSplit = message.split(" ")
        
        n = messageSplit[-2]
        n = n[2:]
        n = n[:-1]

        e = messageSplit[-1]
        e = e[2:]

        print("n:", n)
        print("e:", e)
        return n, e

    def update_message_display(self, message):
        self.messageDisplay.append(message)  # Afficher les messages normaux

    def update_server_message_display(self, message):
        self.serverDisplay.append(message)  # Afficher les messages du serveur
        self.previous_message = message

    def clearTab1(self):
        self.messageDisplay.clear()

    def clearTab2(self):
        self.serverDisplay.clear()

    def AutoSend(self):
        task = "task"
        type = self.comboTask.currentText()
        encode = self.comboEncode.currentText()
        value = self.spinBox.value()
        txt = ""

        if(type == "Diffie Hellman"):
            txt = task + " DifHel"
            txt_encoded = mainFunctions.string_toListInt(txt)
            self.send_message(txt_encoded, txt)

            time.sleep(1)
            self.autoDifHel()
        elif(type == "RSA" and encode == "encode"):
            txt = str(task) + " " + str(type) + " " + str(encode) + " " + str(value)
            txt_encoded = mainFunctions.string_toListInt(txt)
            self.send_message(txt_encoded, txt)
            time.sleep(2)
            self.autoRSA()
            
        else:
            txt = task + " " + type + " " + encode + " " + str(value)
            txt_encoded = mainFunctions.string_toListInt(txt)
            self.send_message(txt_encoded, txt)

        #appeler les fonctions qui gèrent les différents cas
    
    def autoDifHel(self):
        print("lol")
        a = 33
        #ordre: (p,g, on recoit BenvoiaA, cleCryptageA)
        p = 347
        g = Diffie_Hellman.generator(p)[7]
        AenvoiaB = (g ** a) % p

        #on envoie p,g
        txt = str(p) + "," + str(g)
        print("txt:", txt)
        txt_encoded = mainFunctions.string_toListInt(txt)
        self.send_message(txt_encoded, txt)
        time.sleep(2)

        #on recoit sa demi clé
        BenvoiaA = self.splitServerMessage(self.previous_message)
        print("BenvoiaA:",BenvoiaA)

        #on envoie notre demi clé
        notre_demi = str(AenvoiaB)
        txt_encoded = mainFunctions.string_toListInt(notre_demi)
        self.send_message(txt_encoded, notre_demi)
        time.sleep(2)

        #on envoie la clé de cryptage
        cleCryptageA = (int(BenvoiaA)**a) % p
        wholeKey = str(cleCryptageA)
        txt_encoded = mainFunctions.string_toListInt(wholeKey)
        self.send_message(txt_encoded, wholeKey)

    def autoRSA(self):
        messageKey = self.second_last_message
        n,e = self.getRSAKey(messageKey)
        print("n:", n)
        print("e:", e)

        message = self.previous_message
        print("Message String:", message)
        messageList = mainFunctions.string_toListInt(message)
        print("Message List:", messageList)

        encryptedMessage = rsaFunctions.encryptKey(messageList, int(e), int(n))
        time.sleep(2)

    
        self.send_message(encryptedMessage, message)

    def getExtraValue(self):
        value = self.valueEditor.toPlainText()
        print("Valeur supplémentaire:", value)
        try:
            return value
        except ValueError:
            print("La valeur supplémentaire n'est pas un entier valide.")
            return None
        
    def getExtraValue2(self):
        value = self.valueEditor_2.toPlainText()
        print("Valeur supplémentaire:", value)
        try:
            return value
        except ValueError:
            print("La valeur supplémentaire n'est pas un entier valide.")
            return None

    def receive_message(self, message):
        rcv_msg = message.replace(b'\0', b'')
        rcv_msg = rcv_msg.decode('utf-8')
        rcv_msg = rcv_msg[5:]
        self.on_message_received(rcv_msg)
        print(rcv_msg)
        return(rcv_msg) 
    
    def prepare_messageAll(self):
        txt = self.messageInput.toPlainText()
        if not txt.strip():
            self.messageDisplay.append(">>> Veuillez entrer un texte à envoyer.")
            return
        if self.radioText.isChecked():
            if self.radioNone_3.isChecked():
                txt_encoded = mainFunctions.string_toListInt(txt)
                self.send_message(txt_encoded, txt)
            if self.radioShift_3.isChecked():
                shift = int(self.getExtraValue())
                txt_encoded = mainFunctions.string_toListInt(txt)
                txt_encoded = mainFunctions.shifter(txt_encoded, shift)
                print("Texte encodé AALL :", txt_encoded)
                self.send_message(txt_encoded, txt)
            if self.radioXor_3.isChecked():
                nb = int(self.getExtraValue())
                txt_encoded = mainFunctions.string_toListInt(txt)
                txt_encoded = mainFunctions.xor(txt_encoded, nb)
                self.send_message(txt_encoded, txt)
            if self.radioVigenere_3.isChecked():
                key = self.getExtraValue()
                txt_encoded = mainFunctions.string_toListInt(txt)
                txt_encoded = mainFunctions.vigenere(txt_encoded, key)
                self.send_message(txt_encoded, txt)
        
        if self.radioImage.isChecked():
            self.messageDisplay.append(">>> Envoi d'image non supporté pour le moment.")
            return
        
        if self.radioServer.isChecked():
            if self.radioNone.isChecked():
                self.messageDisplay.append(">>> Select correct message type")
            return
        
    def prepare_messageServer(self):
        txt = self.serverInput.toPlainText()
        if not txt.strip():
            self.serverDisplay.append(">>> Veuillez entrer un texte à envoyer.")
            return
        if self.radioNone.isChecked():
            txt_encoded = mainFunctions.string_toListInt(txt)
            self.send_message(txt_encoded, txt)
        if self.radioShift.isChecked():
            previous_msg = self.second_last_message
            shift = int(self.splitServerMessage(previous_msg))
            savedShift = shift
            txt = self.splitServerMessage(self.previous_message)
            print("BBBBBBBBBBBBBBB")
            txt_encoded = mainFunctions.string_toListInt(txt)
            print("Texte encodé sans shift:", txt_encoded)
            txt_encoded = mainFunctions.shifter(txt_encoded, savedShift)
            print("Texte encode avec shift ", txt_encoded)
            self.send_message(txt_encoded, txt)

        if self.radioXor.isChecked():
            nb = int(self.getExtraValue())
            txt_encoded = mainFunctions.string_toListInt(txt)
            txt_encoded = mainFunctions.xor(txt_encoded, nb)
            self.send_message(txt_encoded, txt)
        if self.radioVigenere.isChecked():
            #server_answer = self.serverDisplay.toPlainText()
            key = self.splitServerMessage(txt)
            txt_encoded = mainFunctions.string_toListInt(txt)
            txt_encoded = mainFunctions.vigenere(txt_encoded, key)
            self.send_message(txt_encoded, txt)

    def send_message(self, txt_encoded, txt):
        try:
            key = "ISC"
            
            
            if self.radioText.isChecked():
                print("Radio Text checked")
                msg = str.encode(key + "t")
            if self.radioImage.isChecked(): 
                print("Radio Image checked")
                msg = str.encode(key + "i")
            if self.radioServer.isChecked():
                print("Radio Server checked")
                msg = str.encode(key + "s")


            longueur_txt = len(txt)
            print(" TXT texte:", txt)
            nb_char = longueur_txt.to_bytes(2,"big")
            txt_encoded = mainFunctions.listInt_toString(txt_encoded)
            print("Texte encodé STRING:", txt_encoded)
            final_text = mainFunctions.word_to_bytes(txt_encoded)
            msg_final = msg + nb_char + final_text
            #print("Message final:", msg_final)
    
            self.sock.send(msg_final)
        except Exception as e:
            print(f"Erreur lors de l'envoi des données: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())