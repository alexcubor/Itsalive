import maya.cmds as cmds


def do():
    for cam in cmds.ls(type="camera"):
        if ":cam" in cam.lower():
            cmds.setAttr(cam + ".renderable", 1)
            cmds.setAttr(cam + ".aiUseGlobalShutter", 0)
            cmds.setAttr(cam + ".locatorScale", 25)
        else:
            cmds.setAttr(cam + ".renderable", 0)