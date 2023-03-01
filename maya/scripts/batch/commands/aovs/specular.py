import maya.cmds as cmds
import mtoa.aovs as aovs


def do():
    aov_name = "specular"
    aov = cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name).node
    cmds.setAttr(aov + ".lightGroups", 1)