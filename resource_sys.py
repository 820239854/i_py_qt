# pyside6-rcc resources.qrc -o resources.py
import sys
from PySide6 import QtGui, QtWidgets

# import ui_files.res_rc  # Import the compiled resource file.
from ui_files.MainWindow2 import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        b = QtWidgets.QPushButton("My button")

        icon = QtGui.QIcon(":/icon/animal-penguin.png")
        b.setIcon(icon)
        self.setCentralWidget(b)
        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()