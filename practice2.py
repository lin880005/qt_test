from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from practice import Ui_Dialog
import sys


app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)

def pic_click(event):
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("你按了圖片")
    message.exec_()
    print(event.x())
    print(event.y())
    print(event.button())
    
def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def press():
    x = ui.lineEdit.text()
    y = ui.lineEdit_2.text()
    """if not is_float(x) or not is_float(y):
        message = QMessageBox()
        message.setWindowTitle("error")
        message.setInformativeText("請輸入數字")
        message.exec_()
        return
    if ui.radioButton.isChecked():
        ans = float(x)+float(y) 
    """
    if is_float(x) and is_float(y):
        if ui.radioButton.isChecked():
            ans = float(x)+float(y)
        elif ui.radioButton_2.isChecked():
            ans = float(x)-float(y)
        elif ui.radioButton_3.isChecked():
            ans = float(x)*float(y)
        elif ui.radioButton_4.isChecked():
            ans = float(x)/float(y)
        ui.label.setText(str(ans))
    else:
        message = QMessageBox()
        message.setWindowTitle("error")
        message.setInformativeText("請輸入數字")
        message.exec_()

ui.pic2.mouseReleaseEvent = pic_click
group1 = QButtonGroup(widge)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
group1.addButton(ui.radioButton_3)
group1.addButton(ui.radioButton_4)
ui.radioButton.clicked.connect(press)
ui.radioButton_2.clicked.connect(press)
ui.radioButton_3.clicked.connect(press)
ui.radioButton_4.clicked.connect(press)
ui.pushButton.clicked.connect(press)

widge.show()
sys.exit(app.exec_())