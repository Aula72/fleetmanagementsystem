# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editcar.ui'
#
# Created: Sun Sep 17 19:14:17 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editdriver_2(object):
    def setupUi(self, editdriver_2):
        editdriver_2.setObjectName("editdriver_2")
        editdriver_2.resize(400, 454)
        self.addresschange = QtWidgets.QLineEdit(editdriver_2)
        self.addresschange.setGeometry(QtCore.QRect(160, 230, 201, 31))
        self.addresschange.setObjectName("addresschange")
        self.label_6 = QtWidgets.QLabel(editdriver_2)
        self.label_6.setGeometry(QtCore.QRect(30, 270, 151, 31))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(editdriver_2)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.snamechange = QtWidgets.QLineEdit(editdriver_2)
        self.snamechange.setGeometry(QtCore.QRect(160, 110, 201, 31))
        self.snamechange.setObjectName("snamechange")
        self.label = QtWidgets.QLabel(editdriver_2)
        self.label.setGeometry(QtCore.QRect(170, 30, 131, 31))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(editdriver_2)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(editdriver_2)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(editdriver_2)
        self.label_9.setGeometry(QtCore.QRect(30, 230, 121, 31))
        self.label_9.setObjectName("label_9")
        self.permitchange = QtWidgets.QLineEdit(editdriver_2)
        self.permitchange.setGeometry(QtCore.QRect(160, 270, 201, 31))
        self.permitchange.setObjectName("permitchange")
        self.pnumberchange = QtWidgets.QLineEdit(editdriver_2)
        self.pnumberchange.setGeometry(QtCore.QRect(160, 150, 201, 31))
        self.pnumberchange.setObjectName("pnumberchange")
        self.emailchange = QtWidgets.QLineEdit(editdriver_2)
        self.emailchange.setGeometry(QtCore.QRect(160, 190, 201, 31))
        self.emailchange.setObjectName("emailchange")
        self.label_11 = QtWidgets.QLabel(editdriver_2)
        self.label_11.setGeometry(QtCore.QRect(30, 350, 141, 31))
        self.label_11.setObjectName("label_11")
        self.label_4 = QtWidgets.QLabel(editdriver_2)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 121, 21))
        self.label_4.setObjectName("label_4")
        self.classchange = QtWidgets.QLineEdit(editdriver_2)
        self.classchange.setGeometry(QtCore.QRect(160, 310, 201, 31))
        self.classchange.setObjectName("classchange")
        self.fnamechange = QtWidgets.QLineEdit(editdriver_2)
        self.fnamechange.setGeometry(QtCore.QRect(160, 70, 201, 31))
        self.fnamechange.setObjectName("fnamechange")
        self.label_7 = QtWidgets.QLabel(editdriver_2)
        self.label_7.setGeometry(QtCore.QRect(30, 310, 131, 31))
        self.label_7.setObjectName("label_7")
        self.editdriver = QtWidgets.QPushButton(editdriver_2)
        self.editdriver.setGeometry(QtCore.QRect(120, 400, 131, 31))
        self.editdriver.setObjectName("editdriver")
        self.photochange = QtWidgets.QLineEdit(editdriver_2)
        self.photochange.setGeometry(QtCore.QRect(160, 350, 201, 31))
        self.photochange.setObjectName("photochange")

        self.retranslateUi(editdriver_2)
        QtCore.QMetaObject.connectSlotsByName(editdriver_2)

    def retranslateUi(self, editdriver_2):
        _translate = QtCore.QCoreApplication.translate
        editdriver_2.setWindowTitle(_translate("editdriver_2", "Edit Car"))
        self.label_6.setText(_translate("editdriver_2", "Permit Number"))
        self.label_2.setText(_translate("editdriver_2", "First Name"))
        self.label.setText(_translate("editdriver_2", "Edit Driver"))
        self.label_5.setText(_translate("editdriver_2", "Email Address"))
        self.label_3.setText(_translate("editdriver_2", "Last Name"))
        self.label_9.setText(_translate("editdriver_2", "Address"))
        self.label_11.setText(_translate("editdriver_2", "Photo"))
        self.label_4.setText(_translate("editdriver_2", "Phone Number"))
        self.label_7.setText(_translate("editdriver_2", "Permit Class"))
        self.editdriver.setText(_translate("editdriver_2", "Edit Driver"))

