#!/usr/bin/env python
# -*- coding: utf-8 -*-
def additionalMenu():
    print(info()['name'])
    print(info()['toolTip'])

def info():
    text = {
    'name': 'additionalMenu',
    'toolTip': 'дополнительный функционал, важно чтобы в случае добавления новых функций можно было их добавить в меню даже при отсутствии места на основном интерфейсе'
    }
    return text



