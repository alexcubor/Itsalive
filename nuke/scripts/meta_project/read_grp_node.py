
import os, re
try:
    import nuke
    import nukescripts
except:s=1

def create_read_gr():
    r_gr = nuke.createNode('Group')
    r_gr['tile_color'].setValue(4278239231)
    r_gr.addKnob(nuke.File_Knob('file','file'))
    kn = nuke.PyScript_Knob('reload','reload',
                            'r_gr = nuke.thisNode()\n'
                            'import read_grp_node\n'
                            'read_grp_node.read_gr(r_gr)')
    r_gr.addKnob(kn)

    first = nuke.Int_Knob('first','first')
    last = nuke.Int_Knob('last','last')
    last.clearFlag(nuke.STARTLINE)
    r_gr.addKnob(first)
    r_gr.addKnob(last)

    r_gr.addKnob(nuke.Text_Knob('','',''))

    r_gr.begin()
    merg = nuke.nodes.Merge2()
    merg.setXYpos(100 , 200)
    merg['also_merge'].setValue('all')
    merg['metainput'].setValue('All')
    # merg['rangeinput'].setValue('All')

    CopyBBox = nuke.nodes.CopyBBox()
    CopyBBox.setXYpos(0,200)
    CopyBBox.setInput(0,merg)

    out_ = nuke.nodes.Output()
    out_.setXYpos(0,300)
    out_.setInput(0,CopyBBox)
    r_gr.end()
    return r_gr
def read_gr(r_gr ):
    #_delete Reads_###################
    for r in [i for i in r_gr.nodes() if i.Class()=='Read']:
        nuke.delete(r)
    Merge = [i for i in r_gr.nodes() if i.Class()=='Merge2'][0]

    #_beauty in_folds list _###################
    file = r_gr['file'].value()
    if file[-1] == '/':
        file = file[0:-1]
    in_folds = [path for path in os.listdir(file) if os.path.isdir(file + '/' + path)]

    if 'beauty' in in_folds :
        in_folds = [in_folds[in_folds.index('beauty')]] + [i for i in in_folds if 'beauty' not in i]

    in_folds = [k for k in in_folds if '.exr' in  ''.join( os.listdir(file + '/' + k))]
    #_create Reads _###################
    r_gr.begin()##############

    x,y = 0,0
    re_num = '\.[0-9][0-9][0-9][0-9].'
    re_set = '.%04d.'
    for k in range(len(in_folds )):
        r_file = ''
        fr_first = 1
        fr_last = 1

        img_list = os.listdir(file + '/' + in_folds[k])
        img_files = [ i for i in img_list if re.match('.*[0-9][0-9][0-9].exr.*',i) ]
        img_files.sort()

        if len(img_files)>1:
            f = img_files[0]
            rep = ''.join(re.findall(re_num, f))
            r_file = file + '/' + in_folds[k] + '/' + f.replace(rep, re_set)

            XXXX = img_files[0]
            # r_file = file + '/' + in_folds[k] +'/'+ XXXX.split('.')[0] +'.%04d.'+ XXXX.split('.')[-1]
        
            fr_first = int(img_files[0].split('.')[-2])
            fr_last = int(img_files[-1].split('.')[-2])
        else:
            if len(img_files):
                XXXX = img_files[0]
                r_file = file + '/' + in_folds[k] +'/'+ XXXX





        node = nuke.nodes.Read()
        node['file'].setValue(r_file)
        node['first'].setValue(fr_first)
        node['last'].setValue(fr_last)
        node['origfirst'].setValue(fr_first)
        node['origlast'].setValue(fr_last)
        node['postage_stamp'].setValue(0)
        node.setXYpos(x,y)
        x =x + 100
        Merge.setInput( k+3 , node)

    r_gr.end()##############

    r_gr.knob('first').setValue(r_gr.node('Read1')['first'].value())
    r_gr.knob('last').setValue(r_gr.node('Read1')['last'].value())
    r_gr.node('CopyBBox1').setInput(1,r_gr.node('Read1'))
    r_gr['label'].setValue(file.split('/')[-1]+'\n'+file.split('/')[-2])

    shot_name = '_'.join(list(set(re.findall('ep[0-9][0-9][0-9]', file))) +
                             list(set(re.findall('sh[0-9][0-9][0-9][0-9]', file))))
    r_gr['label'].setValue(shot_name + '\n' + file.split('/')[-1] + '\n' + file.split('/')[-2])