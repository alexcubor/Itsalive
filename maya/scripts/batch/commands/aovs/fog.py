import maya.cmds as cmds
import mtoa.aovs as aovs


def do():
    aov_name = "fog"
    aov = cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name).node
    cmds.setAttr(aov + ".type", 4)
    state = cmds.ls("aiStateFloat_depth")[0] if cmds.ls("aiStateFloat_depth") else cmds.createNode(
        "aiStateFloat", name="aiStateFloat_depth")
    cmds.setAttr(state + ".variable", 5)
    cmds.connectAttr(state + ".outValue", aov + ".defaultValue", f=True)
