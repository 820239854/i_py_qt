import sys

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QLabel, QVBoxLayout, \
    QMessageBox


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.question(self, "Question dialog", "The longer message")

        # QMessageBox.about(parent, title, message)
        # QMessageBox.critical(parent, title, message)
        # QMessageBox.information(parent, title, message)
        # QMessageBox.question(parent, title, message)
        # QMessageBox.warning(parent, title, message)

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()