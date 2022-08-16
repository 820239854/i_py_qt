import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)  # <1>
        self.canvas.fill(Qt.GlobalColor.white)  # <2>

        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
