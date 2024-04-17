import sys
import socket

import mainFunctions, rsaFunctions

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from full_interfacev3_ui import Ui_MainWindow  # Importez votre classe UI généré

# Configuration du socket
HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

COMMANDS = {
    "shift", "vigenere", "rsa",
    "encode", "decode",
    "[0<x<10000]"
}

class ReceiverThread(QThread):
    received = pyqtSignal(str)
    receivedServer = pyqtSignal(str)  # Pour les messages du serveur


    def __init__(self, app, sock):
        super().__init__()
        self.app = app
        self.sock = sock

    def run(self):
        while True:
            try:
                message = self.receive_message()
                # Supposons que vous pouvez distinguer les messages serveur par un préfixe ou une structure spécifique
                if any(cmd in message for cmd in COMMANDS):
                    message = self.app.getFrom_server(self)
                    self.receivedServer.emit(">>> Received from server :" + message)  # Message du serveur
                else:
                    message = self.app.receive_message(self)
                    self.received.emit(">>>Message received: " + message)  # Message normal

                #rcv_msg = MyApp.receive_message(self)
                #self.received.emit(">>>Message received: " + rcv_msg)
                #server_msg = MyApp.getFrom_server(self)
                #self.received.emit(">>>Server message: " + server_msg)
            except Exception as e:
                print(f"Erreur lors de la réception des données: {e}")
                break

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.prepare_message)
        self.submitButton.clicked.connect(self.getExtraValue)
        # Socket: 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, port))
        self.thread = ReceiverThread(self, self.sock)
        self.thread.received.connect(self.update_message_display)
        self.thread.receivedServer.connect(self.update_server_display)
        self.thread.start()

    
    def getExtraValue(self):
        value = self.valueEditor.toPlainText()
        print("Valeur supplémentaire:", value)
        try:
            return int(value)
        except ValueError:
            print("La valeur supplémentaire n'est pas un entier valide.")
            return None
   
    def update_message_display(self, message):
        self.messageDisplay.append(message)  # Afficher le message dans QTextEdit

    def update_server_display(self, message):
        self.serverDisplay.append(message)

    def receive_message(self):
        rcv_msg = self.sock.recv(65536)  # 64Ko
        rcv_msg = rcv_msg.replace(b'\0', b'')
        rcv_msg = rcv_msg.decode('utf-8')
        rcv_msg = rcv_msg[5:]
        print(rcv_msg)

        return(rcv_msg) 
    
    def getFrom_server(self):
        server_msg = self.receive_message()
        server_msg = server_msg[20:]
        print(server_msg)
        return server_msg

    def start_receiving(self):
        import threading
        thread = threading.Thread(target=self.receive_message)
        thread.start()

    def prepare_message(self):
        #self.messageDisplay.append(">>> Entrez votre message:")
        txt = self.messageInput.toPlainText()
        if not txt.strip():
            self.messageDisplay.append(">>> Veuillez entrer un texte à envoyer.")
            return

        if self.radioText.isChecked():
            if self.radioNone.isChecked():
                txt_encoded = mainFunctions.string_toListInt(txt)
                self.send_message(txt_encoded, txt)
            if self.radioShift.isChecked():
                shift = self.getExtraValue()
                txt_encoded = mainFunctions.string_toListInt(txt)
                txt_encoded = mainFunctions.shifter(txt_encoded, shift)
                self.send_message(txt_encoded, txt)
            if self.radioXor.isChecked():
                nb = self.getExtraValue()
                txt_encoded = mainFunctions.string_toListInt(txt)
                txt_encoded = mainFunctions.xor(txt_encoded, nb)
                self.send_message(txt_encoded, txt)
        
        if self.radioImage.isChecked():
            self.messageDisplay.append(">>> Envoi d'image non supporté pour le moment.")
            return
        
        if self.radioServer.isChecked():
            if self.radioNone.isChecked():
                txt_encoded = mainFunctions.string_toListInt(txt)
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
            nb_char = longueur_txt.to_bytes(2,"big")
            txt_encoded = mainFunctions.listInt_toString(txt_encoded)
            final_text = mainFunctions.word_to_bytes(txt_encoded)
            msg_final = msg + nb_char + final_text
    

            self.sock.send(msg_final)
        except Exception as e:
            print(f"Erreur lors de l'envoi des données: {e}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.start_receiving()
    sys.exit(app.exec_())