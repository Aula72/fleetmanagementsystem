# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuelservice.ui'
#
# Created: Mon Sep 18 00:26:26 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fueldetails(object):
    def setupUi(self, fueldetails):
        fueldetails.setObjectName("fueldetails")
        fueldetails.resize(365, 212)
        fueldetails.setStyleSheet("QLabel{\n"
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
        self.label = QtWidgets.QLabel(fueldetails)
        self.label.setGeometry(QtCore.QRect(110, 10, 171, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(fueldetails)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(fueldetails)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(fueldetails)
        self.label_4.setGeometry(QtCore.QRect(20, 125, 141, 21))
        self.label_4.setObjectName("label_4")
        self.fuelnumber = QtWidgets.QLineEdit(fueldetails)
        self.fuelnumber.setGeometry(QtCore.QRect(160, 40, 181, 31))
        self.fuelnumber.setObjectName("fuelnumber")
        self.drivernumber = QtWidgets.QLineEdit(fueldetails)
        self.drivernumber.setGeometry(QtCore.QRect(160, 80, 181, 31))
        self.drivernumber.setObjectName("drivernumber")
        self.carnumber = QtWidgets.QLineEdit(fueldetails)
        self.carnumber.setGeometry(QtCore.QRect(160, 120, 181, 31))
        self.carnumber.setObjectName("carnumber")
        self.givefuel = QtWidgets.QPushButton(fueldetails)
        self.givefuel.setGeometry(QtCore.QRect(120, 170, 131, 31))
        self.givefuel.setObjectName("givefuel")

        self.retranslateUi(fueldetails)
        QtCore.QMetaObject.connectSlotsByName(fueldetails)

    def retranslateUi(self, fueldetails):
        _translate = QtCore.QCoreApplication.translate
        fueldetails.setWindowTitle(_translate("fueldetails", "Fuel Service"))
        self.label.setText(_translate("fueldetails", "Fueling Service"))
        self.label_2.setText(_translate("fueldetails", "Fuel Card Number"))
        self.label_3.setText(_translate("fueldetails", "Driver Number"))
        self.label_4.setText(_translate("fueldetails", "Car Licence Number"))
        self.givefuel.setText(_translate("fueldetails", "Submit Details"))

