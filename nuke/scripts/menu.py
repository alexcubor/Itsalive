import sys
import os.path
import nuke
import nukescripts




from imp import reload
import GL_script
reload(GL_script)


toolbar = nuke.menu("Nodes")
menu = toolbar.addMenu("GL", icon="bah_rnd.png")
menu.addCommand("prj_folder", 'GL_script.GL_S("prj_folder")')
menu.addCommand("write", 'GL_script.GL_S("write")')
menu.addCommand("mov", 'GL_script.GL_S("mov")')
menu.addCommand("out", 'GL_script.GL_S("out")','ctrl+r')
menu.addCommand("render", 'GL_script.GL_S("render")')
menu.addCommand("camera", 'GL_script.GL_S("camera")')


# .addCommand('Atmosphere', 'nuke.createNode("Atmosphere")', icon='A_atmosphere.png')


nuke.knobDefault("Shuffle.postage_stamp", "true") 
if nuke.NUKE_VERSION_MAJOR > 11: 
    nuke.knobDefault("Shuffle.label",'[value in1]') 
else: 
    nuke.knobDefault("Shuffle.label",'[value in]')
