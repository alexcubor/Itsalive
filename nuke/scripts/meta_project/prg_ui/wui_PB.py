# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bzufarov/Documents/Itsalive/nuke/scripts/meta_project/prg_ui/mt_ui/wui_PB.ui',
# licensing of 'C:/Users/bzufarov/Documents/Itsalive/nuke/scripts/meta_project/prg_ui/mt_ui/wui_PB.ui' applies.
#
# Created: Wed Feb  1 22:34:34 2023
#      by: pyside2-uic  running on PySide2 5.12.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PB(object):
    def setupUi(self, PB):
        PB.setObjectName("PB")
        PB.resize(44, 44)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(PB)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_PB = QtWidgets.QPushButton(PB)
        self.pb_PB.setEnabled(True)
        self.pb_PB.setMinimumSize(QtCore.QSize(40, 40))
        self.pb_PB.setMaximumSize(QtCore.QSize(40, 40))
        self.pb_PB.setAutoFillBackground(False)
        self.pb_PB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/openProj.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_PB.setIcon(icon)
        self.pb_PB.setIconSize(QtCore.QSize(30, 30))
        self.pb_PB.setDefault(False)
        self.pb_PB.setFlat(True)
        self.pb_PB.setObjectName("pb_PB")
        self.horizontalLayout_2.addWidget(self.pb_PB)

        self.retranslateUi(PB)
        QtCore.QMetaObject.connectSlotsByName(PB)

    def retranslateUi(self, PB):
        PB.setWindowTitle(QtWidgets.QApplication.translate("PB", "Form", None, -1))

