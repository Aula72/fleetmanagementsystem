from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import xfleetmain
import os
class MainClassFleetX(QMainWindow, xfleetmain.Ui_FleetX):
    signal = pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.carsbutton.clicked.connect(self.cars)
        self.driversbutton.clicked.connect(self.drivers)
        self.maintenancebutton.clicked.connect(self.maintenance)
        self.reportsbutton.clicked.connect(self.reports)
        self.userbutton.clicked.connect(self.userdetails)
        self.uncertainitiesbutton.clicked.connect(self.uncertainity)
        self.searchbutton.clicked.connect(self.msearch)
        self.driverphoto.pressed.connect(self.getfile)
        self.addcar.pressed(self.addcarfunction)
    def cars(self):
        self.mainstackedwidget.setCurrentIndex(0)
    def drivers(self):
        self.mainstackedwidget.setCurrentIndex(1)
    def uncertainity(self):
        self.mainstackedwidget.setCurrentIndex(3)
    def reports(self):
        self.mainstackedwidget.setCurrentIndex(6)
    def maintenance(self):
        self.mainstackedwidget.setCurrentIndex(4)
    def userdetails(self):
        self.mainstackedwidget.setCurrentIndex(5)
    def msearch(self):
        self.mainstackedwidget.setCurrentIndex(2)
    
        
    def menuofcars(self):
        if self.All_Cars.triggered():
            self.cars()
            self.carswidget.setCurrentIndex(0)
        elif self.Deploy_Cars.triggered():
            self.cars()
            self.carswidget.setCurrentIndex(1)
        elif self.Edit_Car_Details.triggered():
            self.cars()
            self.carswidget.setCurrentIndex(2)
        elif self.Add_Car.triggered():
            self.cars()
            self.carswidget.setCurrentIndex(3)
    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif, *.png)")
        self.le.setPixmap(QPixmap(fname))
		
    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        filenames = QStringList()
		
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
			
            with f:
                data = f.read()
                self.contents.setText(data)
                
	def addcarfunction(self):
        self.licensenumber = self.licensenumber.text()
        self.carmodel = self.carmodel.text()
        self.manudate = self.manudate.date()
        self.fuel_type = self.fuel_type.currentText()
        self.initial_mileage = int(self.initial_mileage.text())
        self.carmake = self.carmake.text()
        self.cartype = self.cartype.text()
        self.chasisnumber = self.chasisnumber.text()
        self.carcolor = self.carcolor.text()
        self.insurancecompany = self.insurancecompany.text()
        self.subscriptiondate = self.subscriptiondate.date()
        self.expirydate = self.expirydate.date()
        print(self.expirydate)

if __name__=="__main__":
    myapp = QApplication(sys.argv)
    ourapp = MainClassFleetX()
    ourapp.show()
    myapp.exec_()