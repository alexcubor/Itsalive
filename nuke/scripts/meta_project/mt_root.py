import re
import getpass

def root():
    root = {
        'prj': {
            'iPr': '3033',
            'iEp': 'ep00',
            'iSc': 'sc00',
            'iSh': 'sh000',
            'iVr': 'v000'
        },
        'p_re': {'iEp': '', 'iSc': '', 'iSh': '','iVr': ''},
        'scn': {
            'iPr': '3033',
            'iEp': '{EP}',
            'iSc': '{SC}',
            'iSh': '{SH}',
        },
        'key': ['iEp', 'iSc', 'iSh'],
        'wtn': {'iPr': '', 'iEp': '', 'iSc': '', 'iSh': '', 'iVr': '', 'iVrlist': [], 'iSel': '', 'iUr': ''},
        'dict': {
            'iEp': {'snt': [''], 'id': 0},
            'iSc': {'snt': [''], 'id': 0},
            'iSh': {'snt': [''], 'id': 0}
        },
        'file': {
            'prj': '//alpha/projects/iPr/episodes/iEp/iSc/iSc_iSh',
            'nk': 'comp/nuke/iSc_iSh_comp_iVr.nk',
            'nk_out': 'review/iSc_iSh_comp_iVr.mov',
            'fx': 'render/fx/iVr',
            'render': 'render/maya/iVr',
            'UE': 'render/UE/iVr',
            'lastESS': 'C:/Users/iUr/Documents/lastESS',
            'cam': 'cache'

        }
    }

    root['wtn']['iUr'] = getpass.getuser()

    prj = root['prj']
    p_re = root['p_re']
    for k in p_re:
        root['p_re'][k] = \
            prj[k][0: -len(re.findall('[0-9]', prj[k]))] + \
            ''.join(['[0-9]' for i in re.findall('[0-9]', prj[k])])

    return root


def repl(file = '', prj = {}):
    for p in prj:
        if p in file:
            file = file.replace(p, prj[p])
    return file
# print(root()['p_re'])
# {
#   'prj': {
#       'iPr': '3033',
#       'iEp': 'ep00',
#       'iSc': 'sc00',
#       'iSh': 'sh000',
#       'iVr': 'v000'},
#       'keyESS': ['iEp', 'iSc', 'iSh'],
#       'dict': {
#           'iEp': {'snt': [''], 'id': 0},
#           'iSc': {'snt': [''], 'id': 0},
#           'iSh': {'snt': [''], 'id': 0}},
#           'file': {
#               'nk': '//alpha/projects/iPr/episodes/iEp/iSc/iSc_iSh/comp/nuke/iEp_iSc_iSh_comp_iVr.nk',
#               'nk_out': '//alpha/projects/iPr/episodes/iEp/iSc/iSc_iSh/comp/out/iVr/iEp_iSc_iSh_comp_iVr.%04d.png'},
#        'p_re': {'iEp': 'ep[0-9][0-9]', 'iSc': 'sc[0-9][0-9]', 'iSh': 'sh[0-9][0-9][0-9]'}}