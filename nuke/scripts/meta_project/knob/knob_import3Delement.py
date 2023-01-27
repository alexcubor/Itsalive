#!/usr/bin/env python
# -*- coding: utf-8 -*-
def import3Delement(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'import3Delement',
    'toolTip': 'импорт камеры и различных алембик usd штук (должно окошко где мы выбираем что мы хотим заимпортить из продакшена для данного шота'
    }
    return text

import re, os
try:
    import nuke
except: s=1
'''
def start_importScript(WTName = {}, simpl = False):
    # nk_pub_file = __ProectKeys__()['file']['nk_pub_file']
    nk_pub_file = __ProectKeys__()['file']['nk_work_file']
    nk_work_file = __ProectKeys__()['file']['nk_work_file']
    # WTName = {
    #             'mEp': 'ep003', 'mSq': 'sq006', 'mSh': 'sh0605',
    #             'mSp': 'Compose', 'mTs': 'comp', 'mTs_id': 1297315,
    #             'mSt': 'pndng', 'mEx': ['Alexander Melentyev', 'Alla Vostrikova'],
    #             'mPu': 'v006', 'mFR': '1-64',
    #             'mVr': 'v002', 'mVrdict': {'mVr': ['v006', 'v005', 'v004', 'v003', 'v002', 'v001'], 'id': 4},
    #             'mIc': '//omega/heroes/shots/ep003/ep003_sq006/ep003_sh0605/comp/publish/elements/ep003_sh0605/v006/ep003_sh0605.comp..v006.00032.png'}
    # ImpCam_(WTName['mEp'], WTName['mSh'])

    in_file = __ProectKeys__()['file']['in_file'].split('mEp')[0]
    f = in_file + WTName['mEp'] + '/' + WTName['mSh'] + '/' + 'data/abc'
    if os.path.isdir(f):
        pfile = f + '/' + max(
            [i for i in filter(lambda i: i.endswith('.abc'), os.listdir(f)) if re.match('.*' + 'camera' + '.*', i)])
        mVr = 'v' + pfile.split('_v')[1][:3]
        name = os.path.basename(pfile)
        create_cam(pfile, name)


    file_key = in_file + '/mEp/mEp_mSq/mEp_mSh/stage/mVr/cam_mEp_mSh.abc'
    fl = file_key
    for wtn in WTName:
        if wtn in fl:
            fl = fl.replace(wtn, WTName[wtn])
    file, name = fl.split('/' + WTName['mVr'] + '/')
    if os.path.isdir(file):
        print('file, name', file, name)
        mVr = max([v for v in os.listdir(file)
                    if re.match('v[0-9][0-9][0-9]', v)
                    if name in os.listdir(file + '/' + v)
                   ])
        pfile = file + '/' + mVr + '/' + name
        create_cam(pfile, name, mVr)

def create_cam(pfile, name ,mVr = ''):
    camFiles = pfile
    # _ dot  ################
    d = nuke.createNode('Dot')
    dx, dy = d.xpos(), d.ypos()
    nuke.delete(d)

    # Ca = nuke.createNode('Camera2', )
    Ca = nuke.nodes.Camera2()
    Ca['read_from_file'].setValue(True)
    Ca['frame_rate'].setValue(25)
    Ca['file'].setValue(camFiles)
    Ca['label'].setValue(name + '_' + mVr)
    Ca.setXYpos(dx, dy)

def ImpCam_(p_sire, p_low):
    # p_sire , p_low  = nuke.root().name().split('/')[-1].split('_')[0:2]
    # p_sire='ep035' , p_low='sh0106'
    in_file = __ProectKeys__()['file']['in_file'].split('mEp')[0]
    f = in_file + p_sire + '/' + p_low + '/' + 'data/abc'
    if os.path.isdir(f):
        camFiles = f + '/' + max(
            [i for i in filter(lambda i: i.endswith('.abc'), os.listdir(f)) if re.match('.*' + 'camera' + '.*', i)])
        v = 'v' + camFiles.split('_v')[1][:3]

        # _ dot  ################
        d = nuke.createNode('Dot')
        dx, dy = d.xpos(), d.ypos()
        nuke.delete(d)

        # Ca = nuke.createNode('Camera2', )
        Ca = nuke.nodes.Camera2()
        Ca['read_from_file'].setValue(True)
        Ca['frame_rate'].setValue(25)
        Ca['file'].setValue(camFiles)
        Ca['label'].setValue('cam_' + p_sire + '_' + p_low + '_' + v)
        Ca.setXYpos(dx,dy)
        
'''