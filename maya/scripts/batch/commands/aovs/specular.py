import maya.cmds as cmds
import mtoa.aovs as aovs


def do():
    aov_name = "specular"
    cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name)