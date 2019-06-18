# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScreenCapForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_screenCapForm(object):
    def setupUi(self, screenCapForm):
        screenCapForm.setObjectName("screenCapForm")
        screenCapForm.setEnabled(True)
        screenCapForm.resize(400, 300)
        screenCapForm.setWindowTitle("")
        self.gv_fullscreen = QtWidgets.QGraphicsView(screenCapForm)
        self.gv_fullscreen.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.gv_fullscreen.setObjectName("gv_fullscreen")
        self.l_rec = QtWidgets.QLabel(screenCapForm)
        self.l_rec.setGeometry(QtCore.QRect(0, 0, 72, 15))
        self.l_rec.setText("")
        self.l_rec.setObjectName("l_rec")

        self.retranslateUi(screenCapForm)
        QtCore.QMetaObject.connectSlotsByName(screenCapForm)

    def retranslateUi(self, screenCapForm):
        pass

