import json,os
from mt_root import root
def info_read(prj_name):
    fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    filePath = fold + '/_info/_' + prj_name +'__workTask_list' + '.json'
    return read_json(filePath)
def info_wright(prj_name,info):
    # print('def __work_list_Wright_',mPr_name)
    fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    filePath = fold + '/_info/_' + prj_name +'__workTask_list' + '.json'
    write_json(filePath, info)
def prj_list_read():
    fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    filePath = fold + '/_info/' +'prj_list' + '.json'
    return read_json(filePath)


def lastESS_read():
    fold = root()['file']['lastESS'].replace('\\', '/')
    fold = repl(fold,root()['wtn'])
    filePath = fold + '.json'
    if os.path.exists(filePath):
        return read_json(filePath)
    else:
        return {}
def lastESS_wright(wtn):
    info = {k: wtn[k] for k in root()['key']}
    # print('def __work_list_Wright_',mPr_name)
    fold = root()['file']['lastESS'].replace('\\', '/')
    fold = repl(fold, root()['wtn'])
    filePath = fold + '.json'
    write_json(filePath, info)
def repl(file = '', prj = {}):
    for p in prj:
        if p in file:
            file = file.replace(p, prj[p])
    return file


def read_json(filePath):
    file = open(filePath)
    data1 = json.load(file)
    file.close()
    return data1
def write_json(filePath,info_dict):
    file = open(filePath, "w")
    json.dump(info_dict, file, sort_keys=True, indent=4)
    file.close()