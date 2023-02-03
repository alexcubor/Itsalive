#!/usr/bin/env python
# -*- coding: utf-8 -*-
def render(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'render',
    'toolTip': 'отправки на рендер кнопка'
    }
    return text
import re, os
from mt_root import root
try: import nuke
except: s=1

def start_importScript(WTName = {}, simpl = False):
    print('@@@ start_importScript')
    nk_work_file = root()['file']['prj'] + '/' + root()['file']['nk_out']
    # WTName = {
    #             'mEp': 'ep003', 'mSq': 'sq006', 'mSh': 'sh0605',
    #             'mVr': 'v002', 'mVrlist': ['v001', 'v002', 'v003'

    name = os.path.basename(nuke.root().name())
    p_re = root()['p_re']
    for_star = [k for k in p_re if re.findall(p_re[k], name)]
    if 'iSc' in for_star and 'iSh' in for_star and 'iVr' in for_star:

        iVr = re.findall('v[0-9][0-9][0-9]', name)[0]
        WTName['iVr'] = iVr
        for ess in WTName:
            if ess in nk_work_file:
                nk_work_file = nk_work_file.replace(ess, WTName[ess])
        print(nk_work_file)

        mov_path = nk_work_file
        node = nuke.createNode('Write')
        node['file'].setValue(mov_path)
        node['colorspace'].setValue('Output - sRGB')
        node['file_type'].setValue('mov')
        node['mov64_codec'].setValue('h264')
        node['mov_h264_codec_profile'].setValue('High 4:2:0 8-bit')

