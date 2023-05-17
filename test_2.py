from PyQt5.QtWidgets import * # *代表所有的class
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow1 import Ui_Dialog
import sys

def clicked_hi():
    message = QMessageBox()
    x = ui.lineEdit.text()
    message.setWindowTitle("surprice")
    message.setInformativeText(x)
    message.exec_()

def clicked_hello():
    ui.label.setText = "Hello"
    print("Hello")

def pic_click(event):
    message = QMessageBox()
    message.setWindowTitle("surprice")
    message.setInformativeText("你按了圖片!!")
    message.exec_()
    

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.Test.clicked.connect(clicked_hi)
ui.helloButton.clicked.connect(clicked_hello)
ui.pic.mouseReleaseEvent = pic_click

widget.show()
app.exec_()