import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.vlayout = QVBoxLayout(self)
        self.label = QLabel('Test Label', self)
        self.vlayout.addWidget(self.label)
        self.setLayout(self.vlayout)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Simple Window')

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Utiliser sys.argv ici
    win = SimpleWindow()
    win.show()
    sys.exit(app.exec_())
