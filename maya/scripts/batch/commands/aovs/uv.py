import maya.cmds as cmds
import mtoa.aovs as aovs


def do():
    aov_name = "uv"
    aov = cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name).node
    utility = cmds.ls("aiUtility1")[0] if cmds.ls("aiUtility1") else cmds.createNode("aiUtility", name="aiUtility1")
    cmds.connectAttr(utility + ".outColor", aov + ".defaultValue", f=True)
    cmds.setAttr(utility + ".shadeMode", 2)
    cmds.setAttr(utility + ".colorMode", 5)

    cmds.setAttr(aov + ".enabled", 0)