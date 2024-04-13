import sys
import socket
import mainFunctions
import rsaFunctions
from PyQt5.QtWidgets import QMainWindow, QApplication
from send_v1 import Ui_MainWindow  # Importez votre classe UI générée

HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

class ChatWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.messageDisplay.append("TESSSST")
        self.sendButton.clicked.connect(self.handle_user_input)
        self.messageDisplay.append("Hello")
        #self.messageDisplay.clear()
        
    
    def handle_user_input(self):
        # Récupérer le texte de QTextEdit
        user_input = self.messageInput.toPlainText()

        # Utiliser la variable user_input comme nécessaire
        # Par exemple, stocker la réponse dans une autre variable
        self.last_user_response = user_input

        # Afficher la réponse ou faire autre chose
        #print("Réponse de l'utilisateur:", user_input)

        # Effacer le contenu du QTextEdit
        self.messageInput.clear()

    def send_message(self):
        msg = ""
        txt_encoded = ""
        key_isc = "ISC"
        msg_type = ""

        self.messageDisplay.append("Entrez un type de message : (t,i,s)")
        msg_type = self.handle_user_input
        self.messageDisplay.append(msg_type)


        if msg_type != "t" and msg_type != "i" and msg_type != "s":
            self.messageDisplay.append("Type de message non reconnu")
            self.messageDisplay.append("Entrez un type de message : (t,i,s) : ")
            msg_type = self.messageInput.toPlainText()

        msg = str.encode(key_isc + msg_type)
        self.messageDisplay.append("Entrez votre texte : ")
        txt = self.messageInput.toPlainText()

        self.messageDisplay.append("Entrez un type d'encodage : ")
        encoding_type = self.messageInput.toPlainText()

        if encoding_type == "none":
            txt_encoded = mainFunctions.string_toListInt(txt)

        longueur_txt = len(txt)
        nb_char = longueur_txt.to_bytes(2,"big")

        txt_encoded = mainFunctions.listInt_toString(txt_encoded)
    
        final_text = mainFunctions.word_to_bytes(txt_encoded)
    
        msg_final = msg + nb_char + final_text
    
        sock.send(msg_final)



    def receive_message(self):
        rcv_msg = sock.recv(65536)
        rcv_msg = rcv_msg.replace(b'\0', b'')
        rcv_msg = rcv_msg.decode('utf-8')
        rcv_msg = rcv_msg[5:]

        self.messageDisplay.append("Message recieved: " + rcv_msg) 
        print(rcv_msg)  # Ou afficher dans l'interface

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    #window.send_message()
    #window.receive_message()
    sys.exit(app.exec_())
