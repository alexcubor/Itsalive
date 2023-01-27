#!/usr/bin/env python
# -*- coding: utf-8 -*-
def render(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'render',
    'toolTip': 'отправки на рендер кнопка'
    }
    return text


