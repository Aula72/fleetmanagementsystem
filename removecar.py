# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removecar.ui'
#
# Created: Mon Sep 18 15:44:30 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_removecar(object):
    def setupUi(self, removecar):
        removecar.setObjectName("removecar")
        removecar.resize(384, 151)
        removecar.setStyleSheet("QLabel{\n"
"font-size:15px;\n"
"}\n"
"QPushButton{\n"
"font-size:15px;\n"
"}\n"
"QLineEdit{\n"
"font-size:15px;\n"
"}")
        self.frame = QtWidgets.QFrame(removecar)
        self.frame.setGeometry(QtCore.QRect(10, 10, 361, 134))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 45, 141, 21))
        self.label_2.setObjectName("label_2")
        self.removecarremove = QtWidgets.QPushButton(self.frame)
        self.removecarremove.setGeometry(QtCore.QRect(100, 90, 75, 31))
        self.removecarremove.setObjectName("removecarremove")
        self.removecarclose = QtWidgets.QPushButton(self.frame)
        self.removecarclose.setGeometry(QtCore.QRect(220, 90, 81, 31))
        self.removecarclose.setObjectName("removecarclose")
        self.removecarid = QtWidgets.QLineEdit(self.frame)
        self.removecarid.setGeometry(QtCore.QRect(160, 40, 171, 31))
        self.removecarid.setObjectName("removecarid")

        self.retranslateUi(removecar)
        QtCore.QMetaObject.connectSlotsByName(removecar)

    def retranslateUi(self, removecar):
        _translate = QtCore.QCoreApplication.translate
        removecar.setWindowTitle(_translate("removecar", "Remove Car"))
        self.label.setText(_translate("removecar", "Remove Car"))
        self.label_2.setText(_translate("removecar", "Car Licence Number"))
        self.removecarremove.setText(_translate("removecar", "Remove"))
        self.removecarclose.setText(_translate("removecar", "Close"))

