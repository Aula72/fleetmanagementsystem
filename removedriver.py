# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removedriver.ui'
#
# Created: Mon Sep 18 15:45:40 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_removedriver(object):
    def setupUi(self, removedriver):
        removedriver.setObjectName("removedriver")
        removedriver.resize(400, 152)
        removedriver.setStyleSheet("QLabel{\n"
"font-size:15px;\n"
"}\n"
"QPushButton{\n"
"font-size:15px;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(removedriver)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(removedriver)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.removedriveremove = QtWidgets.QPushButton(self.frame)
        self.removedriveremove.setGeometry(QtCore.QRect(100, 90, 75, 31))
        self.removedriveremove.setObjectName("removedriveremove")
        self.removedriveclose = QtWidgets.QPushButton(self.frame)
        self.removedriveclose.setGeometry(QtCore.QRect(220, 90, 81, 31))
        self.removedriveclose.setObjectName("removedriveclose")
        self.removedriveid = QtWidgets.QLineEdit(self.frame)
        self.removedriveid.setGeometry(QtCore.QRect(160, 40, 171, 31))
        self.removedriveid.setObjectName("removedriveid")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(removedriver)
        QtCore.QMetaObject.connectSlotsByName(removedriver)

    def retranslateUi(self, removedriver):
        _translate = QtCore.QCoreApplication.translate
        removedriver.setWindowTitle(_translate("removedriver", "Remove Drive"))
        self.label.setText(_translate("removedriver", "Remove Driver"))
        self.label_2.setText(_translate("removedriver", "Drive ID"))
        self.removedriveremove.setText(_translate("removedriver", "Remove"))
        self.removedriveclose.setText(_translate("removedriver", "Close"))

