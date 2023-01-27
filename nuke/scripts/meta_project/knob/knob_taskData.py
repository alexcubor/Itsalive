#!/usr/bin/env python
# -*- coding: utf-8 -*-
def taskData(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'taskData',
    'toolTip': 'при выбранном шоте если нажать на кнопку - выскакивает внизу окно с ноутами последними,  дескрипшеном, экспликацией на данный эпизод\сиквенс'
    }
    return text