# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deploycar.ui'
#
# Created: Tue Sep 26 18:34:44 2017
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deploycar(object):
    def setupUi(self, deploycar):
        deploycar.setObjectName("deploycar")
        deploycar.resize(392, 278)
        deploycar.setFocusPolicy(QtCore.Qt.StrongFocus)
        deploycar.setStyleSheet("QLabel{\n"
"font-size:15px;\n"
"}\n"
"QLineEdit{\n"
"font-size:15px; \n"
"}\n"
"QPushButton{\n"
"font-size:15px;\n"
"}")
        deploycar.setModal(False)
        self.gridLayout_5 = QtWidgets.QGridLayout(deploycar)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(deploycar)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_5.addWidget(self.frame_3, 0, 1, 1, 2)
        self.frame = QtWidgets.QFrame(deploycar)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(deploycar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fuelcardnumber = QtWidgets.QLineEdit(self.frame_2)
        self.fuelcardnumber.setObjectName("fuelcardnumber")
        self.gridLayout_2.addWidget(self.fuelcardnumber, 4, 0, 1, 1)
        self.licensenumber = QtWidgets.QLineEdit(self.frame_2)
        self.licensenumber.setObjectName("licensenumber")
        self.gridLayout_2.addWidget(self.licensenumber, 0, 0, 1, 1)
        self.original = QtWidgets.QLineEdit(self.frame_2)
        self.original.setObjectName("original")
        self.gridLayout_2.addWidget(self.original, 3, 0, 1, 1)
        self.orign = QtWidgets.QLineEdit(self.frame_2)
        self.orign.setObjectName("orign")
        self.gridLayout_2.addWidget(self.orign, 2, 0, 1, 1)
        self.driverid = QtWidgets.QLineEdit(self.frame_2)
        self.driverid.setObjectName("driverid")
        self.gridLayout_2.addWidget(self.driverid, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 1, 2, 1, 2)
        self.frame_5 = QtWidgets.QFrame(deploycar)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(deploycar)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.deploycarbutton = QtWidgets.QPushButton(self.frame_4)
        self.deploycarbutton.setObjectName("deploycarbutton")
        self.gridLayout_4.addWidget(self.deploycarbutton, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 2, 1, 1, 2)
        self.frame_6 = QtWidgets.QFrame(deploycar)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_5.addWidget(self.frame_6, 2, 3, 1, 1)
        
        self.retranslateUi(deploycar)
        QtCore.QMetaObject.connectSlotsByName(deploycar)
        deploycar.setTabOrder(self.licensenumber, self.driverid)
        deploycar.setTabOrder(self.driverid, self.orign)
        deploycar.setTabOrder(self.orign, self.original)
        deploycar.setTabOrder(self.original, self.fuelcardnumber)
        deploycar.setTabOrder(self.fuelcardnumber, self.deploycarbutton)

    def retranslateUi(self, deploycar):
        _translate = QtCore.QCoreApplication.translate
        deploycar.setWindowTitle(_translate("deploycar", "Deploy Car"))
        self.label.setText(_translate("deploycar", "DEPLOY CAR"))
        self.label_2.setText(_translate("deploycar", "Car Number"))
        self.label_3.setText(_translate("deploycar", "Drive Number"))
        self.label_4.setText(_translate("deploycar", "Origin"))
        self.label_6.setText(_translate("deploycar", "Destination"))
        self.label_5.setText(_translate("deploycar", "Fuel Card Number"))
        self.deploycarbutton.setText(_translate("deploycar", "Deploy Car"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deploycar = QtWidgets.QDialog()
    ui = Ui_deploycar()
    ui.setupUi(deploycar)
    deploycar.show()
    sys.exit(app.exec_())

