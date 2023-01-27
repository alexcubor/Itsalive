#!/usr/bin/env python
# -*- coding: utf-8 -*-
def finderListOfShots(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        # start_importScript(WTName, simpl)
        pass
def info():
    text = {
    'name': 'finderListOfShots',
    'toolTip': 'открывает окно с списком шотов (если открываем с сущности This task то открывается только выбранная сиквенция) но внутри должны быть фильтры позволяющие переключиться на любую другую сиквенцию и фильтр по статусам тасков с табнейлами'
    }
    return text