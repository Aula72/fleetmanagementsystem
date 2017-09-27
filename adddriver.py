# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adddriver.ui'
#
# Created: Mon Sep 18 01:23:24 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_drive(object):
    def setupUi(self, add_drive):
        add_drive.setObjectName("add_drive")
        add_drive.resize(374, 526)
        add_drive.setStyleSheet("QLabel{\n"
"font-size:15px;\n"
"}\n"
"QLineEdit{\n"
"font-size:15px; \n"
"}\n"
"QPushButton{\n"
"font-size:15px;\n"
"}\n"
"QDateEdit{\n"
"font-size:15px;\n"
"}\n"
"QComboBox{\n"
"font-size:15px;\n"
"}")
        self.label = QtWidgets.QLabel(add_drive)
        self.label.setGeometry(QtCore.QRect(160, 0, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(add_drive)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(add_drive)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(add_drive)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(add_drive)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(add_drive)
        self.label_6.setGeometry(QtCore.QRect(20, 330, 151, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(add_drive)
        self.label_7.setGeometry(QtCore.QRect(20, 370, 131, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(add_drive)
        self.label_8.setGeometry(QtCore.QRect(20, 240, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(add_drive)
        self.label_9.setGeometry(QtCore.QRect(20, 200, 121, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(add_drive)
        self.label_10.setGeometry(QtCore.QRect(20, 280, 151, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(add_drive)
        self.label_11.setGeometry(QtCore.QRect(20, 410, 141, 31))
        self.label_11.setObjectName("label_11")
        self.male = QtWidgets.QCheckBox(add_drive)
        self.male.setGeometry(QtCore.QRect(170, 280, 70, 17))
        self.male.setObjectName("male")
        self.female = QtWidgets.QCheckBox(add_drive)
        self.female.setGeometry(QtCore.QRect(270, 280, 70, 17))
        self.female.setObjectName("female")
        self.pushButton = QtWidgets.QPushButton(add_drive)
        self.pushButton.setGeometry(QtCore.QRect(120, 480, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.fnamedrive = QtWidgets.QLineEdit(add_drive)
        self.fnamedrive.setGeometry(QtCore.QRect(150, 40, 201, 31))
        self.fnamedrive.setObjectName("fnamedrive")
        self.lnamedrive = QtWidgets.QLineEdit(add_drive)
        self.lnamedrive.setGeometry(QtCore.QRect(150, 80, 201, 31))
        self.lnamedrive.setObjectName("lnamedrive")
        self.permitnumber = QtWidgets.QLineEdit(add_drive)
        self.permitnumber.setGeometry(QtCore.QRect(140, 330, 201, 31))
        self.permitnumber.setObjectName("permitnumber")
        self.drivephoto = QtWidgets.QLineEdit(add_drive)
        self.drivephoto.setGeometry(QtCore.QRect(140, 410, 201, 31))
        self.drivephoto.setObjectName("drivephoto")
        self.permitclass = QtWidgets.QLineEdit(add_drive)
        self.permitclass.setGeometry(QtCore.QRect(140, 370, 201, 31))
        self.permitclass.setObjectName("permitclass")
        self.phonedrive = QtWidgets.QLineEdit(add_drive)
        self.phonedrive.setGeometry(QtCore.QRect(150, 120, 201, 31))
        self.phonedrive.setObjectName("phonedrive")
        self.emaildriver = QtWidgets.QLineEdit(add_drive)
        self.emaildriver.setGeometry(QtCore.QRect(150, 160, 201, 31))
        self.emaildriver.setObjectName("emaildriver")
        self.addressdrive = QtWidgets.QLineEdit(add_drive)
        self.addressdrive.setGeometry(QtCore.QRect(150, 200, 201, 31))
        self.addressdrive.setObjectName("addressdrive")
        self.birthdate = QtWidgets.QDateEdit(add_drive)
        self.birthdate.setGeometry(QtCore.QRect(150, 241, 181, 31))
        self.birthdate.setObjectName("birthdate")

        self.retranslateUi(add_drive)
        QtCore.QMetaObject.connectSlotsByName(add_drive)
        add_drive.setTabOrder(self.fnamedrive, self.lnamedrive)
        add_drive.setTabOrder(self.lnamedrive, self.phonedrive)
        add_drive.setTabOrder(self.phonedrive, self.emaildriver)
        add_drive.setTabOrder(self.emaildriver, self.addressdrive)
        add_drive.setTabOrder(self.addressdrive, self.birthdate)
        add_drive.setTabOrder(self.birthdate, self.male)
        add_drive.setTabOrder(self.male, self.female)
        add_drive.setTabOrder(self.female, self.permitnumber)
        add_drive.setTabOrder(self.permitnumber, self.permitclass)
        add_drive.setTabOrder(self.permitclass, self.drivephoto)
        add_drive.setTabOrder(self.drivephoto, self.pushButton)

    def retranslateUi(self, add_drive):
        _translate = QtCore.QCoreApplication.translate
        add_drive.setWindowTitle(_translate("add_drive", "Add Drive"))
        self.label.setText(_translate("add_drive", "Add Car"))
        self.label_2.setText(_translate("add_drive", "First Name"))
        self.label_3.setText(_translate("add_drive", "Last Name"))
        self.label_4.setText(_translate("add_drive", "Phone Number"))
        self.label_5.setText(_translate("add_drive", "Email Address"))
        self.label_6.setText(_translate("add_drive", "Permit Number"))
        self.label_7.setText(_translate("add_drive", "Permit Class"))
        self.label_8.setText(_translate("add_drive", "Date of Birth"))
        self.label_9.setText(_translate("add_drive", "Address"))
        self.label_10.setText(_translate("add_drive", "Gender"))
        self.label_11.setText(_translate("add_drive", "Photo"))
        self.male.setText(_translate("add_drive", "Male"))
        self.female.setText(_translate("add_drive", "Female"))
        self.pushButton.setText(_translate("add_drive", "Add Driver"))

