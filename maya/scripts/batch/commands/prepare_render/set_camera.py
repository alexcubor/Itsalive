import maya.cmds as cmds


def do():
    for cam in cmds.ls(type="camera"):
        if ":cam" in cam.lower():
            cmds.setAttr(cam + ".renderable", 1)
            cmds.setAttr(cam + ".aiUseGlobalShutter", 0)
            cmds.setAttr(cam + ".locatorScale", 25)
            transform = cmds.listRelatives(cam, p=1)[0]
            try:
                cmds.setAttr(transform + ".tx", lock=True)
                cmds.setAttr(transform + ".ty", lock=True)
                cmds.setAttr(transform + ".tz", lock=True)
                cmds.setAttr(transform + ".tx", lock=True)
                cmds.setAttr(transform + ".ty", lock=True)
                cmds.setAttr(transform + ".tz", lock=True)
            except:
                pass

        else:
            cmds.setAttr(cam + ".renderable", 0)
