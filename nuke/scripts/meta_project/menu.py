import nuke
import nukescripts

from imp import reload
import bahMT
reload(bahMT)
from bahMT import bah_mt
mw = bah_mt()
#mw.show()
nukescripts.registerWidgetAsPanel('bah_mt', 'bah_mt','com.aaa.bah_mt')
