#!/usr/bin/env python
# -*- coding: utf-8 -*-
def importAllOut(WTName_list = {}):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName_list########',WTName_list)
    # if WTName_list:
    #     start_importOut(WTName_list)

def info():
    text = {
    'name': 'importAllOut',
    'toolTip': 'импорт аутов всей сиквенции или эпизода(если нет сиквенций, или по выбору то либо другое) импортит в скрипт посчитанные пнг сиквенсы шотов объединенных contact sheet`ом(функционал смотрит в эпизод\сиквенцию открытого шота или выделенного в all tasks'
    }
    return text



'''
from imp import reload
try:
    import nuke
except:
    s=1
import os
import fnk.fnk_WTF
reload(fnk.fnk_WTF)
from fnk.fnk_WTF import CTR_ESS_dict, fltr_ess_list
import project_key.project_read
reload(project_key.project_read)
from project_key.project_read import _EpSqSh_, __work_list__, __ProectKeys__

def start_importOut(WTName_list = {}):
    out_file_dict = {}
    out_pub_file = __ProectKeys__()['file']['out_pub_file']
    # WTName_list = {
    #             'mEp': 'ep003', 'mSq': 'sq006', 'mSh': 'sh0605',
    #             'mSp': 'Compose', 'mTs': 'comp', 'mTs_id': 1297315,
    #             'mSt': 'pndng', 'mEx': ['Alexander Melentyev', 'Alla Vostrikova'],
    #             'mPu': 'v006', 'mFR': '1-64',
    #             'mVr': 'v002', 'mVrdict': {'mVr': ['v006', 'v005', 'v004', 'v003', 'v002', 'v001'], 'id': 4},
    #             'mIc': '//omega/heroes/shots/ep003/ep003_sq006/ep003_sh0605/comp/publish/elements/ep003_sh0605/v006/ep003_sh0605.comp..v006.00032.png'}


    print(out_pub_file)
    ######################################
    for WTName in WTName_list:
        file = out_pub_file.replace('mVr', 'mPu')
        for tsk in WTName:
            if tsk in file:
                file = file.replace(tsk, WTName[tsk])
        out_file_dict[WTName['mSh']] = {'file':file,'mFR':WTName['mFR']}
    
    print(out_file_dict)
    
    
    ######################################

    # _ dot  ################
    d = nuke.createNode('Dot')
    dx, dy = d.xpos(), d.ypos()
    nuke.delete(d)
    ################

    # _ File  ################
    ################
    nodeReadS = nodeReadS_(out_file_dict)

    ################

    # _ XY #########
    x, y = dx, dy
    xx, yy = 110, 140
    c, d = 0, 1
    for n in nodeReadS:
        n.setXYpos(x + xx * c, y + yy * d)
        if c < 2 : c= c + 1
        else:
            c = 0; d = d + 1
    if len(nodeReadS)>1:
        X = nuke.root().width()
        Y = nuke.root().height() / 3 * d

        # _ ContactSheet ###########
        c_sh = nuke.nodes.ContactSheet()
        c_sh['width'].setValue(X)
        c_sh['height'].setValue(Y)
        c_sh['rows'].setValue(d)
        c_sh['columns'].setValue(3)
        c_sh['roworder'].setValue('TopBottom')
        c_sh.setXYpos(dx + xx * 4, dy + yy)
        for i in range(len(nodeReadS)):
            c_sh.setInput(i, nodeReadS[i])

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
'''