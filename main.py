from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 446)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 49, 380, 380))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Создать"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.event = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.event = True
        self.update()

    def paintEvent(self, event):
        if self.event:
            qp = QPainter()
            qp.begin(self)
            self.draw_square(qp)
            qp.end()

    def draw_square(self, qp):
        for i in range(5):
            self.size = randint(30, 150)
            self.x = randint(0, 380 - self.size)
            self.y = randint(0, 380 - self.size)
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            qp.drawEllipse(self.x, self.y, self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

