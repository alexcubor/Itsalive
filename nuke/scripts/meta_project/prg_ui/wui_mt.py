# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bzufarov/Documents/Itsalive/nuke/scripts/meta_project/prg_ui/mt_ui/wui_mt.ui',
# licensing of 'C:/Users/bzufarov/Documents/Itsalive/nuke/scripts/meta_project/prg_ui/mt_ui/wui_mt.ui' applies.
#
# Created: Wed Feb  1 22:34:34 2023
#      by: pyside2-uic  running on PySide2 5.12.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_BMT(object):
    def setupUi(self, BMT):
        BMT.setObjectName("BMT")
        BMT.resize(294, 465)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(BMT)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QtWidgets.QWidget(BMT)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_prj = QtWidgets.QFrame(self.widget)
        self.frame_prj.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prj.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prj.setObjectName("frame_prj")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_prj)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmb_0 = QtWidgets.QComboBox(self.frame_prj)
        self.cmb_0.setObjectName("cmb_0")
        self.horizontalLayout_3.addWidget(self.cmb_0)
        self.pb_archive = QtWidgets.QPushButton(self.frame_prj)
        self.pb_archive.setObjectName("pb_archive")
        self.horizontalLayout_3.addWidget(self.pb_archive)
        self.verticalLayout.addWidget(self.frame_prj)
        self.label_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setWeight(50)
        font.setBold(False)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.frame_mt = QtWidgets.QFrame(self.widget)
        self.frame_mt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_mt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mt.setObjectName("frame_mt")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_mt)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pb_reload = QtWidgets.QPushButton(self.frame_mt)
        self.pb_reload.setObjectName("pb_reload")
        self.verticalLayout_2.addWidget(self.pb_reload)
        self.frame_out = QtWidgets.QFrame(self.frame_mt)
        self.frame_out.setMinimumSize(QtCore.QSize(0, 110))
        self.frame_out.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_out.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_out.setObjectName("frame_out")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_out)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_up = QtWidgets.QPushButton(self.frame_out)
        self.pb_up.setMinimumSize(QtCore.QSize(25, 108))
        self.pb_up.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pb_up.setObjectName("pb_up")
        self.horizontalLayout.addWidget(self.pb_up)
        self.pb_out = QtWidgets.QPushButton(self.frame_out)
        self.pb_out.setMinimumSize(QtCore.QSize(190, 108))
        self.pb_out.setObjectName("pb_out")
        self.horizontalLayout.addWidget(self.pb_out)
        self.pb_down = QtWidgets.QPushButton(self.frame_out)
        self.pb_down.setMinimumSize(QtCore.QSize(25, 108))
        self.pb_down.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pb_down.setObjectName("pb_down")
        self.horizontalLayout.addWidget(self.pb_down)
        self.verticalLayout_2.addWidget(self.frame_out)
        self.frame_menu = QtWidgets.QFrame(self.frame_mt)
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmb_1 = QtWidgets.QComboBox(self.frame_menu)
        self.cmb_1.setObjectName("cmb_1")
        self.horizontalLayout_2.addWidget(self.cmb_1)
        self.cmb_2 = QtWidgets.QComboBox(self.frame_menu)
        self.cmb_2.setObjectName("cmb_2")
        self.horizontalLayout_2.addWidget(self.cmb_2)
        self.cmb_3 = QtWidgets.QComboBox(self.frame_menu)
        self.cmb_3.setObjectName("cmb_3")
        self.horizontalLayout_2.addWidget(self.cmb_3)
        self.verticalLayout_2.addWidget(self.frame_menu)
        self.cmb_nk = QtWidgets.QComboBox(self.frame_mt)
        self.cmb_nk.setObjectName("cmb_nk")
        self.verticalLayout_2.addWidget(self.cmb_nk)
        self.verticalLayout.addWidget(self.frame_mt)
        self.frame_knob = QtWidgets.QFrame(self.widget)
        self.frame_knob.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_knob.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_knob.setObjectName("frame_knob")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_knob)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_pBar = QtWidgets.QVBoxLayout()
        self.layout_pBar.setObjectName("layout_pBar")
        self.gridLayout.addLayout(self.layout_pBar, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_knob)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.widget)

        self.retranslateUi(BMT)
        QtCore.QMetaObject.connectSlotsByName(BMT)

    def retranslateUi(self, BMT):
        BMT.setWindowTitle(QtWidgets.QApplication.translate("BMT", "Form", None, -1))
        self.pb_archive.setText(QtWidgets.QApplication.translate("BMT", "PushButton", None, -1))
        self.label_name.setText(QtWidgets.QApplication.translate("BMT", "TextLabel", None, -1))
        self.pb_reload.setText(QtWidgets.QApplication.translate("BMT", "PushButton", None, -1))
        self.pb_up.setText(QtWidgets.QApplication.translate("BMT", "PushButton", None, -1))
        self.pb_out.setText(QtWidgets.QApplication.translate("BMT", "PushButton", None, -1))
        self.pb_down.setText(QtWidgets.QApplication.translate("BMT", "PushButton", None, -1))

