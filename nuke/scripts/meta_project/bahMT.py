import os.path

from PySide2.QtWidgets import QWidget
from prg_ui.wui_mt import Ui_BMT
from prg_ui.ctr_PB import PB

import getpass
from imp import reload
from fnk.ctr_flowlayout import FlowLayout
from mt_root import root
from fnk_wtf import Ep_Sq_Sh_dct, \
    create_dctESSmin, task_list, \
    iName, iVrList, readlastESS,\
    openNK, repl
from rwInfo import prj_list_read, lastESS_read, lastESS_wright

from knob.fnc_creatPB import \
    knobListDef, pushBarId_bmp
class bah_mt(QWidget):
    def __init__(self, parent=None):
        super(bah_mt, self).__init__(parent)
        self.ui = Ui_BMT()
        self.ui.setupUi(self)

        self.workTaskName = {k:'' for k in root()['wtn']}
        self.workTaskName['iPr'] = root()['prj']['iPr']
        self.workTaskName['iUr'] = getpass.getuser()


        self.StartWorkAddWDGT()
        self.pb_set_value()
        ### start Menu set value
        self.menu_set_value()
        ### end menu set ###########
        self.step_reload()


    def pb_set_value(self):
        self.ui.pb_up.clicked.connect(self.step_up_down)
        self.ui.pb_down.clicked.connect(self.step_up_down)
        self.ui.pb_reload.clicked.connect(self.step_reload)
    def menu_set_value(self):
        # menu project name
        self.menu_prj = self.ui.cmb_0
        self.menu_prj.addItems(prj_list_read())
        self.menu_prj.activated.connect(self.connect_menu_prj)
        # menu ep,sc,sh
        self.cmb = [self.ui.cmb_1, self.ui.cmb_2, self.ui.cmb_3]
        self.menu = {
            root()['key'][i]: self.cmb[i] for i in range(len(self.cmb))
        }
        for k in root()['key']:
            self.menu[k].activated.connect(self.connect_menu_ess)
            self.menu[k].addItem(k)
        # menu nuke files
        self.menu_nk = self.ui.cmb_nk
        self.menu_nk.activated.connect(self.connect_menu_nk)
        #
    def connect_menu_prj(self):
        print('connect_menu_prj')
    def connect_menu_ess(self):
        widget = self.sender()
        self.ESS_setFiltr()
    def connect_menu_nk(self):
        print('connect_menu_nk')
        print(self.menu_nk.currentText())

        self.wtn()
    def step_up_down(self):
        key = 'iSh'
        widget = self.sender()
        print(widget.objectName())
        n = 1
        if widget.objectName() == 'pb_up':
            n = -1
        else:
            n = 1

        lens = self.menu[key].count()
        idx = self.menu[key].currentIndex()
        idx = idx + n
        if idx < 0 :    idx = lens-1
        elif idx >= lens:   idx = 0
        self.menu[key].setCurrentIndex(idx)

        self.ESS_setFiltr()
    def step_reload(self):
        print('step_reload')
        key = root()['key']
        essv = openNK()
        if essv:
            ess = {k:essv[k] for k in key}
        else:
            ess = lastESS_read()
        if ess:
            print('ess',ess)
            self.wright_ESSmenu(readlastESS(ess)['dict'])
            self.ESS_setFiltr()

            if 'iVr' in essv:
                nk = os.path.basename(root()['file']['nk'])
                nk = repl(nk,essv)
                nk_list = [self.menu_nk.itemText(index) for index in range(self.menu_nk.count())]
                index = nk_list.index(nk)
                self.menu_nk.setCurrentIndex(index)
                self.wtn()
    def ESS_setFiltr(self):
        read_SNT_ESS = self.read_ESS()
        EpSqShdct = Ep_Sq_Sh_dct(read_SNT_ESS)
        ESS = EpSqShdct['dict']
        self.wright_ESSmenu(ESS['dict'])

        self.wtn()

        self.nkList()
        self.wtn()
        # self.setPubIcon(tabname)
        self.setPublabelName()
    def read_ESS(self):
        rt_dict = root()
        key = root()['key']
        for k in key: # 'mEp', 'mSq', 'mSh'
            rt_dict['dict'][k]['id'] = self.menu[k].currentIndex()
            rt_dict['dict'][k]['snt'] = [self.menu[k].itemText(index) for index in range(self.menu[k].count())]
        # {'iEp': {'snt': ['t', 'e', 'x', 't', '[', 'i', 'd', 'x', ']'], 'id': 2}, 'iSc': {'snt': ['t', 'e', 'x', 't', '[', 'i', 'd', 'x', ']'], 'id': 8}, 'iSh': {'snt': ['t', 'e', 'x', 't', '[', 'i', 'd', 'x', ']'], 'id': 0}}
        return rt_dict
    def wright_ESSmenu(self,rt_dict):

        key = root()['key']

        text, index = [[], 0]
        for k in key:  # 'mEp', 'mSq', 'mSh'
            self.menu[k].clear()
            text = rt_dict[k]['snt']
            index = rt_dict[k]['id']
            for idx in range(len(text)):
                self.menu[k].addItem(text[idx])
            self.menu[k].setCurrentIndex(index)

            #
    def nkList(self):
        lst = task_list(self.workTaskName)
        if lst:
            self.menu_nk.clear()
            self.menu_nk.addItems(lst)
    def wtn(self):
        ## iEs, iSc, iSh ##
        ess = create_dctESSmin(self.read_ESS()['dict'])
        slkt_nk = {'iSel': self.menu_nk.currentText()}
        ## iVr ##
        lst = ['iVr']
        path = self.menu_nk.currentText()
        if not path:    v = {'iVr':''}
        else:           v = iName(lst, path)

        ## iVrlist ##
        nk_list = [self.menu_nk.itemText(index) for index in range(self.menu_nk.count())]
        if not nk_list: v_list = {'iVrlist': []}
        else:           v_list = {'iVrlist': iVrList(ess, nk_list)}

        essv = {**ess , **v , **v_list , **slkt_nk}
        # essv = ess | v | v_list | slkt_nk

        for k in essv:
            # if k in root()['prj']:
            self.workTaskName[k] = essv[k]
    ## TODO #######################################
    #     ess = create_dctESSmin(self.read_ESS()['dict'])
    #     self.wtn_set_dkt(ess)
    #
    #     slct = self.menu_nk.currentText()
    #     iVr = iName('iVr', slct)
    #     nk_list = [self.menu_nk.itemText(index) for index in range(self.menu_nk.count())]
    #     ess = {k: self.workTaskName[k] for k in root()['key']}
    #     vvl = {
    #         'iVr': iVr['iVr'],
    #         'iSel': slct,
    #         'iVrlist': iVrList(ess, nk_list)
    #     }
    #     self.wtn_set_dkt(vvl)
    #
    #     print(self.workTaskName)
    # def wtn_set_dkt(self, dkt = {}):
    #     for k in dkt:
    #         self.workTaskName[k]: dkt[k]
    #
    #     ## iEs, iSc, iSh ##

    def setPublabelName(self):
        # print('self setPublabelName')
        text = '_'
        key = root()['key']#, 'mPu'   # _EpSqSh_()['keyESS'][0,1]    #keyESS = 'mEp', 'mSq', 'mSh'
        text = '_'.join([self.workTaskName[k] for k in key])
        self.ui.label_name.setText(text)

    def StartWorkAddWDGT(self):
        FlwLut = FlowLayout()
        self.ui.layout_pBar.addLayout(FlwLut)
        self.wiget_dict = {
            'pBar': {},
            'knobIdList': pushBarId_bmp(),
            'layout_pBar': FlwLut,
            'needWDG': PB
        }
        self.wiget_dict =  self.AddWidget(self.wiget_dict)
    def AddWidget(self, masterDict):
        print('self AddWidget')
        knobIdList =    masterDict['knobIdList']
        needWDG =       masterDict['needWDG']
        layout_pBar =   masterDict['layout_pBar']
        pushBar_dict = {}
        buttn_idw = 0
        for knobID in knobIdList:
            pGp = 'bahMT'
            widget = needWDG(buttn_idw, knobID, pGp)
            widget.link.connect(self.Conect_pBar)
            layout_pBar.addWidget(widget)
            pushBar_dict[widget.buttn_idw] = widget
            buttn_idw += 1
        masterDict['pBar'] = pushBar_dict
        return masterDict
        # {0: <ctr_PB.PB(0x18a36bda2d0, name='PB') at 0x0000018A371223C8>,
        # 1: <ctr_... }, 2: ....}
    def Conect_pBar(self):
        print('self Conect_pBar')
        widget = self.sender()
        knobID = widget.knobID
        if str(knobID).isdigit():
            self.Button_work(widget)
        #
        # _Buttond
    def Button_work(self, widget):
            print('self Button_work')

            import knob.fnc_creatPB
            reload(knob.fnc_creatPB)

            buttn_idw = widget.buttn_idw
            knobID = widget.knobID

            if knobListDef()[knobID]['name'] == 'openScript':
                lastESS_wright(self.workTaskName)
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'createScript':
                lastESS_wright(self.workTaskName)
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'importScript':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'importOut':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'taskData':
                pass
                #
            elif knobListDef()[knobID]['name'] == 'noteStatus':
                pass
                #
            elif knobListDef()[knobID]['name'] == 'importUpdateIn':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'import3Delement':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            # elif knobListDef()[knobID]['name'] == 'importMasterAsset':
            elif knobListDef()[knobID]['name'] == 'importAllOut':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'switchTaskMeta':
                pass
                #
            elif knobListDef()[knobID]['name'] == 'finderListOfShots':
                pass
                #
            elif knobListDef()[knobID]['name'] == 'openInFolder':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'frameRangeUpdate':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'render':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            elif knobListDef()[knobID]['name'] == 'publish':
                knobListDef()[widget.knobID]['def'](self.workTaskName)
                #
            else:
                print('not set comand &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

                #

