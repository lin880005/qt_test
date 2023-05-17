from PyQt5.QtWidgets import * # *代表所有的class
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_Dialog
import sys

def isfloat(num):
    try:
        float(num)
        return True
    except:
        return False

def click():
    x = ui.lineEdit.text()
    y = ui.lineEdit_2.text()
    if ui.checkBox.isChecked():
        x,y = y,x
        
    if isfloat(x) and isfloat(y):
        if ui.comboBox.currentIndex() == 0:
            ui.label.setText("答案是 : "+str(radio_click(x,y)))
        elif  ui.comboBox.currentIndex() == 1:
            ui.label.setText("ans is :{} ".format(str(radio_click(x,y))))
    else: 
        message = QMessageBox()
        message.setWindowTitle("ERROR")
        message.setInformativeText("error 請輸入數字!!!")
        message.exec_()
       
def pic_click(event):
    message = QMessageBox()
    message.setWindowTitle("surprice")
    message.setInformativeText("你按錯圖片了!!")
    message.exec_()
    print(event.x(),event.y(),sep=",")
    print(event.button())

def radio_click(x,y):
    if ui.radioButton.isChecked():
        z = float(x)+float(y)
        return z
    elif ui.radioButton_2.isChecked():
        z = float(x)-float(y)
        return z
    elif ui.radioButton_3.isChecked():
        z = float(x)*float(y)
        return z
    elif ui.radioButton_4.isChecked():
        z = float(x)/float(y)
        return z

def chang(i):
    pass
app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

group1 = QButtonGroup(widget)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
group1.addButton(ui.radioButton_3)
group1.addButton(ui.radioButton_4)

ui.pic.mouseReleaseEvent = pic_click

ui.add.clicked.connect(click)
ui.radioButton.clicked.connect(click)
ui.radioButton_2.clicked.connect(click)
ui.radioButton_3.clicked.connect(click)
ui.radioButton_4.clicked.connect(click)
ui.comboBox.addItems(["中文","英文"])
ui.comboBox.activated.connect(chang)


widget.show()
app.exec_()