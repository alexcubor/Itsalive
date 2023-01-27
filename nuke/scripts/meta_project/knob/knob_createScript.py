#!/usr/bin/env python
# -*- coding: utf-8 -*-
def createScript(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'createScript',
    'toolTip': 'назначеных артисту создания скрипта, если версия скрипта есть  создать новую версию на основе последнейесли это первая версия скрипта то он и создает и сразу открывает, если это не первая версия скрипта - то просто создает'
    }
    return text

# from project_key.project_read import _EpSqSh_, __work_list__, __ProectKeys__, re_keyFile
from mt_root import root
import re , os
try: import nuke
except: s=1

def start_importScript(WTName = {}, simpl = False):
    nk_work_file = root()['file']['prj'] + '/' + root()['file']['nk']
    # WTName = {
    #             'mEp': 'ep003', 'mSq': 'sq006', 'mSh': 'sh0605',
    #             'mVr': 'v002', 'mVrlist': ['v001', 'v002', 'v003'
    if WTName['iVrlist']:
        n_len = len(re.findall('[0-9]', root()['prj']['iVr']))
        vMax = int(''.join(re.findall('[0-9]', max(WTName['iVrlist']))))
        mVr = 'v'+str(int(vMax +1)).zfill(n_len)
    else:
        mVr = 'v001'
    print(mVr)

    WTName['iVr'] = mVr
    for ess in WTName:
        if ess in nk_work_file:
            nk_work_file = nk_work_file.replace(ess, WTName[ess])
    print(nk_work_file)
    work_file = os.path.dirname(nk_work_file)
    if not os.path.exists(work_file):
        os.mkdir(work_file)

    first_frame = 'first_frame 1'
    last_frame = 'last_frame 100'
    # if WTName['mFR']:
    #     first_frame =   'first_frame '  + str(WTName['mFR'].split('-')[0])
    #     last_frame =    'last_frame '   + str(WTName['mFR'].split('-')[1])

    nk = """Root {
                \n %s
                \n %s
                \n fps 24
                \n format "1920 1080 0 0 1920 1080 1 HD_1080"
                \n proxy_type scale
                \n proxy_format "1024 778 0 0 1024 778 1 1K_Super_35(full-ap)"
                \n colorManagement OCIO
                \n OCIO_config aces_1.2
                \n defaultViewerLUT "OCIO LUTs"
                \n workingSpaceLUT scene_linear
                \n monitorLut ACES/Rec.709
                \n monitorOutLUT "sRGB (ACES)"
                \n int8Lut matte_paint
                \n int16Lut texture_paint
                \n logLut compositing_log
                \n floatLut scene_linear
                \n}
                """ % (
                first_frame,
                last_frame,
            )

    with open(nk_work_file, "w") as w:
        w.write(nk)
    nuke.scriptOpen(nk_work_file)

















