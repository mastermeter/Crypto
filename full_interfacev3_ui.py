# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'full.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
         # Création des instances de QButtonGroup
        self.buttonGroup1 = QtWidgets.QButtonGroup(MainWindow)  # Groupe pour les types de messages
        self.buttonGroup2 = QtWidgets.QButtonGroup(MainWindow)  # Groupe pour les types d'encodage

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 770)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 24, 761, 681))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelMessageType = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelMessageType.setFont(font)
        self.labelMessageType.setObjectName("labelMessageType")
        self.verticalLayout_3.addWidget(self.labelMessageType)

        self.radioText = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioText.setFont(font)
        self.radioText.setObjectName("radioText")
        self.verticalLayout_3.addWidget(self.radioText)
        self.buttonGroup1.addButton(self.radioText)

        self.radioImage = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioImage.setFont(font)
        self.radioImage.setObjectName("radioImage")
        self.verticalLayout_3.addWidget(self.radioImage)
        self.buttonGroup1.addButton(self.radioImage)

        self.radioServer = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioServer.setFont(font)
        self.radioServer.setObjectName("radioServer")
        self.verticalLayout_3.addWidget(self.radioServer)
        self.buttonGroup1.addButton(self.radioServer)
        
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelEncodingType = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelEncodingType.setFont(font)
        self.labelEncodingType.setObjectName("labelEncodingType")
        self.gridLayout.addWidget(self.labelEncodingType, 0, 0, 1, 2)

        self.radioNone = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioNone.setFont(font)
        self.radioNone.setObjectName("radioNone")
        self.gridLayout.addWidget(self.radioNone, 1, 0, 1, 1)
        self.buttonGroup2.addButton(self.radioNone)

        self.radioVigenere = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioVigenere.setFont(font)
        self.radioVigenere.setObjectName("radioVigenere")
        self.gridLayout.addWidget(self.radioVigenere, 1, 1, 1, 1)
        self.buttonGroup2.addButton(self.radioVigenere)

        self.radioShift = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioShift.setFont(font)
        self.radioShift.setObjectName("radioShift")
        self.gridLayout.addWidget(self.radioShift, 2, 0, 1, 1)
        self.buttonGroup2.addButton(self.radioShift)

        self.radioRSA = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioRSA.setFont(font)
        self.radioRSA.setObjectName("radioRSA")
        self.gridLayout.addWidget(self.radioRSA, 2, 1, 1, 1)
        self.buttonGroup2.addButton(self.radioRSA)

        self.radioXor = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioXor.setFont(font)
        self.radioXor.setObjectName("radioXor")
        self.gridLayout.addWidget(self.radioXor, 3, 0, 1, 1)
        self.buttonGroup2.addButton(self.radioXor)

        self.radioDiffie = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioDiffie.setFont(font)
        self.radioDiffie.setObjectName("radioDiffie")
        self.gridLayout.addWidget(self.radioDiffie, 3, 1, 1, 1)
        self.buttonGroup2.addButton(self.radioDiffie)


        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelExtraEditor = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelExtraEditor.setFont(font)
        self.labelExtraEditor.setObjectName("labelExtraEditor")
        self.verticalLayout_4.addWidget(self.labelExtraEditor)
        self.valueEditor = QtWidgets.QTextEdit(self.layoutWidget)
        self.valueEditor.setObjectName("valueEditor")
        self.verticalLayout_4.addWidget(self.valueEditor)
        self.submitButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout_4.addWidget(self.submitButton)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.labelEnterText = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labelEnterText.setFont(font)
        self.labelEnterText.setObjectName("labelEnterText")
        self.verticalLayout_2.addWidget(self.labelEnterText)
        self.messageInput = QtWidgets.QTextEdit(self.layoutWidget)
        self.messageInput.setObjectName("messageInput")
        self.verticalLayout_2.addWidget(self.messageInput)
        self.sendButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout_2.addWidget(self.sendButton)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 8)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelReceivedMessage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelReceivedMessage.setFont(font)
        self.labelReceivedMessage.setObjectName("labelReceivedMessage")
        self.verticalLayout.addWidget(self.labelReceivedMessage)
        self.messageDisplay = QtWidgets.QTextEdit(self.layoutWidget)
        self.messageDisplay.setReadOnly(True)
        self.messageDisplay.setObjectName("messageDisplay")
        self.verticalLayout.addWidget(self.messageDisplay)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelFromServer = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelFromServer.setFont(font)
        self.labelFromServer.setObjectName("labelFromServer")
        self.verticalLayout_5.addWidget(self.labelFromServer)
        self.serverDisplay = QtWidgets.QTextEdit(self.layoutWidget)
        self.serverDisplay.setReadOnly(True)
        self.serverDisplay.setObjectName("serverDisplay")
        self.verticalLayout_5.addWidget(self.serverDisplay)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projet Crypto"))
        self.labelMessageType.setText(_translate("MainWindow", "Message type :"))
        self.radioText.setText(_translate("MainWindow", "Text"))
        self.radioImage.setText(_translate("MainWindow", "Image"))
        self.radioServer.setText(_translate("MainWindow", "Server"))
        self.labelEncodingType.setText(_translate("MainWindow", "Encoding Type : "))
        self.radioNone.setText(_translate("MainWindow", "None"))
        self.radioVigenere.setText(_translate("MainWindow", "Vigenere"))
        self.radioShift.setText(_translate("MainWindow", "Shift"))
        self.radioRSA.setText(_translate("MainWindow", "RSA"))
        self.radioXor.setText(_translate("MainWindow", "Xor"))
        self.radioDiffie.setText(_translate("MainWindow", "Diffie Hellman"))
        self.labelExtraEditor.setText(_translate("MainWindow", "Extra values:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.labelEnterText.setText(_translate("MainWindow", "Enter your text here :"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.labelReceivedMessage.setText(_translate("MainWindow", "Received Messages :"))
        self.labelFromServer.setText(_translate("MainWindow", "Received from server :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
