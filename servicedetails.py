# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servicedetails.ui'
#
# Created: Mon Sep 18 00:50:42 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_servicedetails(object):
    def setupUi(self, servicedetails):
        servicedetails.setObjectName("servicedetails")
        servicedetails.resize(400, 500)
        servicedetails.setStyleSheet("QLabel{\n"
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
        self.label_6 = QtWidgets.QLabel(servicedetails)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.label_6.setObjectName("label_6")
        self.submitservice = QtWidgets.QPushButton(servicedetails)
        self.submitservice.setGeometry(QtCore.QRect(130, 450, 131, 31))
        self.submitservice.setObjectName("submitservice")
        self.servicetype = QtWidgets.QLineEdit(servicedetails)
        self.servicetype.setGeometry(QtCore.QRect(200, 130, 181, 31))
        self.servicetype.setObjectName("servicetype")
        self.label_3 = QtWidgets.QLabel(servicedetails)
        self.label_3.setGeometry(QtCore.QRect(20, 400, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(servicedetails)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(servicedetails)
        self.label_10.setGeometry(QtCore.QRect(20, 250, 141, 31))
        self.label_10.setObjectName("label_10")
        self.dateservice = QtWidgets.QDateEdit(servicedetails)
        self.dateservice.setGeometry(QtCore.QRect(200, 250, 181, 31))
        self.dateservice.setObjectName("dateservice")
        self.label_7 = QtWidgets.QLabel(servicedetails)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(servicedetails)
        self.label_9.setGeometry(QtCore.QRect(20, 320, 141, 31))
        self.label_9.setObjectName("label_9")
        self.numcarserv = QtWidgets.QLineEdit(servicedetails)
        self.numcarserv.setGeometry(QtCore.QRect(200, 50, 181, 31))
        self.numcarserv.setObjectName("numcarserv")
        self.label_2 = QtWidgets.QLabel(servicedetails)
        self.label_2.setGeometry(QtCore.QRect(20, 55, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(servicedetails)
        self.label.setGeometry(QtCore.QRect(95, 20, 131, 20))
        self.label.setObjectName("label")
        self.drivernumserv = QtWidgets.QLineEdit(servicedetails)
        self.drivernumserv.setGeometry(QtCore.QRect(200, 90, 181, 31))
        self.drivernumserv.setObjectName("drivernumserv")
        self.serviceinvoice = QtWidgets.QLineEdit(servicedetails)
        self.serviceinvoice.setGeometry(QtCore.QRect(200, 410, 181, 31))
        self.serviceinvoice.setObjectName("serviceinvoice")
        self.servicedescription = QtWidgets.QTextEdit(servicedetails)
        self.servicedescription.setGeometry(QtCore.QRect(200, 290, 181, 101))
        self.servicedescription.setObjectName("servicedescription")
        self.partsservice = QtWidgets.QTextEdit(servicedetails)
        self.partsservice.setGeometry(QtCore.QRect(200, 170, 181, 71))
        self.partsservice.setObjectName("partsservice")

        self.retranslateUi(servicedetails)
        QtCore.QMetaObject.connectSlotsByName(servicedetails)

    def retranslateUi(self, servicedetails):
        _translate = QtCore.QCoreApplication.translate
        servicedetails.setWindowTitle(_translate("servicedetails", "Service Details"))
        self.label_6.setText(_translate("servicedetails", "Driver Number"))
        self.submitservice.setText(_translate("servicedetails", "Submit Details"))
        self.label_3.setText(_translate("servicedetails", "Invoice Image"))
        self.label_8.setText(_translate("servicedetails", "Parts affectes"))
        self.label_10.setText(_translate("servicedetails", "Date of Service"))
        self.label_7.setText(_translate("servicedetails", "Service Type"))
        self.label_9.setText(_translate("servicedetails", "Service Description"))
        self.label_2.setText(_translate("servicedetails", "Car licence plate number"))
        self.label.setText(_translate("servicedetails", "Enter repair details"))

