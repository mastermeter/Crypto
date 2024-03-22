import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QFile
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_ui()
        
    def load_ui(self):
        ui_file = QFile("test1.ui")  # Remplacez "your_ui_file.ui" par le chemin de votre fichier UI
        ui_file.open(QFile.ReadOnly)
        loadUi(ui_file, self)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())