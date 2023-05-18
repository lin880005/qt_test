from PyQt5 import QtWidgets,QtCore,QtGui
from mainwindow import Ui_Dialog
import sys

class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.hello.clicked.connect(self.clicked_button)
        group1 = QtWidgets.QButtonGroup(self)
        group1.addButton(self.ui.radioButton)
        group1.addButton(self.ui.radioButton_2)
        group1.addButton(self.ui.radioButton_3)
        group1.addButton(self.ui.radioButton_4)

        self.ui.pic.mouseReleaseEvent = self.pic_click

        self.ui.add.clicked.connect(self.clicked_button)
        self.ui.radioButton.clicked.connect(self.clicked_button)
        self.ui.radioButton_2.clicked.connect(self.clicked_button)
        self.ui.radioButton_3.clicked.connect(self.clicked_button)
        self.ui.radioButton_4.clicked.connect(self.clicked_button)
        self.ui.comboBox.addItems(["中文","English"])

    def isfloat(self,num):
        try:
            float(num)
            return True
        except:
            return False

    def clicked_button(self):
        x = self.ui.lineEdit.text()
        y = self.ui.lineEdit_2.text()
        if self.ui.checkBox.isChecked():
            x,y = y,x
        
        if self.isfloat(x) and self.isfloat(y):
            if self.ui.comboBox.currentIndex() == 0:
                self.ui.label.setText("答案是 : "+str(self.radio_click(x,y)))
            elif  self.ui.comboBox.currentIndex() == 1:
                self.ui.label.setText("ans is :{} ".format(str(self.radio_click(x,y))))
            else:
                self.ui.label.setText("ans is:{} ".format(str(self.radio_click(x,y))))
        else: 
            message =QtWidgets.QMessageBox()
            message.setWindowTitle("ERROR")
            message.setInformativeText("error 請輸入數字!!!")
            message.exec_()

    def pic_click(self,event):
        message =QtWidgets.QMessageBox()
        message.setWindowTitle("surprice")
        message.setInformativeText("你按錯圖片了!!")
        message.exec_()
        print(event.x(),event.y(),sep=",")
        print(event.button())

    def radio_click(self,x,y):
        if self.ui.radioButton.isChecked():
            z = float(x)+float(y)
            return z
        elif self.ui.radioButton_2.isChecked():
            z = float(x)-float(y)
            return z
        elif self.ui.radioButton_3.isChecked():
            z = float(x)*float(y)
            return z
        elif self.ui.radioButton_4.isChecked():
            z = float(x)/float(y)
            return z
        

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())