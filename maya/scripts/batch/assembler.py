# -*- coding: utf-8 -*-
"""
Главный скрипт автосборки. Ищет все скрипты в папке commands и запускает поочерёдно.
"""

import maya.cmds as cmds
from importlib import reload
import lconfig
from . import commands
if lconfig.is_dev():
    from importlib import reload
    reload(lconfig)


def assembly():
    command_list = sorted([x for x in dir(commands) if "." in x])
    # Run commands for all tasks
    for py_command in command_list:
        if py_command.split(".")[0] in ["prepare"]:
            command = "commands." + py_command + ".do()"
            exec(command)
            command_list.remove(py_command)
    # Run commands for "light" tasks
    task_fields = lconfig.task_fields(cmds.file(q=True, sn=True))
    if task_fields["task_activity_name"] == "light":
        for py_command in command_list:
            #print("commands." + py_command)
            #exec(reload("commands." + py_command))
            command = "commands." + py_command + ".do()"
            exec(command)
        cmds.file(force=True, save=1, options="v=0")
        cmds.inViewMessage(amg='- Assembl импортирован\n- Настройки рендера применены\n- Удалены unknown-ноды\n'
                               '- Установлен диапазон кадров',
                           pos='botCenter', fade=1, fst=6000, fot=6000)

def assembly_cerebro(task_info, arg):
    assembly()
