import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("?")

        # we start it using.exec() - just like we did for QApplication to create the main event loop of our application.
        # That’s not a coincidence: when you exec the QDialog an entirely new event loop - specific for the dialog - is created.
        dlg.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()