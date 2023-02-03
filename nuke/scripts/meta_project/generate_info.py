import glob, re
from mt_root import root
from fnk_wtf import repl
from nuke.scripts.meta_project.rwInfo import info_wright

def gnrt_info(prj_name, path):
    # prj_name = root()['prj']['iPr']
    info_wright(prj_name,scan(path))
def scan(path):
    print('scan()')
    p_re = root()['p_re']
    prj_k = root()['key']

    lst = []
    for found in glob.glob(path.format(EP='*', SC='*', SH='*')):
        found_l = re.findall('\w+\d+', found)
        lst.append(found_l)
        # found_l = ['3033', 'ep01', 'sc05', 'sc05_sh020']

    prj_list = []
    for l in lst:
        dd = {
            k: ''.join(re.findall(p_re[k], i))
            for i in l
            for k in prj_k
            if re.match('.*' + p_re[k], i)
        }
        if len(dd) == len(prj_k):
            prj_list.append(dd)
        # [{'iEp': 'ep00', 'iSc': 'sc00', 'iSh': 'sh000'}, {'i
    return prj_list

prj_name = root()['prj']['iPr']
path = repl(root()['file']['prj'], root()['scn'])
print(path)
print(scan(path))
gnrt_info(prj_name, path)