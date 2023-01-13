import pymel.core as pm
import re
from functools import partial
from PySide2 import QtCore, QtWidgets, QtGui


class Batch(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setGeometry(500, 300, 260, 110)
        self.setWindowTitle("It's Render Stats")

        self.visibility_parms = ["primaryVisibility", "castsShadows",
                                 "aiVisibleInDiffuseReflection", "aiVisibleInSpecularReflection",
                                 "aiVisibleInDiffuseTransmission", "aiVisibleInSpecularTransmission",
                                 "aiVisibleInVolume", "aiSelfShadows"]
        self.other_parms = ["aiOpaque", "aiMatte"]

        # Add check boxes
        self.check_boxes = {}
        for name in self.visibility_parms:
            check_box = self.add_checkbox(name)
            self.check_boxes.update({name: check_box})
        sep = QtWidgets.QFrame()
        sep.setFrameShape(QtWidgets.QFrame.HLine)
        self.main_layout.addWidget(sep)
        for name in self.other_parms:
            check_box = self.add_checkbox(name)
            self.check_boxes.update({name: check_box})

        # Get geometry parameters for check boxes
        selection = pm.ls(sl=1)
        pm.select(selection, hi=1)
        self.shapes = pm.ls(sl=1, s=True)
        pm.select(selection)
        for parm_name in self.check_boxes:
            values = set([x.getAttr(parm_name) for x in self.shapes if x.hasAttr(parm_name)])
            if len(values) == 1:
                value = values.pop()
                if value:
                    self.check_boxes[parm_name].setCheckState(QtCore.Qt.CheckState.Checked)
                else:
                    self.check_boxes[parm_name].setCheckState(QtCore.Qt.CheckState.Unchecked)
            else:
                self.check_boxes[parm_name].setCheckState(QtCore.Qt.CheckState.PartiallyChecked)

    def add_checkbox(self, name):
        hbox = QtWidgets.QHBoxLayout()
        check_box = QtWidgets.QCheckBox(name)
        words = re.sub(r'([A-Z])', r' \1', name).split()
        check_box.setText(" ".join(words).title())
        hbox.addWidget(check_box)
        self.main_layout.addLayout(hbox)
        check_box.clicked.connect(partial(self.set_parameter, name))
        return check_box

    def set_parameter(self, name):
        box_value = self.check_boxes[name].checkState()
        if box_value == QtCore.Qt.CheckState.Checked:
            value = True
        else:
            value = False

        for shape in self.shapes:
            if shape.hasAttr(name):
                shape.setAttr(name, value)
