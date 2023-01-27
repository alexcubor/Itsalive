import json,os

def info_read(prj_name):
    fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    filePath = fold + '/_' + prj_name +'__workTask_list' + '.json'
    return read_json(filePath)

def info_wright(prj_name,info):
    # print('def __work_list_Wright_',mPr_name)
    fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    filePath = fold + '/_' + prj_name +'__workTask_list' + '.json'
    write_json(filePath, info)


def prj_list_read():
    fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    filePath = fold + '/' +'prj_list' + '.json'
    return read_json(filePath)
def read_json(filePath):
    file = open(filePath)
    data1 = json.load(file)
    file.close()
    return data1
def write_json(filePath,info_dict):
    file = open(filePath, "w")
    json.dump(info_dict, file, sort_keys=True, indent=4)
    file.close()