#!/usr/bin/env python
# -*- coding: utf-8 -*-
def publish(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'publish',
    'toolTip': 'паблиша в шотган'
    }
    return text

