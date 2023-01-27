from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot, Signal
from PySide2 import QtCore
from knob.fnc_creatPB import \
    knobIcon, knobIconfold, \
    knobListDef , knobListToolTip
from prg_ui.wui_PB import Ui_PB

class PB(QWidget):
    link = Signal()
    def __init__(self, buttn_idw, knobID, parentGroup, parent=None):
        super(PB, self).__init__(parent)
        self.ui = Ui_PB()
        self.ui.setupUi(self)

        self.buttn_idw = buttn_idw
        self.knobID = knobID
        self.parentGroup = parentGroup
        self.pb_PshBtt = self.ui.pb_PB

        knobName    = knobListDef()[self.knobID]['name']
        knobToolTip = knobListToolTip()[self.knobID]

        file = knobIconfold(knobName)
        icon = knobIcon(file)
        self.ui.pb_PB.setIcon(icon)
        self.ui.pb_PB.setIconSize(QtCore.QSize(40, 40))
        self.ui.pb_PB.setToolTip(knobName +':\n'+ knobToolTip)

        self.ui.pb_PB.clicked.connect(self.link)
        #self.ui_to_meta.pb_PB.ToolTip()
        #self.splitter_ui.pb_PB.setEnabled()
    @Slot()
    def press_del(self):
        self.delete.emit(self.idw)

#['FR', 'inCam', 'inform', 'inOut', 'inRren', 'newScript', 'opFS', 'opOut', 'opRen', 'opScript', 'publ', 'scDown', 'scUp', 'setSG', 'toAf']

#a= 'C:/Users/bzufarov/PycharmProjects/baha/mt_icon'
#[i.split('icon_')[1].split('.')[0] for i in os.listdir(a) if 'icon_' in i]


        #file = ctrfold('icon_' + pb_name + '.png', 'mt_icon')
        #mt_icon = ctrIcon(file)