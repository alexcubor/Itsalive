# -*- coding: utf-8 -*-
import maya.cmds as cmds
import pymel.core as pm
from importlib import reload
import config
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
        self.preset_directory = os.path.join(config.library_path(), "maya", "presets").replace("\\", "/")

    def import_settings(self):
        render_settings = self.preset_directory + "/render_settings.json"
        try:
            self.import_json(render_settings)
        except:
            print("[It's alive] Error import render_settings preset!")

        # Установка путей под шот
        context = config.FilePath(cmds.file(q=True, sn=True))
        if context.fields:
            context.fields["task_activity_name"] = "render"
            context.fields["name"] = "maya"
            image_path = config.Template(context.template).apply_fields_publish(context.fields) + "/v001/<RenderLayer>/<RenderPass>/" + context.fields["shot"] + "_<RenderPass>"
            #cmds.workspace(fileRule=['images', image_path])
            pm.Attribute("defaultRenderGlobals.imageFilePrefix").set(image_path)
            pm.Attribute("defaultArnoldRenderOptions.abortOnError").set(0)
            pm.Attribute("defaultArnoldRenderOptions.GITransmissionDepth").set(4)
            pm.Attribute("defaultArnoldRenderOptions.autoTransparencyDepth").set(4)
            pm.Attribute("defaultArnoldRenderOptions.plugin_searchpath").set("//alpha/tools/Arnold/Windows/maya2022-5.2.1/procedurals")

        def _setup_camera():
            for cam in cmds.ls(type="camera"):
                if ":cam" in cam.lower():
                    pm.Attribute(cam + ".renderable").set(1)
                    pm.Attribute(cam + ".aiUseGlobalShutter").set(0)
                    pm.Attribute(cam + ".locatorScale").set(25)
                else:
                    pm.Attribute(cam + ".renderable").set(0)
        _setup_camera()

        def _driver_32bit(aov):
            driver = pm.ls("_32bitArnoldDriver")[0] if pm.ls("_32bitArnoldDriver") else \
                pm.createNode("aiAOVDriver", name="_32bitArnoldDriver")
            pm.Attribute(driver.preserveLayerName).set(1)
            pm.Attribute(driver.exrTiled).set(1)
            pm.Attribute(driver.autocrop).set(1)
            pm.connectAttr(driver.message, pm.Attribute(aov.name() + ".outputs")[0].driver, f=True)

        def _aov_z():
            aov = pm.ls("aiAOV_Z")[0] if pm.ls("aiAOV_Z") else pm.createNode("aiAOV", name="aiAOV_Z")
            _driver_32bit(aov)
        _aov_z()

        def _aov_uv():
            aov_uv = pm.ls("aiAOV_uv")[0] if pm.ls("aiAOV_uv") else None
            if aov_uv:
                if not aov_uv.defaultValue.connections():
                    utility = pm.ls("aiUtility1")[0] if pm.ls("aiUtility1") else pm.createNode("aiUtility", name="aiUtility1")
                    pm.connectAttr(utility.outColor, aov_uv.defaultValue, f=True)
                    pm.Attribute(utility.shadeMode).set(2)
                    pm.Attribute(utility.colorMode).set(5)
        _aov_uv()

        def _aov_crypto():
            aov_crypto_mat = pm.ls("aiAOV_crypto_material")[0] if pm.ls("aiAOV_crypto_material") else None
            if aov_crypto_mat:
                if not aov_crypto_mat.defaultValue.connections():
                    crypto = pm.ls("_aov_cryptomatte")[0] if pm.ls("_aov_cryptomatte") else pm.createNode("cryptomatte",
                                                                                               name="_aov_cryptomatte")
                    pm.connectAttr(crypto.outColor, aov_crypto_mat.defaultValue, f=True)
            aov_crypto_obj = pm.ls("aiAOV_crypto_object")[0] if pm.ls("aiAOV_crypto_object") else None
            if aov_crypto_obj:
                if not aov_crypto_obj.defaultValue.connections():
                    crypto = pm.ls("_aov_cryptomatte")[0] if pm.ls("_aov_cryptomatte") else pm.createNode("cryptomatte",
                                                                                               name="_aov_cryptomatte")
                    pm.connectAttr(crypto.outColor, aov_crypto_obj.defaultValue, f=True)
        _aov_crypto()

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