import sys
from PySide2.QtWidgets import QApplication
from bahMT import bah_mt
import os
# print(sys.path)
print(os.environ.get('PATH'))

#
if __name__ == '__main__':
    app = QApplication()
    window = bah_mt()
    window.show()

    print(os.path.dirname(__file__))
    sys.exit(app.exec_())

# nuke.pluginAddPath('C:/Users/bzufarov/Documents/Itsalive/nuke/scripts/meta_project')
# from imp import reload
# import bahMT
# reload(bahMT)
# from bahMT import bah_mt
# mw = bah_mt()
# #mw.show()
# nukescripts.registerWidgetAsPanel('bah_mt', 'bah_mt','com.aaa.bah_mt')
