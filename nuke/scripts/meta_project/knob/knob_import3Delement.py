#!/usr/bin/env python
# -*- coding: utf-8 -*-
def import3Delement(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'import3Delement',
    'toolTip': 'импорт камеры и различных алембик usd штук (должно окошко где мы выбираем что мы хотим заимпортить из продакшена для данного шота'
    }
    return text

import re, os
try: import nuke,nukescripts
except: s=1
from mt_root import root

def start_importScript(WTName = {}, simpl = False):
    file_key = root()['file']['prj'] + '/' + root()['file']['cam']
    fl = file_key
    for wtn in WTName:
        if wtn in fl:
            fl = fl.replace(wtn, WTName[wtn])
    cam_lst = [c for c in os.listdir(fl) if 'cam' in c]

    print('file_key', file_key)

    for cam in cam_lst:
        pfile = fl + '/' + cam
        create_cam(pfile, cam)

def create_cam(pfile, name ,mVr = ''):
    camFiles = pfile
    # _ dot  ################
    d = nuke.createNode('Dot')
    dx, dy = d.xpos(), d.ypos()
    nuke.delete(d)

    # Ca = nuke.createNode('Camera2', )
    Ca = nuke.nodes.Camera3()
    Ca['read_from_file'].setValue(True)
    Ca['frame_rate'].setValue(25)
    Ca['file'].setValue(camFiles)
    Ca['label'].setValue(name + '_' + mVr)
    Ca.setXYpos(dx, dy)
