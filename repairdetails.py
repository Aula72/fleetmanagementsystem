# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repairdetails.ui'
#
# Created: Sun Sep 17 19:13:15 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_repaircar(object):
    def setupUi(self, repaircar):
        repaircar.setObjectName("repaircar")
        repaircar.resize(373, 484)
        repaircar.setStyleSheet("QLabel{\n"
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
        self.label = QtWidgets.QLabel(repaircar)
        self.label.setGeometry(QtCore.QRect(95, 20, 131, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(repaircar)
        self.label_2.setGeometry(QtCore.QRect(20, 55, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(repaircar)
        self.label_3.setGeometry(QtCore.QRect(20, 400, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(repaircar)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(repaircar)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(repaircar)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(repaircar)
        self.label_9.setGeometry(QtCore.QRect(20, 320, 141, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(repaircar)
        self.label_10.setGeometry(QtCore.QRect(20, 250, 141, 31))
        self.label_10.setObjectName("label_10")
        self.repairsubmit = QtWidgets.QPushButton(repaircar)
        self.repairsubmit.setGeometry(QtCore.QRect(110, 440, 131, 31))
        self.repairsubmit.setObjectName("repairsubmit")
        self.numcar = QtWidgets.QLineEdit(repaircar)
        self.numcar.setGeometry(QtCore.QRect(180, 50, 171, 31))
        self.numcar.setObjectName("numcar")
        self.numdrive = QtWidgets.QLineEdit(repaircar)
        self.numdrive.setGeometry(QtCore.QRect(180, 90, 171, 31))
        self.numdrive.setObjectName("numdrive")
        self.invoiceimage = QtWidgets.QLineEdit(repaircar)
        self.invoiceimage.setGeometry(QtCore.QRect(180, 400, 171, 31))
        self.invoiceimage.setObjectName("invoiceimage")
        self.repairtype = QtWidgets.QLineEdit(repaircar)
        self.repairtype.setGeometry(QtCore.QRect(180, 130, 171, 31))
        self.repairtype.setObjectName("repairtype")
        self.repairdescription = QtWidgets.QTextEdit(repaircar)
        self.repairdescription.setGeometry(QtCore.QRect(180, 290, 171, 101))
        self.repairdescription.setObjectName("repairdescription")
        self.partsrepair = QtWidgets.QTextEdit(repaircar)
        self.partsrepair.setGeometry(QtCore.QRect(180, 170, 171, 71))
        self.partsrepair.setObjectName("partsrepair")
        self.daterepair = QtWidgets.QDateEdit(repaircar)
        self.daterepair.setGeometry(QtCore.QRect(180, 250, 171, 31))
        self.daterepair.setObjectName("daterepair")

        self.retranslateUi(repaircar)
        QtCore.QMetaObject.connectSlotsByName(repaircar)

    def retranslateUi(self, repaircar):
        _translate = QtCore.QCoreApplication.translate
        repaircar.setWindowTitle(_translate("repaircar", "Repair Car Details"))
        self.label.setText(_translate("repaircar", "Enter repair details"))
        self.label_2.setText(_translate("repaircar", "Car licence plate number"))
        self.label_3.setText(_translate("repaircar", "Invoice Image"))
        self.label_6.setText(_translate("repaircar", "Driver Number"))
        self.label_7.setText(_translate("repaircar", "Repair Type"))
        self.label_8.setText(_translate("repaircar", "Parts Repair"))
        self.label_9.setText(_translate("repaircar", "Repair Description"))
        self.label_10.setText(_translate("repaircar", "Date of Repair"))
        self.repairsubmit.setText(_translate("repaircar", "Submit Details"))

