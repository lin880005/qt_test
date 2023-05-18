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
    ui.progressBar.setValue(90)

def clicked_hello():
    ui.label.setText = "Hello"
    print("Hello")
    ui.progressBar.setValue(40)

def pic_click(event):
    message = QMessageBox()
    message.setWindowTitle("surprice")
    message.setInformativeText("你按了圖片!!")
    message.exec_()
    
def slider_change():
    x = ui.horizontalSlider.value()
    print(f"change it is : {x}")

def slider_release():
    message = QMessageBox()
    message.setWindowTitle("surprice")
    message.setInformativeText("你選擇的是!! "+str(ui.horizontalSlider.value()))
    message.exec_()
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
ui.progressBar.setValue(3)
ui.horizontalSlider.setMaximum(110)
ui.horizontalSlider.setMinimum(-3)
ui.horizontalSlider.valueChanged.connect(slider_change)
ui.horizontalSlider.sliderReleased.connect(slider_release)


ui.Test.clicked.connect(clicked_hi)
ui.helloButton.clicked.connect(clicked_hello)
ui.pic.mouseReleaseEvent = pic_click

widget.show()
app.exec_()