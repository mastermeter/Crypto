import sys
import socket
import mainFunctions, rsaFunctions
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from send_v1 import Ui_MainWindow  # Importez votre classe UI générée

# Configuration du socket
HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect((HOST, port))


class ReceiverThread(QThread):
    received = pyqtSignal(str)

    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            try:
                rcv_msg = self.sock.recv(65536)  # 64Ko
                rcv_msg = rcv_msg.replace(b'\0', b'')
                rcv_msg = rcv_msg.decode('utf-8')
                rcv_msg = rcv_msg[5:]
                print(rcv_msg)

                self.received.emit(">Message received: " + rcv_msg)
            except Exception as e:
                print(f"Erreur lors de la réception des données: {e}")
                break


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.send_message)
        # Socket: 
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, port))
        self.thread = ReceiverThread(self.sock)
        self.thread.received.connect(self.update_message_display)
        self.thread.start()
       
    
    def update_message_display(self, message):
        self.messageDisplay.append(message)  # Afficher le message dans QTextEdit


    def send_message(self):
        try:
            print("Tentative d'envoi de message")
            key = "ISC"
            msg_type = "t"
            msg = str.encode(key + msg_type)
            txt = self.messageInput.toPlainText()  # Récupère le texte de l'interface utilisateur
            print(f"Texte récupéré pour envoi: '{txt}'")  # Affiche le texte récupéré pour le débogage

            txt_encoded = mainFunctions.string_toListInt(txt)
            print(f"Texte encodé en liste d'entiers: {txt_encoded}")  # Affiche le texte encodé pour le débogage

            longueur_txt = len(txt)
            nb_char = longueur_txt.to_bytes(2, "big")
            print(f"Nombre de caractères en bytes: {nb_char}")  # Affiche la longueur du texte en bytes

            txt_encoded = mainFunctions.listInt_toString(txt_encoded)
            print(f"Liste d'entiers convertie en chaîne: {txt_encoded}")  # Affiche la liste d'entiers convertie en chaîne

            final_text = mainFunctions.word_to_bytes(txt_encoded)
            print(f"Texte final à envoyer: {final_text}")  # Affiche le texte final encodé

            msg_final = msg + nb_char + final_text
            print(f"Message final encodé à envoyer: {msg_final}")  # Affiche le message final encodé

            if self.sock:
                print("Socket connecté")
                self.sock.send(msg_final)
                self.messageInput.clear()
                print("Message envoyé avec succès")
            else:
                print("Socket non connecté")
        except Exception as e:
            print(f"Erreur lors de l'envoi du message : {e}")


    def receive_message(self):
        rcv_msg = self.sock.recv(65536)  # 64Ko
        rcv_msg = rcv_msg.replace(b'\0', b'')
        rcv_msg = rcv_msg.decode('utf-8')
        rcv_msg = rcv_msg[5:]
        print(rcv_msg)

        return(rcv_msg) 

    def start_receiving(self):
        import threading
        thread = threading.Thread(target=self.receive_message)
        thread.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.start_receiving()
    sys.exit(app.exec_())


