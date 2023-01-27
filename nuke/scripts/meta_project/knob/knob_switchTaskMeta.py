#!/usr/bin/env python
# -*- coding: utf-8 -*-
def switchTaskMeta(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'switchTaskMeta',
    'toolTip': 'эта кнопка позволяет  переключиться в allTask - при выбранной мышкой read ноды затянутого шота  - переключает в сущность(контекст)  выбранного read'
    }
    return text