# F = '//omega/koshchey/3_post/sq111/sq111_sh0040/comp/out/v006/sq111_sh0040_comp_v006.%05d.png'


import nuke, nukescripts
import os, re , string
# X:/BABA_YAGA/SHOTS/seq068/seq068_0490/comp/v001/seq068_sc0490_comp_v001.%04d.jpg
def GL_S(comand=''):
    prj = {
        '|-Pj-|': 'x:/BABA_YAGA/SHOTS', 
        '|-Cm-|': 'M:/cache/BABA_YAGA/SHOTS', 
        '|-Wt-|': 'comp', 
        '|-Sq-|': '000',
        '|-Sh-|': '0000', 
        '|-Vc-|': '000',
        'pFc': '%04d.jpg', 
        'pFm': 'mov'
    }
    name = os.path.basename(nuke.root().name())

    prj['|-Sq-|'], prj['|-Sh-|'], prj['|-Vc-|'] = \
        [
            ''.join(re.findall('[0-9]', k))
            for k in name.split('.')[0].split('_')
            if re.findall('[0-9]', k)
        ]
    if len(name.split('_')[0]) > 6:
        prj['|-Sq-|'] = name.split('_')[0].split('seq')[1]

    if comand == 'write':
        write = {
            'file': '|-Pj-|/seq|-Sq-|/seq|-Sq-|_|-Sh-|/|-Wt-|/v|-Vc-|/seq|-Sq-|_sc|-Sh-|_|-Wt-|_v|-Vc-|.%04d.jpg',
            'file_type': 'jpeg',
            '_jpeg_quality':1,
            '_jpeg_sub_sampling':'4:4:4'
        }
        write['file'] = repl(write['file'], prj)
        write_node(write)
    elif comand == 'mov':
        mov = {
            'file': '|-Pj-|/seq|-Sq-|/seq|-Sq-|_|-Sh-|/|-Wt-|/seq|-Sq-|_sc|-Sh-|_|-Wt-|_v|-Vc-|.mov',
            'colorspace': 'sRGB',
            'file_type': 'mov',
            'mov_prores_codec_profile': 'ProRes 4:2:2 LT 10-bit'
        }
        mov['file'] = repl(mov['file'], prj)
        write_node(mov)
    elif comand == 'out':
        out = {'file': '|-Pj-|/seq|-Sq-|/seq|-Sq-|_|-Sh-|/|-Wt-|/v|-Vc-|/'}
        out['file'] = repl(out['file'], prj)
        # print(out)
        path = os.path.dirname(out['file'])
        Import_(path)
        return
    elif comand == 'render':
        prj['|-Wt-|'] = 'render'
        render = {'file': '|-Pj-|/seq|-Sq-|/seq|-Sq-|_|-Sh-|/|-Wt-|/'}
        render['file'] = repl(render['file'], prj)
        path = render['file'] + \
               max(
                   [
                       k for k in os.listdir(render['file'])
                       if re.match('V[0-9][0-9]',k)
                   ]
               )
        Import_(path)
        return
    elif comand == 'prj_folder':
        prj_folder = {'file': '|-Pj-|/seq|-Sq-|/seq|-Sq-|_|-Sh-|'}
        prj_folder['file'] = repl(prj_folder['file'], prj)
        path = prj_folder['file']
        print(path)
        if os.path.exists(path):
            print(path)
            os.startfile(path.replace('/', '\\'))
        else:
            return
    elif comand == 'camera':
        prj['|-Wt-|'] = 'camera'
        camera = {'file': '|-Cm-|/seq|-Sq-|/seq|-Sq-|_|-Sh-|/|-Wt-|/|-Wt-|.abc','name':'seq|-Sq-|_sc|-Sh-|'}
        camera['file'] = repl(camera['file'], prj)
        camera['name'] = repl(camera['name'], prj)

        path = camera['file']
        name = camera['name']
        print(path,name)
        if os.path.exists(path):
            print(path)
            ImpCam_koshchey(path,name)
        else:
            return
    else:
        return

def write_node(w_dict = {}):
    w_node = nuke.createNode('Write')
    for d in w_dict:
        w_node[d].setValue(w_dict[d])
    return w_node

def repl(file = '', prj = {}):
    for p in prj:
        if p in file:
            file = file.replace(p, prj[p])
    return file

def Import_(path):
    print(path)
    try:
        os.system( 'echo ' + path + '| clip' )
        nuke.nodePaste(nukescripts.cut_paste_file())
        os.system('echo off | clip')
    except: q=1    

def ImpCam_koshchey(path,name):
    Ca = nuke.createNode('Camera2')
    Ca['read_from_file'].setValue(True)
    Ca['frame_rate'].setValue(24)
    Ca['file'].setValue(path)
    Ca['label'].setValue('cam_' + name)
    Ca['read_from_file'].setValue(False)





























