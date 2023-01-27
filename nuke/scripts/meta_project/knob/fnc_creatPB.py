#!/usr/bin/env python
# -*- coding: utf-8 -*-

from imp import reload
import knob.knob_openScript
import knob.knob_createScript
import knob.knob_importScript
import knob.knob_importOut
import knob.knob_taskData
import knob.knob_noteStatus
import knob.knob_importUpdateIn
import knob.knob_import3Delement
import knob.knob_importMasterAsset
import knob.knob_importAllOut
import knob.knob_switchTaskMeta
import knob.knob_finderListOfShots
import knob.knob_openInFolder
import knob.knob_frameRangeUpdate
import knob.knob_render
import knob.knob_publish
reload(knob.knob_openScript)
reload(knob.knob_createScript)
reload(knob.knob_importScript)
reload(knob.knob_importOut)
reload(knob.knob_taskData)
reload(knob.knob_noteStatus)
reload(knob.knob_importUpdateIn)
reload(knob.knob_import3Delement)
reload(knob.knob_importMasterAsset)
reload(knob.knob_importAllOut)
reload(knob.knob_switchTaskMeta)
reload(knob.knob_finderListOfShots)
reload(knob.knob_openInFolder)
reload(knob.knob_frameRangeUpdate)
reload(knob.knob_render)
reload(knob.knob_publish)


from knob.knob_openScript           import openScript
from knob.knob_createScript         import createScript
from knob.knob_importScript         import importScript
from knob.knob_importOut            import importOut
from knob.knob_taskData             import taskData
from knob.knob_noteStatus           import noteStatus
from knob.knob_importUpdateIn       import importUpdateIn
from knob.knob_import3Delement      import import3Delement
from knob.knob_importMasterAsset    import importMasterAsset
from knob.knob_importAllOut         import importAllOut
from knob.knob_switchTaskMeta       import switchTaskMeta
from knob.knob_finderListOfShots    import finderListOfShots
from knob.knob_openInFolder         import openInFolder
from knob.knob_frameRangeUpdate     import frameRangeUpdate
from knob.knob_render               import render
from knob.knob_publish              import publish


def knobListDef(): # knobDefList()[0]()
    kbl_Def = {
        0:  {'def': openScript,         'name': 'openScript'},
        1:  {'def': createScript,       'name': 'createScript'},
        2:  {'def': importScript,       'name': 'importScript'},
        3:  {'def': importOut,          'name': 'importOut'},
        4:  {'def': taskData,           'name': 'taskData'},
        5:  {'def': noteStatus,         'name': 'noteStatus'},
        6:  {'def': importUpdateIn,     'name': 'importUpdateIn'},
        7:  {'def': import3Delement,    'name': 'import3Delement'},
        8:  {'def': importMasterAsset,  'name': 'importMasterAsset'},
        9:  {'def': importAllOut,       'name': 'importAllOut'},
        10: {'def': switchTaskMeta,     'name': 'switchTaskMeta'},
        11: {'def': finderListOfShots,  'name': 'finderListOfShots'},
        12: {'def': openInFolder,       'name': 'openInFolder'},
        13: {'def': frameRangeUpdate,   'name': 'frameRangeUpdate'},
        14: {'def': render,             'name': 'render'},
        15: {'def': publish,            'name': 'publish'}
    }
    return kbl_Def


def knobListToolTip():
    knbl_ToolTip = {
        0: 'кнопка  открытия назначеных артисту скрипта при выбранном таске . при правах лида - кнопка простого открытия шота должна быть активна, если лидовских прав у артиста нет то кнопка открытия скрипта должна быть инактивной. При пустом скрипте - открывает шот в этом же скрипте, если в скрипте уже что то есть или открыт другой шот - открывает новый шот в новом скрипте'
        , 1: 'назначеных артисту создания скрипта, если версия скрипта есть  создать новую версию на основе последнейесли это первая версия скрипта то он и создает и сразу открывает, если это не первая версия скрипта - то просто создает'
        , 2: 'кнопка позволят заимпортить последний скрипт из другого шота не открывая его, (необходимо для артистов при копирований мастер\шотов или аналогичных уже сделанных) '
        , 3: 'импорта посчитанной сиквенции выбранного шота'
        , 4: 'при выбранном шоте если нажать на кнопку - выскакивает внизу окно с ноутами последними,  дескрипшеном, экспликацией на данный эпизод\сиквенс'
        , 5: 'эта кнопка вызывает окно где человек может сменить статус шота на другой любой а так же написать ноут на композ или рендер и т.п.'
        , 6: 'открывает окно с апдейтом рендера и импорта разных ассетов\исходников\иллюстров всего что связано с данным шотом, внутри можно импортить просто риды, или если используется функционал скрипта с точками с неймингом - чтобы автоматом цеплялись исходники в скрипт, если нет то просто импорт и апдейт. обращается всегда в выбранную сущность проекта - если ты в this task - открывает все по твоему шоту, если ты в all tasks - открывает импорты того что там выбрано, апдейты рендеров делает на основе того что затянуто внутрь скрипта'
        , 7: 'импорт камеры и различных алембикusd штук (должно окошко где мы выбираем что мы хотим заимпортить из продакшена для данного шота'
        , 8: 'импорт мастер-скриптов - заранее подготовленные лидом проекта мастер-скрипты под эпизод или сиквенцию - там просто выбор из скриптов положенных в правильные места (там где договоримся держать мастера или композные ассеты\пресборки фксов в том числе)'
        , 9: 'импорт аутов всей сиквенции или эпизода(если нет сиквенций, или по выбору то либо другое) импортит в скрипт посчитанные пнг сиквенсы шотов объединенных contact sheet`ом(функционал смотрит в эпизод\сиквенцию открытого шота или выделенного в all tasks'
        , 10:'эта кнопка позволяет  переключиться в allTask - при выбранной мышкой read ноды затянутого шота  - переключает в сущность(контекст)  выбранного read'
        , 11: 'открывает окно с списком шотов (если открываем с сущности This task то открывается только выбранная сиквенция) но внутри должны быть фильтры позволяющие переключиться на любую другую сиквенцию и фильтр по статусам тасков с табнейлами '
        , 12: 'кнопка открывает папку in для данного шота\таска'
        , 13: 'пробить framerange по шотгану в скрипте'
        , 14: 'отправки на рендер кнопка'
        , 15: 'паблиша в шотган'
        }
    return knbl_ToolTip

def pushBarId_bmp():
    MyT_pBar = [0, 1, 2, 3, 6, 7, 12, 13, 14]
    # [knobListDef()[i]['name'] for i in MyT_pBar]
    return MyT_pBar
def pushBarId_myTask():
    MyT_pBar = [0, 1, 2, 3,9, 4]
    # [knobListDef()[i]['name'] for i in MyT_pBar]
    return MyT_pBar

def pushBarId_thisTask():
    ThT_pBar = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return ThT_pBar

def pushBarId_allTask():
    AlT_pBar = [6, 7, 8, 9, 10, 11, 12]
    return AlT_pBar

def pushBarId_finTask():
    MyT_pBar = [2, 9]
    # [knobListDef()[i]['name'] for i in MyT_pBar]
    return MyT_pBar



def pushBarId_workAllTask():
    WkT_pBar = [0, 1, 2, 3, 4, 5]
    return WkT_pBar

def pushBarId_workThisTask():
    WkT_pBar = [3, 4, 5]
    return WkT_pBar





from PySide2 import QtCore, QtGui, QtWidgets
import os

def knobIcon(file = ''):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(file), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon

def knobIconfold(name = ''):
    fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    file = fold +'/icon/icon_'+ name +'.png'
    return file