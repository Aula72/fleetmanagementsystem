from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import uimain
import os
import shutil, time


class MainClassFleetX(QMainWindow, uimain.Ui_FleetX):
    signal = pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.carsbutton.clicked.connect(self.cars)
        self.driversbutton.clicked.connect(self.drivers)
        self.maintenancebutton.clicked.connect(self.maintenance)
        self.reportsbutton.clicked.connect(self.reports)
        #self.userbutton.clicked.connect(self.userdetails)
        self.uncertainitiesbutton.clicked.connect(self.uncertainity)
        self.searchbutton.clicked.connect(self.msearch)
        self.logoutbutton.clicked.connect(self.loginpage)
        self.driverphoto.pressed.connect(self.driverpics)
        self.rightimagebutton.pressed.connect(self.rightpics)
        self.leftimagebutton.pressed.connect(self.leftpics)
        self.behindimagebutton.pressed.connect(self.behindpics)
        #self.driverphoto.pressed.connect(self.driverpics)
        self.addcar.pressed.connect(self.addcarfunction)
        self.newdriverbutton.pressed.connect(self.driveraddfunction)
        self.addaccident.pressed.connect(self.addaccidenteventfunction)
        self.viewpreviousmaintenance.clicked.connect(self.viewpreviousmaintenancefunction)
        self.loginbutton.clicked.connect(self.firstpage)    
        self.trayicon = QIcon("icons/app-icon.png")
        self.objectrayicon = QSystemTrayIcon(self.trayicon, self)
        self.traymenu = QMenu()
        self.xclose = QAction("Close", self)
        self.xlogout = QAction("Logout", self)
        self.traymenu.addActions([self.xlogout,self.xclose])
        self.objectrayicon.setContextMenu(self.traymenu)
        self.xclose.triggered.connect(self.close)
        self.xlogout.triggered.connect(self.loginpage)
        self.objectrayicon.show()
        self.usernamedisplay.setText("Aula")
        self.frontimagebutton.clicked.connect(self.getfile)
        #self.backtocars.clicked.connect(self.cars)
        
    
    def deploying(self):
        self.mainstackedwidget.setCurrentIndex(7)

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
        
        
        
    def driveraddfunction(self):
        self.firstnamedrive = self.fnamedrive.text()
        self.secondnamedrive = self.lnamedrive.text()
        self.phone = int(self.phonedrive.text()) 
        self.address = self.addressdrive.text()
        self.gender = self.drivergenda.currentText()
        self.email = self.emaildriver.text()
        self.dob = self.birthdate.date()
        self.permit_number = self.permitnumber.text()
        self.permit_class = self.permitclass.currentText()
        #self.driverpics()
        #print(self.gender)
        
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
        self.upl=self.fname.getOpenFileName(self, 'Open File',"c:\\","Image Files (*.gif *.jpg *.png)")
         
   
    def copyFile(self, src, dest):
        try:
            shutil.copy(src, dest)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)
    def renamefile(self):
        self.realname = os.path.basename(os.path.splitext(self.upl)[0])
        self.newname = self.realname + "1234"
    def driverpics(self):
        self.getfile()
        self.drivepath = ".\\allpics\\drivers\\"
        self.drivephoto.setText(self.upl[0])
        shutil.copy(self.upl[0], self.drivepath)
        #.replace(os.path.basename(os.path.splitext(self.upl[0])[0]),'1')
    def frontpics(self):
        self.getfile()
        self.frontpath = ".\\allpics\\front\\"
        self.frontimage.setText(self.upl[0])
        shutil.copy(self.upl[0], self.frontpath)
        #.replace(os.path.basename(os.path.splitext(self.upl[0])[0]),'1')
    def leftpics(self):
        self.getfile()
        self.leftpath = ".\\allpics\\left\\"
        self.leftimage.setText(self.upl[0])
        shutil.copy(self.upl[0], self.leftpath)
        #.replace(os.path.basename(os.path.splitext(self.upl[0])[0]),'1')
    def rightpics(self):
        self.getfile()
        self.rightpath = ".\\allpics\\right\\"
        self.rightimage.setText(self.upl[0])
        shutil.copy(self.upl[0], self.rightpath)
        #.replace(os.path.basename(os.path.splitext(self.upl[0])[0]),'1')
    def behindpics(self):
        self.getfile()
        self.drivepath = ".\\allpics\\behind\\"
        self.leftimage.setText(self.upl[0])
        shutil.copy(self.upl[0], self.behindpath)
        #.replace(os.path.basename(os.path.splitext(self.upl[0])[0]),'1')
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