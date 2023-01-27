#!/usr/bin/env python
# -*- coding: utf-8 -*-
def importMasterAsset(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'importMasterAsset',
    'toolTip': 'импорт мастер-скриптов - заранее подготовленные лидом проекта мастер-скрипты под эпизод или сиквенцию - там просто выбор из скриптов положенных в правильные места (там где договоримся держать мастера или композные ассеты\пресборки фксов в том числе)'
    }
    return text
'''


from project_key.project_read import _EpSqSh_, __work_list__, __ProectKeys__
import re
try:
    import nuke
except: s=1

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
'''