#!/usr/bin/env python
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
def openScript(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'openScript',
    'toolTip': 'кнопка  открытия назначеных артисту скрипта при выбранном таске . при правах лида - кнопка простого открытия шота должна быть активна, если лидовских прав у артиста нет то кнопка открытия скрипта должна быть инактивной. При пустом скрипте - открывает шот в этом же скрипте, если в скрипте уже что то есть или открыт другой шот - открывает новый шот в новом скрипте'
    }
    return text


import os
try: import nuke
except: s=1
from mt_root import root
def start_importScript(WTName = {}, simpl = False):
    compFile = os.path.dirname(root()['file']['prj'] + '/' + root()['file']['nk']) +'/'+ WTName['iSel']
    for k in WTName:
        if k in compFile:
            compFile = compFile.replace(k, WTName[k])
    print('compFile', compFile)
    openNK(compFile)

def openNK( compFile ):
    # try:
    #     nuke.scriptName()
    # except:
    #     if os.path.isfile(os.getenv('NUKE_TEMP_DIR') + '/tmp.nk'):
    #         os.remove(os.getenv('NUKE_TEMP_DIR') + '/tmp.nk')
    #     nuke.scriptSaveAs(os.getenv('NUKE_TEMP_DIR') + '/tmp.nk')
    nuke.scriptOpen( compFile )
    #
    #