# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordaccident.ui'
#
# Created: Mon Sep 18 00:40:57 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_accidentevent(object):
    def setupUi(self, accidentevent):
        accidentevent.setObjectName("accidentevent")
        accidentevent.resize(400, 351)
        accidentevent.setStyleSheet("QLabel{\n"
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
"}\n"
"QTextEdit{\n"
"font-color:15px;\n"
"}")
        self.label = QtWidgets.QLabel(accidentevent)
        self.label.setGeometry(QtCore.QRect(110, 20, 271, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(accidentevent)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 171, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(accidentevent)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(accidentevent)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(accidentevent)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 121, 31))
        self.label_5.setObjectName("label_5")
        self.carid = QtWidgets.QLineEdit(accidentevent)
        self.carid.setGeometry(QtCore.QRect(230, 60, 151, 31))
        self.carid.setObjectName("carid")
        self.driverid = QtWidgets.QLineEdit(accidentevent)
        self.driverid.setGeometry(QtCore.QRect(230, 100, 151, 31))
        self.driverid.setObjectName("driverid")
        self.accdescription = QtWidgets.QTextEdit(accidentevent)
        self.accdescription.setGeometry(QtCore.QRect(190, 220, 201, 71))
        self.accdescription.setObjectName("accdescription")
        self.addaccident = QtWidgets.QPushButton(accidentevent)
        self.addaccident.setGeometry(QtCore.QRect(120, 300, 161, 31))
        self.addaccident.setObjectName("addaccident")
        self.comboBox = QtWidgets.QComboBox(accidentevent)
        self.comboBox.setGeometry(QtCore.QRect(230, 140, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(accidentevent)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 161, 31))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(accidentevent)
        self.dateEdit.setGeometry(QtCore.QRect(230, 180, 161, 31))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(accidentevent)
        QtCore.QMetaObject.connectSlotsByName(accidentevent)

    def retranslateUi(self, accidentevent):
        _translate = QtCore.QCoreApplication.translate
        accidentevent.setWindowTitle(_translate("accidentevent", "Record Accident"))
        self.label.setText(_translate("accidentevent", "Add accident event"))
        self.label_2.setText(_translate("accidentevent", "Car Licence Plate Number"))
        self.label_3.setText(_translate("accidentevent", "Drive ID"))
        self.label_4.setText(_translate("accidentevent", "Type"))
        self.label_5.setText(_translate("accidentevent", "Brief description"))
        self.addaccident.setText(_translate("accidentevent", "Add Event"))
        self.comboBox.setItemText(0, _translate("accidentevent", "Fatal"))
        self.comboBox.setItemText(1, _translate("accidentevent", "Non Fatal"))
        self.label_6.setText(_translate("accidentevent", "Event Time"))

