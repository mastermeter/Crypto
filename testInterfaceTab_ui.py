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
        self.buttonTab1Group1 = QtWidgets.QButtonGroup(MainWindow)  # Groupe pour les types de messages
        self.buttonTab1Group2 = QtWidgets.QButtonGroup(MainWindow)  # Groupe pour les types d'encodage
        self.buttonTab2Group1 = QtWidgets.QButtonGroup(MainWindow)  # Groupe pour les types de messages
        self.buttonTab2Group2 = QtWidgets.QButtonGroup(MainWindow)  # Groupe pour les types d'encodage

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1345, 848)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(80, 40, 1241, 741))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 1201, 671))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.radioRSA_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioRSA_3.setFont(font)
        self.radioRSA_3.setObjectName("radioRSA_3")
        self.gridLayout_4.addWidget(self.radioRSA_3, 3, 1, 1, 1)
        self.buttonTab1Group1.addButton(self.radioRSA_3)


        self.radioXor_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioXor_3.setFont(font)
        self.radioXor_3.setObjectName("radioXor_3")
        self.gridLayout_4.addWidget(self.radioXor_3, 4, 0, 1, 1)
        self.buttonTab1Group1.addButton(self.radioXor_3)

        self.radioVigenere_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioVigenere_3.setFont(font)
        self.radioVigenere_3.setObjectName("radioVigenere_3")
        self.gridLayout_4.addWidget(self.radioVigenere_3, 2, 1, 1, 1)
        self.buttonTab1Group1.addButton(self.radioVigenere_3)

        self.radioNone_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioNone_3.setFont(font)
        self.radioNone_3.setObjectName("radioNone_3")
        self.gridLayout_4.addWidget(self.radioNone_3, 2, 0, 1, 1)
        self.buttonTab1Group1.addButton(self.radioNone_3)

        self.radioShift_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioShift_3.setFont(font)
        self.radioShift_3.setObjectName("radioShift_3")
        self.gridLayout_4.addWidget(self.radioShift_3, 3, 0, 1, 1)
        self.buttonTab1Group1.addButton(self.radioShift_3)

        self.labelEncodingType_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelEncodingType_3.setFont(font)
        self.labelEncodingType_3.setObjectName("labelEncodingType_3")
        self.gridLayout_4.addWidget(self.labelEncodingType_3, 1, 0, 1, 2)

        self.radioDiffie_3 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioDiffie_3.setFont(font)
        self.radioDiffie_3.setObjectName("radioDiffie_3")
        self.gridLayout_4.addWidget(self.radioDiffie_3, 4, 1, 1, 1)
        self.buttonTab1Group1.addButton(self.radioDiffie_3)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelMessageType_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelMessageType_2.setFont(font)
        self.labelMessageType_2.setObjectName("labelMessageType_2")
        self.verticalLayout_8.addWidget(self.labelMessageType_2)

        self.radioText = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioText.setFont(font)
        self.radioText.setObjectName("radioText")
        self.verticalLayout_8.addWidget(self.radioText)
        self.buttonTab1Group2.addButton(self.radioText)
        
        self.radioImage = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioImage.setFont(font)
        self.radioImage.setObjectName("radioImage")
        self.verticalLayout_8.addWidget(self.radioImage)
        self.buttonTab1Group2.addButton(self.radioImage)

        self.gridLayout_4.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
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
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.clearTab1Button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.clearTab1Button.setFont(font)
        self.clearTab1Button.setObjectName("clearTab1Button")
        self.verticalLayout_9.addWidget(self.clearTab1Button)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
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
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.labelExtraEditor_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelExtraEditor_2.setFont(font)
        self.labelExtraEditor_2.setObjectName("labelExtraEditor_2")
        self.verticalLayout_12.addWidget(self.labelExtraEditor_2)
        self.valueEditor_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.valueEditor_2.setObjectName("valueEditor_2")
        self.verticalLayout_12.addWidget(self.valueEditor_2)
        self.submitButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.submitButton_2.setFont(font)
        self.submitButton_2.setObjectName("submitButton_2")
        self.verticalLayout_12.addWidget(self.submitButton_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_12)
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
        self.verticalLayout_2.setStretch(0, 3)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setGeometry(QtCore.QRect(20, 30, 1201, 671))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelMessageType = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelMessageType.setFont(font)
        self.labelMessageType.setObjectName("labelMessageType")
        self.verticalLayout_3.addWidget(self.labelMessageType)

        self.radioServer = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioServer.setFont(font)
        self.radioServer.setObjectName("radioServer")
        self.verticalLayout_3.addWidget(self.radioServer)
        self.buttonTab2Group2.addButton(self.radioServer)

        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelEncodingType = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelEncodingType.setFont(font)
        self.labelEncodingType.setObjectName("labelEncodingType")
        self.gridLayout.addWidget(self.labelEncodingType, 0, 0, 1, 2)

        self.radioNone = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioNone.setFont(font)
        self.radioNone.setObjectName("radioNone")
        self.gridLayout.addWidget(self.radioNone, 1, 0, 1, 1)
        self.buttonTab2Group1.addButton(self.radioNone)

        self.radioVigenere = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioVigenere.setFont(font)
        self.radioVigenere.setObjectName("radioVigenere")
        self.gridLayout.addWidget(self.radioVigenere, 1, 1, 1, 1)
        self.buttonTab2Group1.addButton(self.radioVigenere)

        self.radioShift = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioShift.setFont(font)
        self.radioShift.setObjectName("radioShift")
        self.gridLayout.addWidget(self.radioShift, 2, 0, 1, 1)
        self.buttonTab2Group1.addButton(self.radioShift)

        self.radioRSA = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioRSA.setFont(font)
        self.radioRSA.setObjectName("radioRSA")
        self.gridLayout.addWidget(self.radioRSA, 2, 1, 1, 1)
        self.buttonTab2Group1.addButton(self.radioRSA)

        self.radioXor = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioXor.setFont(font)
        self.radioXor.setObjectName("radioXor")
        self.gridLayout.addWidget(self.radioXor, 3, 0, 1, 1)
        self.buttonTab2Group1.addButton(self.radioXor)

        self.radioDiffie = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.radioDiffie.setFont(font)
        self.radioDiffie.setObjectName("radioDiffie")
        self.gridLayout.addWidget(self.radioDiffie, 3, 1, 1, 1)
        self.buttonTab2Group1.addButton(self.radioDiffie)

        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelFromServer = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelFromServer.setFont(font)
        self.labelFromServer.setObjectName("labelFromServer")
        self.verticalLayout_5.addWidget(self.labelFromServer)
        self.serverDisplay = QtWidgets.QTextEdit(self.layoutWidget1)
        self.serverDisplay.setReadOnly(True)
        self.serverDisplay.setObjectName("serverDisplay")
        self.verticalLayout_5.addWidget(self.serverDisplay)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SendtoServer = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SendtoServer.setFont(font)
        self.SendtoServer.setObjectName("SendtoServer")
        self.verticalLayout_6.addWidget(self.SendtoServer)
        self.serverInput = QtWidgets.QTextEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.serverInput.setFont(font)
        self.serverInput.setObjectName("serverInput")
        self.verticalLayout_6.addWidget(self.serverInput)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.sendServer = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.sendServer.setFont(font)
        self.sendServer.setObjectName("sendServer")
        self.verticalLayout_7.addWidget(self.sendServer)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboEncode = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.comboEncode.setFont(font)
        self.comboEncode.setObjectName("comboEncode")
        self.comboEncode.addItem("")
        self.comboEncode.addItem("")
        self.comboEncode.addItem("")
        self.horizontalLayout_2.addWidget(self.comboEncode)
        self.comboTask = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.comboTask.setFont(font)
        self.comboTask.setEditable(False)
        self.comboTask.setObjectName("comboTask")
        self.comboTask.addItem("")
        self.comboTask.addItem("")
        self.comboTask.addItem("")
        self.comboTask.addItem("")
        self.horizontalLayout_2.addWidget(self.comboTask)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(10000)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.clearTab2Button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.clearTab2Button.setFont(font)
        self.clearTab2Button.setObjectName("clearTab2Button")
        self.gridLayout_2.addWidget(self.clearTab2Button, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1345, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projet Crypto"))
        self.radioRSA_3.setText(_translate("MainWindow", "RSA"))
        self.radioXor_3.setText(_translate("MainWindow", "Xor"))
        self.radioVigenere_3.setText(_translate("MainWindow", "Vigenere"))
        self.radioNone_3.setText(_translate("MainWindow", "None"))
        self.radioShift_3.setText(_translate("MainWindow", "Shift"))
        self.labelEncodingType_3.setText(_translate("MainWindow", "Encoding Type : "))
        self.radioDiffie_3.setText(_translate("MainWindow", "Diffie Hellman"))
        self.labelMessageType_2.setText(_translate("MainWindow", "Message type :"))
        self.radioText.setText(_translate("MainWindow", "Text"))
        self.radioImage.setText(_translate("MainWindow", "Image"))
        self.labelReceivedMessage.setText(_translate("MainWindow", "All messages :"))
        self.clearTab1Button.setText(_translate("MainWindow", "Clear"))
        self.labelExtraEditor.setText(_translate("MainWindow", "Extra values :"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.labelExtraEditor_2.setText(_translate("MainWindow", "Extra values :"))
        self.submitButton_2.setText(_translate("MainWindow", "Submit"))
        self.labelEnterText.setText(_translate("MainWindow", "Message all : "))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "All"))
        self.labelMessageType.setText(_translate("MainWindow", "Message type :"))
        self.radioServer.setText(_translate("MainWindow", "Server"))
        self.labelEncodingType.setText(_translate("MainWindow", "Encoding Type : "))
        self.radioNone.setText(_translate("MainWindow", "None"))
        self.radioVigenere.setText(_translate("MainWindow", "Vigenere"))
        self.radioShift.setText(_translate("MainWindow", "Shift"))
        self.radioRSA.setText(_translate("MainWindow", "RSA"))
        self.radioXor.setText(_translate("MainWindow", "Xor"))
        self.radioDiffie.setText(_translate("MainWindow", "Diffie Hellman"))
        self.labelFromServer.setText(_translate("MainWindow", "Received from server :"))
        self.SendtoServer.setText(_translate("MainWindow", "Message server :"))
        self.sendServer.setText(_translate("MainWindow", "Send"))
        self.comboEncode.setItemText(0, _translate("MainWindow", "encode"))
        self.comboEncode.setItemText(1, _translate("MainWindow", "decode"))
        self.comboEncode.setItemText(2, _translate("MainWindow", "none"))
        self.comboTask.setCurrentText(_translate("MainWindow", "shift"))
        self.comboTask.setItemText(0, _translate("MainWindow", "shift"))
        self.comboTask.setItemText(1, _translate("MainWindow", "vigenere"))
        self.comboTask.setItemText(2, _translate("MainWindow", "RSA"))
        self.comboTask.setItemText(3, _translate("MainWindow", "Diffie Hellman"))
        self.clearTab2Button.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Server"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())