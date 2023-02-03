try: import nuke
except: s=1
def reShfLight():
    node = nuke.createNode('NoOp')

    ch_list = list(set([
        c.split('.')[0]
        for c in node.channels()
    ]))
    name_key = [
        c.split('RGBA_')[1]
        for c in ch_list
        if 'RGBA_' in c
    ]
    name_key.sort()


    ch_dict = {}
    for n in name_key:
        cc = ''.join([
            i for i in filter(
                lambda i: i.endswith(n), ch_list
            )
        ])
        ch_dict[n]=cc

    x,y = node.xpos(),node.ypos()+24

    sh_none = nuke.nodes.Shuffle2()
    sh_none['in1'].setValue('none')
    sh_none.setXYpos(x,y+24)
    sh_none.setInput(0, node)

    #Merge2
    mrg = nuke.nodes.Merge2()
    mrg.setXYpos(x+165,y+504)
    mrg['operation'].setValue('plus')



    sh_cop = nuke.nodes.Shuffle2()

    nd_dict = {}
    id_mrg = 3
    for k in name_key:
        x = x+165+110
        #Dot1
        d1 = nuke.nodes.Dot()
        d1['label'].setValue('\n'+k)
        d1['note_font_size'].setValue(30)
        d1.setXYpos(x+34,y+52)
        d1.setInput(0, sh_none)
        #Shuffle2
        sh = nuke.nodes.Shuffle2()
        sh['postage_stamp'].setValue(1)
        sh['label'].setValue('[value in1]')
        sh.setXYpos(x,y+113)
        sh.setInput(0, d1)
        sh['in1'].setValue(ch_dict[k])
        #Grade
        gr = nuke.nodes.Grade()
        gr.setXYpos(x,y+240)
        gr.setInput(0, sh)
        gr['black_clamp'].setValue(0)
        gr['channels'].setValue('rgba')
        #Dot2
        d2 = nuke.nodes.Dot()
        d2.setXYpos(x+34,y+364)
        d2.setInput(0, gr)

        #text
        txt = nuke.nodes.Text2()
        txt['message'].setValue(k)
        txt['global_font_scale'].setValue(2)
        txt.setXYpos(x+55,y+360)
        txt.setInput(0, d2)
        txt['box'].setValue([
            0,0,txt.input(0).width(),txt.input(0).height()
        ])

        nd_dict[k]={'d1':d1,'sh':sh,'gr':gr,'d2':d2,'txt':txt}

        mrg.setInput(id_mrg, d2)
        id_mrg += 1

    cs = nuke.nodes.ContactSheet()
    cs.setXYpos(x,y+364+212)
    id_cs = 0
    for k in name_key:
        cs.setInput(id_cs, nd_dict[k]['txt'])
        id_cs += 1
    cs['width'].setValue(cs.input(0).width()*2)
    cs['height'].setValue(cs.input(0).height())
    cs['rows'].setValue(2)
    cs['roworder'].setValue('TopBottom')


    l = len(name_key)/2
    if int(l) < l:  ll = int(l)
    else:           ll = l
    cs['columns'].setValue(ll)








