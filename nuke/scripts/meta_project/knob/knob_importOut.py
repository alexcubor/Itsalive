#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def importOut(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        start_importOut(WTName,simpl)

def info():
    text = {
    'name': 'importOut',
    'toolTip': 'импорта посчитанной сиквенции выбранного шота'
    }
    return text


from imp import reload
try: import nuke, nukescripts
except: s=1
import os
from mt_root import root
def start_importOut(WTName = {},simpl = False):
    # WTName = {
    #             'mEp': 'ep003', 'mSq': 'sq006', 'mSh': 'sh0605',
    #             'mVr': 'v002', 'mVrdict': {'mVr': ['v006', 'v005', 'v004', 'v003', 'v002', 'v001'], 'id': 4},

    out_file_dict = {}
    out_pub_file = root()['file']['prj'] + '/' + root()['file']['nk_out']
    print(out_pub_file)

    file = out_pub_file.split('/iVr')[0]
    for tsk in WTName:
        if tsk in file:
            file = file.replace(tsk, WTName[tsk])
    print(file)
    copy_paste_file(file)

    '''
    out_file = os.path.dirname(file)
    print('out_file',out_file)
    out_lst = os.listdir(out_file)
    fr = \
        str(int(''.join(re.findall('[0-9][0-9][0-9][0-9]', out_lst[0])))) \
        +'-'+ \
        str(int(''.join(re.findall('[0-9][0-9][0-9][0-9]', out_lst[-1]))))

    out_file_dict[WTName['mSh']] = {'file':file,'mFR':fr}


    # _ dot  ################
    d = nuke.createNode('Dot')
    dx, dy = d.xpos(), d.ypos()
    nuke.delete(d)
    
    nodeReadS = nodeReadS_(out_file_dict)

    x, y = dx, dy
    xx, yy = 110, 140
    c, d = 0, 1
    for n in nodeReadS:
        n.setXYpos(x + xx * c, y + yy * d)
        if c < 2 : c= c + 1
        else:
            c = 0; d = d + 1
    '''
def nodeReadS_(out_file_dict = {}):
    dict = out_file_dict
    nodeReadS = []
    x, y = 0, 0
    for out in dict:
        r_file = dict[out]['file']
        if os.path.isdir(os.path.dirname(r_file)):
            fr_first,fr_last = [int(i) for i in dict[out]['mFR'].split('-')]

            node = nuke.nodes.Read()
            node['file'].setValue(r_file)
            node['first'].setValue(fr_first)
            node['last'].setValue(fr_last)
            node['origfirst'].setValue(fr_first)
            node['origlast'].setValue(fr_last)

            node.setXYpos(x, y)

            x = x + 100
            nodeReadS.append(node)
    return nodeReadS

def copy_paste_file(file):
    try:
        os.system('echo ' + file + '| clip')
        nuke.nodePaste(nukescripts.cut_paste_file())
        os.system('echo off | clip')
    except:
        s = 1
