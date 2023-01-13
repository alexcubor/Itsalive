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
        self.preset_directory = os.path.join(config.library_path(), "maya", "presets")

    def import_settings(self):
        render_settings = self.preset_directory + "/render_settings.json"
        self.import_json(render_settings)

        # Установка путей под шот
        context = config.FilePath(cmds.file(q=True, sn=True))
        if context.fields:
            context.fields["task_activity_name"] = "render"
            name = context.fields["name"].rsplit(".", 1)[0]
            context.fields["name"] = "maya"
            image_path = config.Template(context.template).apply_fields_publish(context.fields) + "/v001/" + name
            #cmds.workspace(fileRule=['images', image_path])
            pm.Attribute("defaultRenderGlobals.imageFilePrefix").set(image_path)

        def _aov_uv():
            aov_uv = pm.ls("aiAOV_uv")[0] if pm.ls("aiAOV_uv") else None
            if aov_uv:
                if not aov_uv.defaultValue.connections():
                    utility = pm.ls("aiUtility1")[0] if pm.ls("aiUtility1") else pm.createNode("aiUtility", name="aiUtility1")
                    pm.connectAttr(utility.outColor, aov_uv.defaultValue)
                    pm.Attribute(utility.shadeMode).set(2)
                    pm.Attribute(utility.colorMode).set(5)
        _aov_uv()

        def _aov_crypto():
            aov_crypto_mat = pm.ls("aiAOV_crypto_material")[0] if pm.ls("aiAOV_crypto_material") else None
            if aov_crypto_mat:
                if not aov_crypto_mat.defaultValue.connections():
                    crypto = pm.ls("_aov_cryptomatte")[0] if pm.ls("_aov_cryptomatte") else pm.createNode("cryptomatte",
                                                                                               name="_aov_cryptomatte")
                    pm.connectAttr(crypto.outColor, aov_crypto_mat.defaultValue)
            aov_crypto_obj = pm.ls("aiAOV_crypto_object")[0] if pm.ls("aiAOV_crypto_object") else None
            if aov_crypto_obj:
                if not aov_crypto_obj.defaultValue.connections():
                    crypto = pm.ls("_aov_cryptomatte")[0] if pm.ls("_aov_cryptomatte") else pm.createNode("cryptomatte",
                                                                                               name="_aov_cryptomatte")
                    pm.connectAttr(crypto.outColor, aov_crypto_mat.defaultValue)
        _aov_crypto()

        def _aov_position():
            aov = pm.ls("aiAOV_position")[0] if pm.ls("aiAOV_position") else None
            if aov:
                if not aov.defaultValue.connections():
                    space_tr = pm.createNode("aiSpaceTransform", name="aiSpaceTransform_position")
                    pm.Attribute(space_tr.to).set(2)
                    pm.connectAttr(space_tr.outValue, aov.defaultValue)
                    state = pm.createNode("aiSpaceTransform", name="aiSpaceTransform_position")
                    pm.Attribute(space_tr.variable).set(3)
                    pm.connectAttr(state.outValue, space_tr.input)
                    filter = pm.createNode("aiAOVFilter", name="aiAOVFilter_closest")
                    pm.Attribute(filter.aiTranslator).set("closest")
                    pm.connectAttr(filter.message, aov.outputs[0].filter)
        _aov_position()


    @staticmethod
    def export_json(filepath):
        with open(filepath, "w+") as file:
            json.dump(renderSetup.instance().encode(None), fp=file, indent=2, sort_keys=True)

    @staticmethod
    def import_json(filepath):
        with open(filepath, "r") as file:
            renderSetup.instance().decode(json.load(file), renderSetup.DECODE_AND_OVERWRITE, None)
