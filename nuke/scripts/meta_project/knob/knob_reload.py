#!/usr/bin/env python
# -*- coding: utf-8 -*-
def reload(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'reload',
    'toolTip': 'blablablablabla'
    }
    return text