# -*- coding: utf-8 -*-
"""
Генерирует полки при каждом запуске Maya. Полезно, если художник случайно сломал полку.
"""

import maya.cmds as mc
import os
import lconfig
import re


def _null(*args):
    pass


class _shelf():
    '''A simple class to build shelves in maya. Since the build method is empty,
    it should be extended by the derived class to build the necessary shelf elements.
    By default it creates an empty shelf called "customShelf".'''

    def __init__(self, name="customShelf", iconPath=""):
        self.name = name
        self.iconPath = iconPath

        self.labelBackground = (0, 0, 0, 0)
        self.labelColour = (.9, .9, .9)

    def addButton(self, label, icon="commandButton.png", command="", doubleCommand=""):
        '''Adds a shelf button with the specified label, command, double click command and image.'''
        mc.setParent(self.name)
        if self.iconPath:
            icon = os.path.join(self.iconPath, icon)

        mc.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand, imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour)

    def addMenuItem(self, parent, label, command=_null, icon=""):
        '''Adds a shelf button with the specified label, command, double click command and image.'''
        if icon:
            icon = self.iconPath + icon
        return mc.menuItem(p=parent, l=label, c=command, i="")

    def addSubMenu(self, parent, label, icon=None):
        '''Adds a sub menu item with the specified label and icon to the specified parent popup menu.'''
        if icon:
            icon = self.iconPath + icon
        return mc.menuItem(p=parent, l=label, i=icon, subMenu=1)

    def build(self):
        '''Checks if the shelf exists and empties it if it does or creates it if it does not.'''
        if mc.shelfLayout(self.name, ex=1):
            if mc.shelfLayout(self.name, q=1, ca=1):
                for each in mc.shelfLayout(self.name, q=1, ca=1):
                    mc.deleteUI(each)
        else:
            mc.shelfLayout(self.name, p="ShelfLayout")


"""
Создание полок
"""


def create():
    shelf = _shelf()
    shelf.name = "Itsalive"
    shelf.build()
    command = "import studiolibrary; studiolibrary.main()"
    shelf.addButton(label="Library", icon="cube-dynamic-color.png", command=command)
    command = rebuild_command("from batch import assembler; assembler.assembly()")
    shelf.addButton(label="Asmbl", icon="bag-dynamic-color.png", command=command)
    command = rebuild_command("from batch.assembler import commands; commands.prepare.frame_range.do()")
    double_command = rebuild_command("from batch.assembler import commands; commands.prepare.frame_range.do(mode='camera')")
    shelf.addButton(label="FrameR", icon="next-dynamic-color.png", command=command, doubleCommand=double_command)
    command = rebuild_command("import render_stats; wind = render_stats.Batch(); wind.show()")
    shelf.addButton(label="RStats", icon="minecraft-dynamic-color.png", command=command)
    #command = rebuild_command("import render; render.RenderSetup().import_settings()")
    #shelf.addButton(label="Settings", icon="camera-dynamic-color.png", command=command)
    shelf.addButton(label="Batch", icon="star-dynamic-color.png", command="import maya.cmds as cmds; cmds.delete(cmds.ls(type='unknown')); import afanasy; ui = afanasy.UI(); ui.show()")
    command = rebuild_command("import af_meArnoldRender; af_meArnoldRender=af_meArnoldRender.meArnoldRender()")
    shelf.addButton(label="Arnold", icon="star-dynamic-color.png", command=command)
    command = rebuild_command("import render; render.save_lights()")
    shelf.addButton(label="Save", icon="bulb-dynamic-color.png", command=command)


def rebuild_command(command):
    libname = re.findall("import (\w+);", command)[0]
    if lconfig.is_dev():
        return command.replace("import %s;" % libname, "import %s;" % libname + " from importlib import reload; reload(%s);" % libname)
    else:
        return command