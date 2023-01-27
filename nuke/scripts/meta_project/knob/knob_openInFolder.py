#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from mt_root import root
def openInFolder(dctESSmin = {}):
    if dctESSmin:

        inFile = root()['file']['prj']
        print(inFile)
        for ess in dctESSmin:
            if ess in inFile:
                inFile = inFile.replace(ess,dctESSmin[ess])
                print(ess,inFile)

        if os.path.isdir(inFile):
            os.startfile(inFile.replace('/','\\'))

    print(dctESSmin)
    print(info()['name'])
    print(info()['toolTip'])

def info():
    text = {
    'name': 'openInFolder',
    'toolTip': 'кнопка открывает папку in для данного шота\таска'
    }
    return text