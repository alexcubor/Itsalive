#!/usr/bin/env python
# -*- coding: utf-8 -*-
def frameRangeUpdate(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    # if WTName:
    # start_importScript(WTName, simpl)

def info():
    text = {
    'name': 'frameRangeUpdate',
    'toolTip': 'пробить framerange по шотгану в скрипте'
    }
    return text

'''

from fnk.fnk_nk import file_crt_ESS
from fnk.fnk_WTF import CRT_WT_Name, readSaved_list
try:
    import nuke,nukescripts
except: s=1



def start_importScript(WTName = {}, simpl = False):
    # WTName = {
    #             'mEp': 'ep003', 'mSq': 'sq006', 'mSh': 'sh0605',
    #             'mSp': 'Compose', 'mTs': 'comp', 'mTs_id': 1297315,
    #             'mSt': 'pndng', 'mEx': ['Alexander Melentyev', 'Alla Vostrikova'],
    #             'mPu': 'v006', 'mFR': '1-64',
    #             'mVr': 'v002', 'mVrdict': {'mVr': ['v006', 'v005', 'v004', 'v003', 'v002', 'v001'], 'id': 4},
    #             'mIc': '//omega/heroes/shots/ep003/ep003_sq006/ep003_sh0605/comp/publish/elements/ep003_sh0605/v006/ep003_sh0605.comp..v006.00032.png'}
    print('@@@ start_importScript')
    rrr = nuke.selectedNodes('Read') + nuke.selectedNodes('Group')
    if rrr:
        print('rrr')
        fr = [i['last'].value() for i in rrr]
        rott = nuke.root()
        rott['first_frame'].setValue(rrr[fr.index(max(fr))]['first'].value())
        rott['last_frame'].setValue(rrr[fr.index(max(fr))]['last'].value())
    else:
        nk_file = nuke.root().name()
        ESS = file_crt_ESS(nk_file)
        WTName = CRT_WT_Name(readSaved_list(ESS))[0]
        if WTName['mFR']:
            first_frame = WTName['mFR'].split('-')[0]
            last_frame = WTName['mFR'].split('-')[1]

            rott = nuke.root()
            rott['first_frame'].setValue(int(first_frame))
            rott['last_frame'].setValue(int(last_frame))
            print('frameRangeUpdate',first_frame,last_frame)

'''