import maya.cmds as cmds
import mtoa.aovs as aovs


def do():
    aov_name = "crypto_object"
    aov = cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name).node
    crypto = cmds.ls("_aov_cryptomatte")[0] if cmds.ls("_aov_cryptomatte") else cmds.createNode("cryptomatte",
                                                                                                name="_aov_cryptomatte")
    cmds.connectAttr(crypto + ".outColor", aov + ".defaultValue", f=True)