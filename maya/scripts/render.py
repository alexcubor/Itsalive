# -*- coding: utf-8 -*-
import maya.cmds as cmds
import pymel.core as pm
from importlib import reload
import lconfig
import json
import os
import maya.app.renderSetup.model.renderSetup as renderSetup
from PySide2 import QtCore, QtWidgets, QtGui


class RenderSetup(QtWidgets.QWidget):  # TODO Add exporter render settings for episode and sequence level
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setGeometry(500, 300, 260, 110)
        self.setWindowTitle("It's Render Settings")
        self.preset_directory = os.path.join(lconfig.library_path(), "maya", "presets").replace("\\", "/")

    def import_settings(self):
        render_settings = self.preset_directory + "/render_settings.json"
        try:
            pass#self.import_json(render_settings)
        except:
            print("[It's alive] Error import render_settings preset!")
        pm.Attribute("defaultArnoldRenderOptions.plugin_searchpath").set("//alpha/tools/Arnold/Windows/maya2022-5.2.1/procedurals")

        def _aov_position():
            aov = pm.ls("aiAOV_position")[0] if pm.ls("aiAOV_position") else None
            if aov:
                if not aov.defaultValue.connections():
                    space_tr = pm.PyNode("aiSpaceTransform_position") if pm.ls("aiSpaceTransform_position") else \
                        pm.createNode("aiSpaceTransform", name="aiSpaceTransform_position")
                    pm.Attribute(space_tr.to).set(2)
                    pm.connectAttr(space_tr.outValue, aov.defaultValue, f=True)
                    state = pm.PyNode("aiStateVector_position") if pm.ls("aiStateVector_position") else \
                        pm.createNode("aiStateVector", name="aiStateVector_position")
                    pm.Attribute(state.variable).set(3)
                    pm.connectAttr(state.outValue, space_tr.input, f=True)
                    filter = pm.PyNode("aiAOVFilter_closest") if pm.ls("aiAOVFilter_closest") else \
                        pm.createNode("aiAOVFilter", name="aiAOVFilter_closest")
                    pm.Attribute(filter.aiTranslator).set('closest')
                    pm.connectAttr(filter.message, pm.Attribute(aov.name() + ".outputs")[0].filter, f=True)
                    #_driver_32bit(aov)
        _aov_position()

        def _add_denoiser():
            denoiser = pm.PyNode("aiImagerDenoiserNoice1") if pm.ls("aiImagerDenoiserNoice1") else \
                        pm.createNode("aiImagerDenoiserNoice", name="aiImagerDenoiserNoice1")
            pm.connectAttr("aiImagerDenoiserNoice1.message", "defaultArnoldRenderOptions.imagers[0]", f=True)
            pm.Attribute(denoiser.variance).set(0.1)
            pm.Attribute(denoiser.outputSuffix).set("_denoise")
            aov_selection = "RGBA or diffuse_direct or diffuse_indirect or specular or sss"
            def _get_light_groups():
                # loop over all light groups in the scene
                lights = cmds.ls(exactType=['pointLight', 'directionalLight', 'spotLight', 'areaLight', 'aiAreaLight',
                                            'aiSkyDomeLight', 'aiMeshLight', 'aiPhotometricLight'])
                existing_light_groups = []
                for light in lights:
                    light_group = cmds.getAttr(light + ".aiAov")
                    if light_group != "" and not light_group in existing_light_groups:
                        existing_light_groups.append(light_group)
                return existing_light_groups
            light_groups = _get_light_groups()
            for lg in light_groups:
                aov_selection += " or RGBA_" + lg
            pm.Attribute(denoiser.layerSelection).set(aov_selection)
        # _add_denoiser() отключен, так как для персонажки плохо смотрится

        from batch import assembler
        reload(assembler)
        reload(assembler.commands)
        print(assembler)
        assembler.assembly()


    @staticmethod
    def export_json(filepath):
        with open(filepath, "w+") as file:
            json.dump(renderSetup.instance().encode(None), fp=file, indent=2, sort_keys=True)

    @staticmethod
    def import_json(filepath):
        with open(filepath, "r") as file:
            renderSetup.instance().decode(json.load(file), renderSetup.DECODE_AND_OVERWRITE, None)


def save_lights():
    pm.select("|lights")
    filepath = cmds.file(q=True, sn=True)
    shot_dir = filepath.split("/light/")[0]
    cmds.file(shot_dir + "/cache/lights.ma", force=True, options="v=0;", typ="mayaAscii", pr=1, es=1)