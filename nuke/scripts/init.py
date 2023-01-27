import nuke
import sys
import os


nuke.pluginAddPath(os.path.dirname(__file__) + "/meta_project")
from imp import reload
import bahMT
reload(bahMT)
from bahMT import bah_mt
mw = bah_mt()
#mw.show()
nukescripts.registerWidgetAsPanel('bah_mt', 'bah_mt','com.aaa.bah_mt')