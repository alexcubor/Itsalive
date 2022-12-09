# -*- coding: utf-8 -*-
"""
Этот модуль посвящён всем скриптам, которые относятся к автосборке.
Со временем он может превратиться в папку с под-модулями.
"""

import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mm
import os
import config
if config.is_dev():
    from importlib import reload
    reload(config)


def assembly():
    env_path = import_env()
    ref_nodes = get_meshes(pm.ls(pm.referenceQuery(env_path, n=True)))
    assign_shadow_matte(ref_nodes, "env_shadow_matte")
    mm.eval("MLdeleteUnused")
    cmds.inViewMessage(amg='- env.fbx импортирован, как референс\n- Ноды env расфасованы\n- На новую геометрию '
                           'назначен Shadow matte\n- На новой геометрии отключен Self shadow', pos='botCenter',
                       fade=1, fst=6000, fot=6000)


def import_env():
    task_fields = config.task_fields(cmds.file(q=True, sn=True))
    env_path = os.path.join(config.project_path(), "episodes", task_fields["episode"], task_fields["scene"],
                            task_fields["shot"], "cache", task_fields["shot"] + "_env.fbx")
    print("[DEBUG] Find cache + %s" % env_path)
    if os.path.isfile(env_path):
        try:
            cmds.referenceQuery(env_path, filename=True)
        except:
            cmds.file(env_path, reference=True)

        node_env = pm.createNode("transform", name="env") if not pm.ls("env") else pm.ls("env")[0]
        node_env_lights = pm.createNode("transform", name="env_lights") \
            if not pm.ls("env_lights") else pm.ls("env_lights")[0]
        ref_nodes = cmds.referenceQuery(env_path, n=True)
        for root_node in pm.ls(assemblies=True):
            if root_node.name() in ref_nodes:
                children = pm.listRelatives(root_node, c=True)
                if children is None:
                    pm.parent(root_node, node_env)
                else:
                    if pm.nodeType(children[0]) in ["aiAreaLight", "aiSkyDomeLight", "aiPhotometricLight",
                                                    "aiLightPortal", "ambientLight", "directionalLight", "pointLight",
                                                    "spotLight", "areaLight"]:
                        pm.parent(root_node, node_env_lights)
                    else:
                        pm.parent(root_node, node_env)
    return env_path


def assign_shadow_matte(meshes, shader_name):
    node = pm.ls(shader_name)
    if not node:
        shader_node = pm.createNode("aiShadowMatte", name=shader_name)
        print("[DEBUG] Shadow matte created successfully!")
    else:
        shader_node = node[0]
        pm.warning("[DEBUG] Shadow matte already exist!")
    for mesh in meshes:
        mesh.aiSelfShadows.set(0)
        pm.select(mesh, r=1)
        pm.hyperShade(assign=shader_node)


def get_meshes(nodes):
    meshes = []
    for node in pm.ls(nodes):
        if node.type() == "transform":
            children = [n for n in pm.listRelatives(node, c=True) if n.type() == "mesh"]
            meshes += children
    return meshes
