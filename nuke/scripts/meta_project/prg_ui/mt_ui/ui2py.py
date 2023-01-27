import os,re
import sys, pprint
from pyside2uic import compileUi

path = 'C:/Users/bzufarov/Documents/Itsalive/nuke/scripts/meta_project/prg_ui/mt_ui'
path_to = 'C:/Users/bzufarov/Documents/Itsalive/nuke/scripts/meta_project/prg_ui'

ui_list = [i for i in filter(lambda i: i.endswith('.ui'), os.listdir(path))]

for it in ui_list:
    pyfile = open(path_to + '/' + it.replace('.ui', '.py'), 'w')
    compileUi(path + '/' + it, pyfile, False, 4, False)
    pyfile.close()

    print('ui_to_meta_____________________________________________',it)
print(path,'ui_to_meta_____________________________________________')