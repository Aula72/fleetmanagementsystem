# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otherdeploydriver.ui'
#
# Created: Mon Sep 18 01:03:13 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_otherdeploy(object):
    def setupUi(self, otherdeploy):
        otherdeploy.setObjectName("otherdeploy")
        otherdeploy.resize(379, 275)
        otherdeploy.setAutoFillBackground(True)
        otherdeploy.setStyleSheet("QLabel{\n"
"font-size:15px;\n"
"}\n"
"QLineEdit{\n"
"font-size:15px; \n"
"}\n"
"QPushButton{\n"
"font-size:15px;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(otherdeploy)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(otherdeploy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 141, 31))
        self.label_3.setObjectName("label_3")
        self.otherdriver = QtWidgets.QLineEdit(self.frame)
        self.otherdriver.setGeometry(QtCore.QRect(180, 50, 161, 31))
        self.otherdriver.setObjectName("otherdriver")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 131, 31))
        self.label_4.setObjectName("label_4")
        self.ontherlicence = QtWidgets.QLineEdit(self.frame)
        self.ontherlicence.setGeometry(QtCore.QRect(180, 90, 161, 31))
        self.ontherlicence.setObjectName("ontherlicence")
        self.otherfuel = QtWidgets.QLineEdit(self.frame)
        self.otherfuel.setGeometry(QtCore.QRect(180, 130, 161, 31))
        self.otherfuel.setObjectName("otherfuel")
        self.otherdestination = QtWidgets.QLineEdit(self.frame)
        self.otherdestination.setGeometry(QtCore.QRect(180, 170, 161, 31))
        self.otherdestination.setObjectName("otherdestination")
        self.deployother = QtWidgets.QPushButton(self.frame)
        self.deployother.setGeometry(QtCore.QRect(130, 222, 121, 31))
        self.deployother.setObjectName("deployother")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 121, 16))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(otherdeploy)
        QtCore.QMetaObject.connectSlotsByName(otherdeploy)

    def retranslateUi(self, otherdeploy):
        _translate = QtCore.QCoreApplication.translate
        otherdeploy.setWindowTitle(_translate("otherdeploy", "Deploy Driver"))
        self.label.setText(_translate("otherdeploy", "Driver ID"))
        self.label_2.setText(_translate("otherdeploy", "Car Licence Number"))
        self.label_3.setText(_translate("otherdeploy", "Fuel Car Number"))
        self.label_4.setText(_translate("otherdeploy", "Destination"))
        self.deployother.setText(_translate("otherdeploy", "Deploy"))
        self.label_5.setText(_translate("otherdeploy", "Deploy driver"))

