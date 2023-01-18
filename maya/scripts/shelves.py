# -*- coding: utf-8 -*-
"""
Генерирует полки при каждом запуске Maya. Полезно, если художник случайно сломал полку.
"""

import maya.cmds as mc
import os
import config
if config.is_dev():
    from importlib import reload


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
    command = "import assembler; assembler.assembly()"
    if config.is_dev():
        command = "import assembler; from importlib import reload; reload(assembler); assembler.assembly()"
    shelf.addButton(label="Asmbl", icon="bag-dynamic-color.png", command=command)
    command = "import render_stats; wind = render_stats.Batch(); wind.show()"
    if config.is_dev():
        command = "import render_stats; from importlib import reload; reload(render_stats); wind = render_stats.Batch(); wind.show()"
    shelf.addButton(label="RStats", icon="minecraft-dynamic-color.png", command=command)
    command = "import render; render.RenderSetup().import_settings()"
    if config.is_dev():
        command = "import render; from importlib import reload; reload(render); render.RenderSetup().import_settings()"
    shelf.addButton(label="Settings", icon="camera-dynamic-color.png", command=command)
    shelf.addButton(label="Afanasy", icon="star-dynamic-color.png", command="import afanasy; ui = afanasy.UI(); ui.show()")
