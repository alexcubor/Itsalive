#!/usr/bin/env python
# -*- coding: utf-8 -*-
def importUpdateIn(WTName = {}, simpl = False):
    print(info()['name'])
    print(info()['toolTip'])
    print('WTName########',WTName)
    if WTName:
        in_file = root()['file']['prj'] + '/' + root()['file']['fx']
        start_importUpdateIn(WTName, in_file)
        in_file = root()['file']['prj'] + '/' + root()['file']['render']
        start_importUpdateIn(WTName, in_file)
        in_file = root()['file']['prj'] + '/' + root()['file']['UE']
        start_importUpdateIn(WTName, in_file)

        pass
def info():
    text = {
    'name': 'importUpdateIn',
    'toolTip': 'открывает окно с апдейтом рендера и импорта разных ассетов\исходников\иллюстров всего что связано с данным шотом, внутри можно импортить просто риды, или если используется функционал скрипта с точками с неймингом - чтобы автоматом цеплялись исходники в скрипт, если нет то просто импорт и апдейт. обращается всегда в выбранную сущность проекта - если ты в this task - открывает все по твоему шоту, если ты в all tasks - открывает импорты того что там выбрано, апдейты рендеров делает на основе того что затянуто внутрь скрипта'
    }
    return text

from imp import reload
import re, os
import read_grp_node
reload(read_grp_node)
try: import nuke
except: s=1
from mt_root import root


def start_importUpdateIn(WTName = {}, in_file = ''):
    # in_file = root()['file']['prj'] +'/'+ root()['file']['render']
    # WTName = {
    #             'mEp': 'ep003', 'mSq': 'sq006', 'mSh': 'sh0605',
    #             'mPu': 'v006', 'mFR': '1-64',
    #             'mVr': 'v002', 'mVrdict': {'mVr': ['v006', 'v005'
    file_in = in_file.split('/iVr')[0]
    for tsk in WTName:
        if tsk in file_in:
            file_in = file_in.replace(tsk, WTName[tsk])

    mLy_dict = {**in_render(file_in)[0] , **in_render(file_in)[1] }



    # _import_#######
    d = nuke.createNode('Dot')
    dx, dy = d.xpos(), d.ypos()
    x = dx
    nuke.delete(d)
    postag = 1
    if mLy_dict:
        beauty_nodes = read_in_list(mLy_dict, postag)
            # creatr read_group node
        for k in beauty_nodes:
            y = dy
            for node in beauty_nodes[k]:
                node.setXYpos(x, y)
                y = y + 100
            x = x + 100



def in_render(file_in, all_or_end='end'):
    mLy_dict = {}
    mLy_dict_other = {}
    r_in_file = file_in
    if os.path.isdir(r_in_file):

        r_list = os.listdir(r_in_file)
        in_vers = [f for f in r_list if re.match('v[0-9][0-9][0-9]', f)]

        for vers in in_vers:
            for mLy in os.listdir(r_in_file + '/' + vers):
                if not os.path.isfile(r_in_file + '/' + vers + '/' + mLy):
                    mLy_dict[mLy] = ''
                else:
                    mLy_dict_other[os.path.splitext(os.path.splitext(mLy)[0])[0]] = ''
        # for vers in in_vers:
        #     for mLy in os.listdir(r_in_file + '/' + vers):
        #         if re.match('[0-9][0-9]_.*_[0-9][0-9]', mLy):
        #             mLy_dict[mLy] = ''
        #         else:
        #             mLy_dict_other[mLy] = ''



        for mLy in mLy_dict:
            b = []
            for vers in in_vers:
                if mLy in os.listdir(r_in_file + '/' + vers):
                    b.append(r_in_file + '/' + vers + '/' + mLy)
            # _END_vers_ or _ALL_vers_
            if all_or_end == 'end':
                mLy_dict[mLy] = [max(b)]
            else:
                mLy_dict[mLy] = b

        for mLy in mLy_dict_other:
            b = []
            for vers in in_vers:
                ddd = [True for i in os.listdir(r_in_file + '/' + vers) if mLy in i ]
                if True in ddd:
                    b.append(r_in_file + '/' + vers )
                    # b.append(r_in_file + '/' + vers + '/' + mLy)
            # _END_vers_ or _ALL_vers_

            if all_or_end == 'end':
                mLy_dict_other[mLy] = [max(b)]
            else:
                mLy_dict_other[mLy] = b

    return mLy_dict, mLy_dict_other

def read_in_list(inRenrer_list, postag=0):
    R_list = {}
    for k in inRenrer_list:
        R_list[k] = [creatr_read_node(file, postag) for file in inRenrer_list[k] if os.listdir(file)]
    return R_list

def creatr_read_node(file, postag=0):
    if os.path.isfile(file):
        read_node = nuke.nodes.Read()
        read_node['file'].setValue(file)
        read_node['postage_stamp'].setValue(postag)

    if os.path.isdir(file):
        if 'beauty' in os.listdir(file):
            read_node = read_grp_node.create_read_gr()

            read_node['file'].setValue(file + '/')
            r_gr = read_node

            read_grp_node.read_gr(r_gr)

        else:
            read_node = nuke.nodes.Read()

            XXXX = [i for i in os.listdir(file) if 'exr' in i or 'png' in i][0]
            r_file = file + '/' + XXXX.split('.')[0] + '.%' + str(len(XXXX.split('.')[1])).zfill(2) + 'd.' + \
                     XXXX.split('.')[-1]

            read_node['file'].setValue(r_file)
            read_node['postage_stamp'].setValue(postag)

            exr = os.listdir(file)
            exr.sort()
            exr = [i for i in exr if 'exr' in i or 'png' in i]
            fr_first = int(exr[0].split('.')[1])
            fr_last = int(exr[-1].split('.')[1])

            read_node['first'].setValue(fr_first)
            read_node['last'].setValue(fr_last)
            read_node['origfirst'].setValue(fr_first)
            read_node['origlast'].setValue(fr_last)

    return read_node
