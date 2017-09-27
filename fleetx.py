from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import fleetsystem, addcarone, repairdetails, servicedetails, editcar,deploycar
import adddriver, fuelservice, recordaccident, otherdeploydriver,removecar, removedriver
class MainClass(QMainWindow, fleetsystem.Ui_fleetx):
    signal = pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.fleetaddcar.triggered.connect(self.addcarshow)
        self.fleetdeploycar.triggered.connect(self.deploycarshow)
        self.fleetadddrive.triggered.connect(self.adddrivershow)
        self.fleeteditcardetails.triggered.connect(self.editcarshow)
        self.fleetclose.triggered.connect(self.close)
        self.fleetfluage.triggered.connect(self.fuelshow)
        self.fleetaccident.triggered.connect(self.accidentshow)
        self.fleetrepair.triggered.connect(self.repairshow)
        self.fleetservices.triggered.connect(self.serviceshow)
        self.fleetdeploydrive.triggered.connect(self.deploydrivershow)
        self.fleetremovecar.triggered.connect(self.removecarshow)
        self.fleetremovedriver.triggered.connect(self.removedrivershow)

    def addcarshow(self):
        self.addcarview = QDialog()
        self.lookaddcar = addcarone.Ui_addcarone()
        self.lookaddcar.setupUi(self.addcarview)
        self.addcarview.show()
        
    def deploycarshow(self):
        self.deploycarview = QDialog()
        self.lookdeploycar = deploycar.Ui_deploycar()
        self.lookdeploycar.setupUi(self.deploycarview)
        self.deploycarview.show()
    
    def adddrivershow(self):
        self.adddriveview = QDialog()
        self.lookadddriver = adddriver.Ui_add_drive()
        self.lookadddriver.setupUi(self.adddriveview)
        self.adddriveview.show()

    def editcarshow(self):
        self.editcarview = QDialog()
        self.lookeditcar = editcar.Ui_editdriver_2()
        self.lookeditcar.setupUi(self.editcarview)
        self.editcarview.show()

    def fuelshow(self):
        self.fuelview = QDialog()
        self.lookfuel = fuelservice.Ui_fueldetails()
        self.lookfuel.setupUi(self.fuelview)
        self.fuelview.show()

    def accidentshow(self):
        self.accidentview = QDialog()
        self.lookaccident = recordaccident.Ui_accidentevent()
        self.lookaccident.setupUi(self.accidentview)
        self.accidentview.show()

    def repairshow(self):
        self.repairview = QDialog()
        self.lookrepair = repairdetails.Ui_repaircar()
        self.lookrepair.setupUi(self.repairview)
        self.repairview.show()
    def serviceshow(self):
        self.serviceview = QDialog()
        self.lookservice = servicedetails.Ui_servicedetails()
        self.lookservice.setupUi(self.serviceview)
        self.serviceview.show()
    
    def deploydrivershow(self):
        self.deploydriverview = QDialog()
        self.lookdeploydriver = otherdeploydriver.Ui_otherdeploy()
        self.lookdeploydriver.setupUi(self.deploydriverview)
        self.deploydriverview.show()
    
    def removecarshow(self):
        self.removecarview = QDialog()
        self.lookremovecar = removecar.Ui_removecar()
        self.lookremovecar.setupUi(self.removecarview)
        self.removecarview.show()
    
    def removedrivershow(self):
        self.removedriverview=QDialog()
        self.lookremovedriver = removedriver.Ui_removedriver()
        self.lookremovedriver.setupUi(self.removedriverview)
        self.removedriverview.show()

if __name__ =="__main__":
    apo = QApplication(sys.argv)
    appshow = MainClass()
    appshow.show()
    apo.exec_()