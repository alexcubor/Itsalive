import maya.cmds as cmds
import mtoa.aovs as aovs


def do():
    aov_name = "fresnel"
    aov = cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name).node
    cmds.setAttr(aov + ".type", 4)
    sampler = cmds.ls("samplerInfo1")[0] if cmds.ls("samplerInfo1") else cmds.createNode(
        "samplerInfo", name="samplerInfo1")
    range_invert = cmds.ls("aiRange_invert_sampler")[0] if cmds.ls("aiRange_invert_sampler") else cmds.createNode(
        "aiRange", name="aiRange_invert_sampler")
    cmds.setAttr(range_invert + ".outputMin", 1)
    cmds.setAttr(range_invert + ".outputMax", 0)
    cmds.connectAttr(sampler + ".facingRatio", range_invert + ".inputR", f=True)
    cmds.connectAttr(sampler + ".facingRatio", range_invert + ".inputG", f=True)
    cmds.connectAttr(sampler + ".facingRatio", range_invert + ".inputB", f=True)
    cmds.connectAttr(range_invert + ".outColor", aov + ".defaultValue", f=True)
