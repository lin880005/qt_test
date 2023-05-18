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

        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider_2.setMaximum(100)
        self.ui.horizontalSlider_2.setMinimum(0)
        self.ui.horizontalSlider.valueChanged.connect(self.slider_change)
        self.ui.horizontalSlider_2.valueChanged.connect(self.slider_change1)
        #self.ui.horizontalSlider.sliderReleased.connect(self.slider_release)
        self.ui.progressBar.setValue(0)
        
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
            z = (float(x)+float(y))*float(self.num)
            return z
        elif self.ui.radioButton_2.isChecked():
            z = (float(x)-float(y))*float(self.num)
            return z
        elif self.ui.radioButton_3.isChecked():
            z = (float(x)*float(y))*float(self.num)
            return z
        elif self.ui.radioButton_4.isChecked():
            z = (float(x)/float(y))*float(self.num)
            return z
    
    def slider_change(self):
        self.num = self.ui.horizontalSlider.value()
        self.ui.progressBar.setValue(self.num)
       
    
    def slider_change1(self):
        self.num1 = self.ui.horizontalSlider_2.value()
        self.ui.pic.setGeometry(QtCore.QRect(int(80-int(self.num1)), int(50-(self.num1)), int(100+(self.num1*4)), int(100+(self.num1*4))))
    
    """def slider_release(self):
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("surprice")
        message.setInformativeText("你選擇的是!! "+str(self.ui.horizontalSlider.value()))
        message.exec_()"""
        
if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())