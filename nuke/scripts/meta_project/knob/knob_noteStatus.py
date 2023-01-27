#!/usr/bin/env python
# -*- coding: utf-8 -*-
def noteStatus(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'noteStatus',
    'toolTip': 'эта кнопка вызывает окно где человек может сменить статус шота на другой любой а так же написать ноут на композ или рендер и т.п.'
    }
    return text