#!/usr/bin/env python
# -*- coding: utf-8 -*-
def frameRangeUpdate(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    # if WTName:
    start_importScript(WTName, simpl)

def info():
    text = {
    'name': 'frameRangeUpdate',
    'toolTip': 'пробить framerange по шотгану в скрипте'
    }
    return text




try:
    import nuke,nukescripts
except: s=1



def start_importScript(WTName = {}, simpl = False):
    print('@@@ start_importScript')
    rrr = nuke.selectedNodes('Read') + nuke.selectedNodes('Group')
    if rrr:
        print('rrr')
        fr = [i['last'].value() for i in rrr]
        rott = nuke.root()
        rott['first_frame'].setValue(rrr[fr.index(max(fr))]['first'].value())
        rott['last_frame'].setValue(rrr[fr.index(max(fr))]['last'].value())

