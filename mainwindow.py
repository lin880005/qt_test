# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(330, 290, 60, 30))
        self.add.setObjectName("add")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 180, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 180, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 120, 120, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pic = QtWidgets.QLabel(Dialog)
        self.pic.setGeometry(QtCore.QRect(10, 10, 111, 111))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("s.jpg"))
        self.pic.setScaledContents(True)
        self.pic.setObjectName("pic")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(80, 220, 120, 20))
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 240, 120, 20))
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 260, 120, 20))
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(80, 280, 120, 20))
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(230, 50, 110, 40))
        self.checkBox.setObjectName("checkBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(340, 10, 110, 40))
        self.comboBox.setObjectName("comboBox")
        self.hello1 = QtWidgets.QPushButton(Dialog)
        self.hello1.setGeometry(QtCore.QRect(160, 280, 110, 40))
        self.hello1.setObjectName("hello1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add.setText(_translate("Dialog", "Add"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.radioButton.setText(_translate("Dialog", "+"))
        self.radioButton_2.setText(_translate("Dialog", "-"))
        self.radioButton_3.setText(_translate("Dialog", "*"))
        self.radioButton_4.setText(_translate("Dialog", "/"))
        self.checkBox.setText(_translate("Dialog", "CheckBox"))
        self.hello1.setText(_translate("Dialog", "hello"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
