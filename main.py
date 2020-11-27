from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.event = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.event = True
        self.update()

    def paintEvent(self, event):
        if self.event:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 226, 6))
            self.draw_square(qp)
            qp.end()

    def draw_square(self, qp):
        for i in range(5):
            self.size = randint(30, 150)
            self.x = randint(0, 380 - self.size)
            self.y = randint(0, 380 - self.size)
            qp.drawEllipse(self.x, self.y, self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

