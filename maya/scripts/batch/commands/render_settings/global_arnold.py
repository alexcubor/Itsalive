import maya.cmds as cmds
import os


def do():
    # Global Arnold
    cmds.setAttr("defaultRenderGlobals.currentRenderer", "arnold", type="string")
    cmds.setAttr("defaultArnoldDriver.halfPrecision", 1)
    cmds.setAttr("defaultArnoldDriver.preserveLayerName", 1)
    cmds.setAttr("defaultArnoldDriver.autocrop", 1)
    cmds.setAttr("defaultArnoldDriver.mergeAOVs", 1)
    # cmds.setAttr("defaultArnoldRenderOptions.motion_blur_enable", 1)
    cmds.setAttr("defaultArnoldRenderOptions.abortOnError", 0)
    # Sampling and Ray Depth
    cmds.setAttr("defaultArnoldRenderOptions.AASamples", 8)
    cmds.setAttr("defaultArnoldRenderOptions.GITransmissionDepth", 4)
    cmds.setAttr("defaultArnoldRenderOptions.autoTransparencyDepth", 4)
    cmds.setAttr("defaultArnoldRenderOptions.enableAdaptiveSampling", 1)
    cmds.setAttr("defaultArnoldRenderOptions.AASamplesMax", 9)
    # Resolution
    cmds.setAttr("defaultResolution.width", 2048)
    cmds.setAttr("defaultResolution.height", 858)
    cmds.setAttr("defaultResolution.deviceAspectRatio", 2.387)
    cmds.setAttr("defaultResolution.pixelAspect", 1.000)
    # Path
    shot_path = cmds.file(q=True, sn=True).split("/light/")[0]
    shot_name = os.path.basename(shot_path)
    image_path = shot_path + "/render/maya/v001/<RenderLayer>/beauty/" + shot_name + "_beauty"
    cmds.setAttr("defaultRenderGlobals.imageFilePrefix", image_path, type="string")
