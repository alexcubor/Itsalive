import maya.cmds as cmds
import mtoa.aovs as aovs


def do():
    aov_name = "P"
    aov = cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name).node
    def _driver_32bit(aov):
        driver = cmds.ls("_32bitArnoldDriver")[0] if cmds.ls("_32bitArnoldDriver") else \
            cmds.createNode("aiAOVDriver", name="_32bitArnoldDriver")
        cmds.setAttr(driver + ".preserveLayerName", 1)
        cmds.setAttr(driver + ".exrTiled", 1)
        cmds.setAttr(driver + ".autocrop", 1)
        cmds.connectAttr(driver + ".message", aov + ".outputs[0].driver", f=True)

    _driver_32bit(aov)