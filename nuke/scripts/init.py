import nuke
import sys
import os


nuke.pluginAddPath(os.path.dirname(__file__) + "/meta_project")
from meta_project import bahMT
mw = bahMT.bah_mt()
nukescripts.registerWidgetAsPanel('bah_mt', 'bah_mt','com.aaa.bah_mt')