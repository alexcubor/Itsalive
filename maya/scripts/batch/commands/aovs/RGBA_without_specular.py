import maya.cmds as cmds
import mtoa.aovs as aovs


def get_light_groups():
    # loop over all light groups in the scene
    lights = cmds.ls(exactType=['pointLight', 'directionalLight', 'spotLight', 'areaLight', 'aiAreaLight',
                                'aiSkyDomeLight', 'aiMeshLight', 'aiPhotometricLight'])
    existing_light_groups = []
    for light in lights:
        light_group = cmds.getAttr(light + ".aiAov")
        if light_group != "" and not light_group in existing_light_groups:
            existing_light_groups.append(light_group)
    return existing_light_groups


def do():
    light_groups = get_light_groups()
    # Create light passes
    for lg in light_groups:
        aov_name = "light_" + lg
        aov = cmds.ls("aiAOV_" + aov_name)[0] if cmds.ls("aiAOV_" + aov_name) else aovs.AOVInterface().addAOV(aov_name).node
        cmds.setAttr(aov + ".lightPathExpression", "C(<RD>|<TD>)<L.'%s'>" % lg, type="string")
    # Delete unused light passes
    for aov in cmds.ls(type="aiAOV"):
        if "aiAOV_light_" in aov:
            if aov.split("aiAOV_light_")[-1] not in light_groups:
                cmds.delete(aov)