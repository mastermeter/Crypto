# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys
import threading

# Configuration du socket
HOST = "vlbelintrocrypto.hevs.ch"
port = 6000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect((HOST, port))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(350, 520, 93, 28))
        self.sendButton.setObjectName("sendButton")
        self.sendButton.setText("Envoyer")

        self.messageInput = QtWidgets.QTextEdit(self.centralwidget)
        self.messageInput.setGeometry(QtCore.QRect(50, 50, 700, 100))
        self.messageInput.setObjectName("messageInput")

        self.messageDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.messageDisplay.setGeometry(QtCore.QRect(50, 160, 700, 350))
        self.messageDisplay.setObjectName("messageDisplay")
        self.messageDisplay.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.sendButton.clicked.connect(self.send_message)

    def send_message(self):
        # Gather input from messageInput
        key = "ISC"
        msg_type = "t"  # Use "t" as an example type
        txt = self.messageInput.toPlainText()
        encoding_type = "none"  # No encoding
        
        msg = (key + msg_type).encode()
        txt_encoded = txt.encode()  # Encoding text as bytes

        full_message = msg + txt_encoded  # Concatenate parts of the message
        
        # Send the message
        sock.sendall(full_message)

        # Optional: Clear input after sending
        self.messageInput.clear()

    def receive_message(self):
        # This function should be called in a way that does not block the GUI, such as in a separate thread
        while True:
            data = sock.recv(1024)
            if data:
                message = data.decode('utf-8')
                self.messageDisplay.append(message)

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Start the message receiving function in a separate thread to avoid freezing the GUI
    receive_thread = threading.Thread(target=ui.receive_message)
    receive_thread.daemon = True
    receive_thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
