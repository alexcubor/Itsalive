#!/usr/bin/env python
# -*- coding: utf-8 -*-
def importScript(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        start_importScript(WTName, simpl)
def info():
    text = {
    'name': 'importScript',
    'toolTip': 'кнопка позволят заимпортить последний скрипт из другого шота не открывая его, (необходимо для артистов при копирований мастер\шотов или аналогичных уже сделанных) '
    }
    return text

from imp import reload
try: import nuke,nukescripts
except: s=1
import os
from mt_root import root

def start_importScript(WTName = {}, simpl = False):
    nk_work_file = os.path.dirname(root()['file']['prj'] + '/' + root()['file']['nk']) +'/'+ WTName['iSel']

    # WTName = {
    #       'iPr': '3033', 'iEp': 'ep01', 'iSc': 'sc02', 'iSh': 'sh020',
    #       'iVr': 'v003', 'iVrlist': ['v001', 'v002', 'v003'],
    #       'iSel': 'sc02_sh020_comp_v003.nk'}

    for tsk in WTName:
        if tsk in nk_work_file:
            nk_work_file = nk_work_file.replace(tsk, WTName[tsk])
    file = nk_work_file

    if os.path.isfile(file):
        # _ dot  ################
        d = nuke.createNode('Dot')
        dx, dy = d.xpos(), d.ypos()
        nuke.delete(d)
        ################
        print('file', file)

        copy_paste_file(file)

def copy_paste_file(file):
        try:
            os.system('echo ' + file + '| clip')
            nuke.nodePaste(nukescripts.cut_paste_file())
            os.system('echo off | clip')
        except: s = 1
