import sys
import socket

import mainFunctions, rsaFunctions

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication
from testInterfaceTab_ui import Ui_MainWindow  # Importez votre classe UI généré

# Configuration du socket
HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
                message = self.app.receive_message()
                if(self.app.radioServer.isChecked()):
                    print("KEY IN MESSAGE")
                    print("MESSAGE RECEIVED :"+ message)
                    self.receivedServer.emit(">>> Received from server : " + message)  # Message du serveur
                    #message = self.app.getFrom_server()
                    #print("MESSAGE AFTER GET FROM SERVER :"+ message)
                    #self.receivedServer.emit(">>> " + message)  # Message du serveur
                else:
                    self.received.emit(">>>Message received: " + message)  # Message normal

            except Exception as e:
                print(f"Erreur lors de la réception des données: {e}")
                break

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.prepare_messageAll)
        self.submitButton.clicked.connect(self.getExtraValue)
        self.sendServer.clicked.connect(self.prepare_messageServer)  # Ajout du bouton pour envoyer un message au serveur

    def receive_message(self):
        rcv_msg = self.sock.recv(65536)  # 64Ko
        rcv_msg = rcv_msg.replace(b'\0', b'')
        rcv_msg = rcv_msg.decode('utf-8')
        rcv_msg = rcv_msg[5:]
        print(rcv_msg)

        return(rcv_msg) 