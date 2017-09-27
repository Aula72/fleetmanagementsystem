from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import deploycar

class DeployCar(QDialog, deploycar.Ui_deploycar):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.deploycarbutton.pressed.connect(self.close)
    
#if __name__=="__main__":
    def showme(self):
        self.showdeploy = QDialog()
        self.ourdeploy = DeployCar()
        self.showdeploy.show()
