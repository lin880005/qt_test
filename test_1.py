from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from mainwindow import Ui_Dialog
import sys

app = QApplication(sys.argv)
widge = QWidget()
ui = Ui_Dialog()
ui.setupUi(widge)
widge.show()
app.exec_()