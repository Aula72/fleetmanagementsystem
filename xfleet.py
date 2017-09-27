from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import xfleetmain #, deploycar, alldialog
import os
import shutil, time

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
        self.logoutbutton.clicked.connect(self.loginpage)
        self.driverphoto.pressed.connect(self.getfile)
        self.addcar.pressed.connect(self.addcarfunction)
        self.adddriverbutton.pressed.connect(self.driveraddfunction)
        self.addaccident.pressed.connect(self.addaccidenteventfunction)
        self.viewpreviousmaintenance.clicked.connect(self.viewpreviousmaintenancefunction)
        self.loginbutton.clicked.connect(self.firstpage)
        #self.userbutton.clicked.connect(self.deploycarshow)
        self.trayicon = QIcon("icons/app-icon.png")
        self.objectrayicon = QSystemTrayIcon(self.trayicon, self)
        self.traymenu = QMenu()
        self.xclose = QAction("Close", self)
        self.xlogout = QAction("Logout", self)
        self.traymenu.addActions([self.xlogout,self.xclose])
        self.objectrayicon.setContextMenu(self.traymenu)
        self.xclose.triggered.connect(self.close)
        self.objectrayicon.show()
        self.usernamedisplay.setText("Aula")

    #deploycar is tab 7
    #driver details tab 8
    def firstpage(self):
        self.loginstackedwidget.setCurrentIndex(2)
        self.cars()
        self.carswidget.setCurrentIndex(0)
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
    def cardeploy(self):
        self.mainstackedwidget.setCurrentIndex(7)
    def driverdetails(self):
        self.mainstackedwidget.setCurrentIndex(8)
    def loginpage(self):
        self.loginstackedwidget.setCurrentIndex(0)
    def addcarfunction(self):
        self.license_number = self.licensenumber.text()
        self.car_model = self.carmodel.text()
        self.manu_date = self.manudate.date()
        self.fueltype = self.fuel_type.currentText()
        self.initialmileage = int(self.initial_mileage.text())
        self.car_make = self.carmake.text()
        self.car_type = self.cartype.text()
        self.chasis_number = self.chasisnumber.text()
        self.car_color = self.carcolor.text()
        self.insurance_company = self.insurancecompany.text()
        self.subscription_date = self.subscriptiondate.date()
        self.expiry_date = self.expirydate.date()
        
        try: 
            print(self.initialmileage)  
        except:

            print("heutfh")
        print(self.expiry_date) 
        print(self.fueltype)
    def driveraddfunction(self):
        self.firstnamedrive = self.fnamedrive.text()
        self.secondnamedrive = self.lnamedrive.text()
        self.phone = int(self.phonedrive.text()) 
        self.address = self.addressdrive.text()
        self.gender = self.drivergenda.currentText()
        self.email = self.emaildriver.text()
        self.dob = self.birthdate.date()
        self.permit_number = self.permitnumber.text()
        self.permit_class = self.permitclass.text()
        print(self.gender)
    def addaccidenteventfunction(self):
        self.carregnumber = self.caraccnumber.text()
        self.acclocation = self.accidentlocation.text()
        self.acctime = self.accidentdate.date()
        self.caracc = self.carstatus.currentText()
        self.accdriver = int(self.driverid.text())
        self.acctype = self.accidenttype.currentText()
        self.accpassengerstatus = self.passengerstatus.currentText()
        self.accdriverstatus = self.driverstatus.currentText()
        self.accdescption = self.briefdescription.toPlainText()
        self.accresolution = self.resolution.toPlainText()
        print(self.accdescption)
    def viewpreviousmaintenancefunction(self):
        self.newitem = self.viewpreviousmaintenance.rowCount()
        self.viewpreviousmaintenance.insertRow(self.newitem)
        self.r1 = QTableWidgetItem("Aula")
        self.r2 =QTableWidgetItem("simon")
        self.r3 = QTableWidgetItem(45)
        self.r4 = QTableWidgetItem(90)
        #self.viewpreviousmaintenance.selectedItems(self.r1, self.r2, self.r3,self.r4)
        self.viewpreviousmaintenance.setItem(self.newitem,0,self.r1)
        self.viewpreviousmaintenance.setItem(self.newitem,1,self.r2)
        self.viewpreviousmaintenance.setItem(self.newitem,2,self.r3)
        self.viewpreviousmaintenance.setItem(self.newitem,3,self.r4)
    def getfile(self):        
        self.fname = QFileDialog()
        self.upl=self.fname.getOpenFileName(self, 'Open File',"c\\","Image Files (*.gif *.jpg *.png)")
        print(self.upl)
        print(os.getcwd())
        #print(os.path.dirname(os.path.realpath(self.upl)))
        #print(os.path.mv(self.upl))
        '''
        self.destpath = 'D:\\FLEET\\fleetmanagement\\aula\\'
        #self.saveto = (self.destpath,os.path.dirname(self.upl))
        #self.saveto = os.path.join(self.destpath,os.path.dirname(self.upl))
        
        os.makedirs(self.saveto)
        shutil.copy(self.upl, self.destpath)
        assert not os.path.abspath(self.upl)
        
        #self.srcfile = 
        '''
        #self.n = os.ctermid(self.saveto)
        #print(self.n)
        #shutil.move(self.saveto, self.destpath)
    def getfiles(self):
        self.dlg = QFileDialog()
        self.dlg.setFileMode(QFileDialog.AnyFile)
        self.dlg.setFilter("Images (*.png *.jpg *.gif)")
        self.filenames = QStringList()
        if self.dlg.exec_():
            self.filenames=self.dlg.selectedFiles()
            self.f=open(filenames[0],'r')
            with self.f:
                self.data = self.f.read()
    
    
    def savephoto(self):
        pass
    def pictures(self):
        os.mkdir("./aula")

if __name__=="__main__":
    #MainClassFleetX.pictures(None)
    myapp = QApplication(sys.argv)
    ourapp = MainClassFleetX()
    oursplash_image=QPixmap("icons/app-icon.png")
    splash = QSplashScreen(oursplash_image)    
    splash.show()
    time.sleep(5)
    ourapp.show()
    splash.finish(ourapp)
    myapp.exec_()