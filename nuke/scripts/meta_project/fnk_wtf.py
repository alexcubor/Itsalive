
import os,re
from rwInfo import info_read
from mt_root import root
try: import nuke
except: s=1
def readlastESS(ess_key_old):
    # print('wtf readSaved')
    #ess_key_old = {'mEp': 'ep002', 'mSq': 'sq005', 'mSh': 'sh0602'}
    # print('ess_key_old',ess_key_old)
    ess_list = info_read(root()['prj']['iPr'])
    ESSdct = root()
    ESSdct['dict'] = CTR_ESS_dict(ess_list, ess_key_old)['dict']
    return ESSdct

def Ep_Sq_Sh_dct(ESSdct={},simple_chac = False):
    # print('wtf Ep_Sq_Sh_dct')
    if not ESSdct: ESSdct = root()
    prj_name = ESSdct['prj']['iPr']

    ESS_list = info_read(prj_name)

    # step All ESS menu Skan  CTR_ESS_dict #########################
    ess_key_old = {ess: '' for ess in root()['key'] }
    if ESSdct['dict']: ess_key_old = create_dctESSmin(ESSdct['dict'])
    # ess_key_old = {'mEp':'ep001','mSq':'sq002','mSh':'sh0203'}
    ess_dict = CTR_ESS_dict(ESS_list, ess_key_old,simple_chac)
    ESSdct['dict']          = ess_dict['dict']

    #########################
    return {'dict': ESSdct}
def CTR_ESS_dict(ess_list = [] ,ess_key_old={},simple_chac = False):
    ################################
    keyESS = root()['key']
    # ess_list = [{
    #     "Compose": [
    #         {   "executor": ["Alisa Kostogarova"],
    #             "frameRenge": "1-44",
    #             "publish": "v003",
    #             "shot_id": 130139,
    #             "shot_name": "ep001_sh0203",
    #             "status": "clsd",
    #             "step": "comp",
    #             "step_id": 8,
    #             "task": "Compose",
    #             "task_id": 1198484            }
    #     ],
    #     "mEp": "ep001",
    #     "mSh": "sh0203",
    #     "mSh_id": 130139,
    #     "mSq": "sq002"
    #},,,... ]

    # ess_key_old = {'mEp':'ep001','mSq':'sq002','mSh':'sh0203'}
    # ess_key_old = generate_Sq(ess_key_old)
    ess_dick = {}

    for ess in keyESS:
        lsts = list(set([lst[ess] for lst in ess_list]))
        if not lsts: lsts = ['']
        lsts.sort()
        key = ess_key_old[ess]
        id = ess_id_generation(key,lsts)
        ess_dick[ess] = {'snt': lsts, 'id': id}
        ess_key = ess_dick[ess]['snt'][id]
        ess_list = [lst for lst in ess_list if lst[ess] == ess_key]
    ####################################
    #  ess_dick= {
    #       'mEp': {'snt': ['ep001', 'ep002'], 'id': 0},
    #       'mSq': {'snt': ['sq001', 'sq002'], 'id': 0},
    #       'mSh': {'snt': ['sh0101', 'sh0102', ... , 'sh0120'], 'id': 0},
    return {'dict':ess_dick}
def create_dctESSmin(ess_dict):
    # {'mEp':'ep001','mSq':'sq002','mSh':'sh0203'}
    dctESSmin = {}
    keyESS = root()['key']
    for k in keyESS:
        id = ess_dict[k]['id']
        key = ess_dict[k]['snt']
        dctESSmin[k] = key[id]
    return dctESSmin
def ess_id_generation(key,lsts):
    # print('wtf ess_id_generation')
    if key in lsts:
        id = lsts.index(key)
    else:
        lsts.append(key)
        lsts.sort()
        id = lsts.index(key)
        lsts.remove(key)
        if id >= len(lsts): id = len(lsts) - 1
        if id < 0:          id = 0
    return id


def repl(file = '', prj = {}):
    for p in prj:
        if p in file:
            file = file.replace(p, prj[p])
    return file


def task_list(wtn={}):
    # ['sc02_sh030_comp_v002.nk', 'sc02_sh030_comp_v001.nk', 'tt.nk', 'test_shuf_light_voo.nk']
    nk_list = ['']
    if not wtn:
        return

    path = os.path.dirname(root()['file']['prj'] + '/' + root()['file']['nk'])
    path = repl(path, wtn)
    if os.path.exists(path):
        nk_list = [
            nk
            for nk in
            filter(lambda i: i.endswith('.nk'), os.listdir(path))
        ]
        nk_list.sort(reverse=True)
    # sort nk filr list to name
    if nk_list:
        name = \
            os.path.splitext(
                os.path.basename(
                    root()['file']['prj'] + '/' +
                    root()['file']['nk'].split('iVr')[0]
                )
            )[0]
        name = repl(name, wtn)
        a = []
        b = []
        for nk in nk_list:
            if name in nk:  a.append(nk)
            else:           b.append(nk)
        nk_list =  a + b
    return nk_list
def iVrList(wtn = {}, nk_list = []):
    # print('fnk_wtf iVrList') # iVr_lst ['v001', 'v002']
    p_re = root()['p_re']
    nk_file = os.path.basename(root()['file']['nk']).split('iVr')[0]
    nk_file = repl(nk_file, wtn)
    iVr_lst = [
        ''.join(re.findall(p_re['iVr'], nkl))
        for nkl in nk_list
        if nk_file in nkl
    ]
    iVr_lst.sort()
    # print('iVr_lst',iVr_lst)
    return iVr_lst

def iName(lst = [],path = ''):
    # print('fnk_wtf iName')
    p_re = root()['p_re']
    dct = {
        k: ''.join(re.findall(p_re[k], path))
        for i in lst
        for k in p_re
        if k in lst
        if re.match('.*' + p_re[k], path)
    }
    # print('dct', dct)
    return dct

def openNK():
    name = nuke.root().name()
    p_re = root()['p_re']
    essv = {k: re.findall(p_re[k], name)[0] for k in p_re if re.findall(p_re[k], name)}
    if len(essv) == len(p_re):
        return essv
    else:
        return {}

# print(os.path.splitext('skdjhf.skdjhf'))
'''
def generate_Sq(ESS):
    import re
    mSq_re = _EpSqSh_()['reFind']['mSq']
    if not 'mSq' in ESS:
        mSq_len = len(re.findall('[0-9]', mSq_re))
        mSh = ESS['mSh']
        mSq_num = str(int(''.join(re.findall('[0-9]', mSh)[0:2]))).zfill(mSq_len)
        mSq = mSq_re[:mSq_len - 1] + mSq_num
        ESS['mSq'] = mSq
    return ESS

def fltr_ess_list(snt_filtr,ess_list):
    # print('wtf fltr_ess_list')
    # snt_filtr = {'mSt': 'all_status', 'mEx': 'ssergeev', 'mTs': 'comp'}
    keySNT      = _EpSqSh_()['keySNT']  # ['mSt', 'mEx', 'mTs']
    UserWork    = _EpSqSh_()['UserWork']
    new_ess_list = ess_list

    FiltrSNT = {k: snt_filtr[k] for k in keySNT if not 'all_' in snt_filtr[k]}
    #{'mSt': 'rdy', 'mEx': 'bzufarov'}
    if FiltrSNT:
        new_ess_list = []
        for lsk in ess_list:
            #{'Compose':[{'task':'comp','status': 'pndng', 'executor': 'ssergeev',...}, {'task':'key...}],
            #, 'mEp': 'ep888', 'mSh': 'sh0101', 'mSh_id': 124080, 'mSq': 'sq001'}
            taskF = []
            if UserWork in lsk:
                for wtt in  lsk[UserWork]:
                    #wtt = {'task':'comp','status': 'pndng',...}
                    WTT = transName(wtt)
                    #WTT = {'mSt': 'pndng', 'mEx': 'bzufarov', 'mPu': 'v004', 'mTs': 'comp'}
                    # filtring
                    key = FiltrSNT
                    A_dikt = FiltrSNT
                    B_dikt = WTT
                    chTs = ratio_dikt_TF(key, A_dikt, B_dikt)
                    if chTs:
                        taskF.append(wtt)
                if taskF:
                    lsk[UserWork]=taskF
                    new_ess_list.append(lsk)

    return new_ess_list
def transName(too_dict):
    # print('wtf transName')
    code = _EpSqSh_()['code']
    trn = {k: too_dict[code[k]] for k in code if code[k] in too_dict}
    # WTT = {'mSt': 'pndng', 'mEx': 'bzufarov', 'mPu': 'v004', 'mTs': 'comp'}
    return trn
def ratio_dikt_TF(key, A_dikt, B_dikt):#  True or False
    # print('wtf ratio_dikt_TF')
    ratio=False
    chTs = []
    for k in key:
        if k in A_dikt:
            if k in 'mEx':  chTs.append(A_dikt[k] in B_dikt[k])
            else:           chTs.append(A_dikt[k] == B_dikt[k])
    if not False in chTs:
        ratio = True
    return ratio


def readSaved(ess_key_old):
    # print('wtf readSaved')
    #ess_key_old = {'mEp': 'ep002', 'mSq': 'sq005', 'mSh': 'sh0602'}
    # print('ess_key_old',ess_key_old)
    ess_list = __work_list__()
    ESSdct = _EpSqSh_()
    ESSdct['dict'] = CTR_ESS_dict(ess_list, ess_key_old)['dict']
    return ESSdct
def readSaved_list(saved):
    # print('wtf readSaved')
    #saved = {'mEp': 'ep002', 'mSq': 'sq005', 'mSh': 'sh0602'}
    ess_list = __work_list__()
    keyESS = [ess for ess in _EpSqSh_()['keyESS'] if saved[ess]]
    ess = {}
    for lst in ess_list:
        if ratio_dikt_TF(keyESS, saved, lst):
            ess = lst
            break
    # {
    # 'Compose': [
    #     {'executor': ['Alexander Bosenko'],
    #      'frameRenge': '1-195', 'publish': 'v004', 'shot_id': 144579,
    #       'shot_name': 'ep006_sh0108', 'status': 'clsd', 'step': 'comp', 'step_id': 8, 'task': 'Compose',
    #       'task_id': 1314799}
    # ],
    # 'mEp': 'ep006',
    # 'mSh': 'sh0108',
    # 'mSh_id': 144579,
    # 'mSq': 'sq001'
    # }
    return ess

def create_ShotList(snt_filtr):
    # print('wtf create_ShotList')
    # snt_filtr = {'mSt': 'ip', 'mEx': 'Alla Vostrikova', 'mTs': 'all_task'}

    ess_list = __work_list__()
    EEE = []
    ess_mTs = fltr_ess_list(snt_filtr, ess_list)

    wt_list = [CRT_WT_Name(lst) for lst in ess_mTs]
    if wt_list:
        for i in wt_list:
            EEE = EEE + i
    return EEE
def create_TaskList():
    # print('wtf create_TaskList')
    ess_list = __work_list__()
    UserWork = _EpSqSh_()['UserWork']
    code = _EpSqSh_()['code']
    t = []
    for ess in ess_list:
        if UserWork in ess and ess[UserWork]:
            t = t + ess[UserWork]
    task = list(set([tsk[code['mTs']] for tsk in t]))

    return task



def creat_ShotPubIcon(workTaskName, fps=50, mTsName='comp'):
    # print('wtf creat_ShotPubIcon')
    # workTaskName = {'mEp': 'ep001', 'mSq': 'sq001', 'mSh': 'sh0101',
    #               'mTs': 'comp', 'mSt': 'pndng', 'mEx': 'ssergeev',
    #               'mPu': 'v011', 'mFR': '1-177', 'mVr': 'v011',
    #               'mVrdict': {'mVr': ['v011', 'v010', ..., 'v001'], 'id': 0},
    #               'mIc': '//omega/.../ep001_sh0101/v011/ep001_sh0101.comp..v011.00001.png'}
    ESS = {}

    iconFile = setFile('Terror-Night')
    if workTaskName:

        if mTsName == workTaskName['mTs']:
            ESS = workTaskName

        if ESS:
            FR = ESS['mFR'].split('-')[1]
            pub_file = re_keyFile(ESS, 'out_pub_file').replace(ESS['mVr'],ESS['mPu'])

            if not 'Terror-Night' in workTaskName['mIc']:
                pub_file = re_keyFile(ESS, 'out_work_file')

            for k in ESS:
                if k in pub_file:
                    pub_file = pub_file.replace(k, ESS[k])

            pub_fold = os.path.dirname(pub_file)
            if ESS['mVr'] == '' or not os.path.exists(pub_fold):
                return iconFile

            else:
                aeqq = ''.join(re.findall('%[0-9][0-9]d', pub_file))
                n = int(''.join(re.findall('[0-9][0-9]', aeqq)))
                iconFile = pub_file.replace(aeqq, str(int(int(FR) * fps / 100)).zfill(n))

                if not os.path.isfile(iconFile):
                    iconFile = setFile('Terror-Night')
                # n = len([i for i in pub_file if i == '#'])
                # iconFile = pub_file.replace('#####' , str( int(int(FR) * fps / 100)).zfill(n))

    return iconFile





def CRT_WT_Name(ess_mTs):
    # print('wtf CRT_WT_Name')
    # ess_mTs = {
    #     "Compose": [
    #         {"executor": ["Alisa Kostogarova"],
    #          "frameRenge": "1-44",
    #          "publish": "v003",
    #          "shot_id": 130139,
    #          "shot_name": "ep001_sh0203",
    #          "status": "clsd",
    #          "step": "comp",
    #          "step_id": 8,
    #          "task": "Compose",
    #          "task_id": 1198484
    #          }],
    #     "mEp": "ep001",
    #     "mSh": "sh0203",
    #     "mSh_id": 130139,
    #     "mSq": "sq002"
    # }
    keyESS = _EpSqSh_()['keyESS']  # ['mEp', 'mSq', 'mSh']
    code = _EpSqSh_()['code']  # {'mEp': 'episode', 'mSq': 'sequence', 'mSh':
    UserWork = _EpSqSh_()['UserWork']


    dctESSmin = {ess:ess_mTs[ess] for ess in keyESS}
    #dctESSmin =  {'mEp': 'ep001', 'mSq': 'sq001', 'mSh': 'sh0101'}
    task_dct = []
    task_name = []
    if UserWork in ess_mTs:
        task_dct = ess_mTs[UserWork]
        #task_dct =  [{'task':'comp','status': 'pndng', 'executor': 'ssergeev', 'publish': 'v011'},{'task':'key...]
        task_name = [tsk[code['mTs']] for tsk in ess_mTs[UserWork]]
        #task_name = ['comp' ,'key']

    WT = []
    if task_name:
        for tk_dct in [k for k in task_dct if k[code['mTs']] in task_name ]:

            wTask = {}

            for k in keyESS:
                wTask[k] = dctESSmin[k]
                ##{'mEp': 'ep001', 'mSq': 'sq001', 'mSh': 'sh0101'}
            for c in code:
                if code[c] in tk_dct:
                    wTask[c] = tk_dct[code[c]]
                #{'mSt': 'pndng', 'mEx': 'bzufarov', 'mPu': 'v004', 'mTs': 'comp'}

            # set Vers #################
            V = ctr_wt_mVr(wTask)
            for v in V:
                wTask[v] = V[v]
                #{'mVr': 'v011', 'mVrdict': {'mVr': ['v011', .... , 'v001'],'id': 0}}
            # set Icon ####################
            wTask['mIc'] = ctr_wt_mIc(wTask)
            #mIc': '//omega/non_tale/shots/ep001/ep...'}
            WT.append(wTask)

        
        # {
        #     'mEp': 'ep001', 'mSq': 'sq001', 'mSh': 'sh0101', 
        #     'mPr': 'non_tale', 'mTs': 'comp', 'mSt': 'pndng',
        #     'mEx': 'ssergeev', 'mPu': 'v011', 
        #     'mVr': 'v011', 'mVrdict': {'mVr': ['v011', .... , 'v001'],'id': 0},
        #     'mIc': '//omega/non_tale/shots/ep001/ep...'
        # }
        

    return WT
def ctr_wt_mVr(wTask):
    # print('wtf ctr_wt_mVr')
    mVrdict = {}
    mVr=''
    nkFile = re_keyFile(wTask,'nk_work_file')
    nkFold = os.path.dirname(nkFile)
    nkName = os.path.basename(nkFile).split('mVr')[0]

    if os.path.exists(nkFold):
        nkList = [nk.split('.nk')[0].split(nkName)[1]
                  for nk in filter(lambda i: i.endswith('.nk'), os.listdir(nkFold))
                  if nkName in nk]

        V = [i for i in {k for k in nkList} ]
        V.sort()
        V.reverse()
        if V:
            mVr = V[0]
            mVrdict={'mVr':V,'id':0}

    return {'mVr': mVr ,'mVrdict':mVrdict}

        # {'mVr':v006,'mVrdict':{'mVr':['v006', 'v005', 'v004', 'v003', 'v002', 'v001', 'v000`'],'id':0}}
def ctr_wt_mIc(wTask):
    # print('wtf ctr_wt_mIc')
    pub_file = re_keyFile(wTask,'out_pub_file')
    FR = wTask['mFR'].split('-')[1]

    aeqq = ''.join(re.findall('%[0-9][0-9]d', pub_file))
    n = int(''.join(re.findall('[0-9][0-9]', aeqq)))
    iconFile = pub_file.replace(aeqq, str(int(int(FR) * 50 / 100)).zfill(n))

    if wTask['mVr'] == '' or not os.path.exists(iconFile):
        iconFile = setFile('Terror-Night')

    return iconFile


def create_menuList(snt = 'mTs'):
    # print('wtf create_TaskList')
    ess_list = __work_list__()
    UserWork = _EpSqSh_()['UserWork']
    code = _EpSqSh_()['code']
    t = []
    for ess in ess_list:
        if UserWork in ess and ess[UserWork]:
            t = t + ess[UserWork]
    lst = list(set([tsk[code[snt]] for tsk in t]))

    return lst


'''