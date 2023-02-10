# -*- coding: utf-8 -*-
"""
Этот модуль посвящён всем скриптам, которые относятся к автосборке.
Со временем он может превратиться в папку с под-модулями.
"""

import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mm
import os
import sys
import lconfig
import glob
if lconfig.is_dev():
    from importlib import reload
    from importlib import reload
    reload(lconfig)


def assembly():
    task_fields = lconfig.task_fields(cmds.file(q=True, sn=True))
    if task_fields["task_activity_name"] == "anim":
        env_path = import_env()
        ref_nodes = get_meshes(pm.ls(pm.referenceQuery(env_path, n=True)))
        assign_shadow_matte(ref_nodes, "env_shadow_matte")
        mm.eval("MLdeleteUnused")
        cmds.inViewMessage(amg='- env.fbx импортирован, как референс\n- Ноды env расфасованы\n- На новую геометрию '
                               'назначен Shadow matte\n- На новой геометрии отключен Self shadow', pos='botCenter',
                           fade=1, fst=6000, fot=6000)
    if task_fields["task_activity_name"] == "light":
        if not pm.ls(type="reference"):
            import_assembl()
        import render
        from importlib import reload
        reload(render)
        render.RenderSetup().import_settings()
        cmds.delete(cmds.ls(type='unknown'))
        # Setup framerange scene
        cut_in = None
        cut_out = None
        if "cerebro" in sys.modules:
            from pycerebro import database
            from tentaculo.core import capp, config, clogger
            db = database.Database()
            db.connect_from_cerebro_client()
            root_tasks = db.root_tasks()
            def find(f, seq):
                # поиск объектов в списке
                for item in seq:
                    if f(item):
                        return item
            log = clogger.CLogger()
            config = config.ConfigLoader()
            task_id = config.task_for_file(capp.file_name(log))
            task = db.task(task_id)
            parent_task = db.task(task[2])
            for tag in db.task_tags(parent_task[1]):
                if "cut in" in tag:
                    cut_in = tag[-1]
                if "cut out" in tag:
                    cut_out = tag[-1]
                if cut_in and cut_out:
                    break
        else:
            main_cam = [x for x in pm.ls(type="camera") if ":cam" in x.name().lower()]
            main_cam = main_cam[0].parent(0) if main_cam else None
            if main_cam:
                main_cam.tx.set(lock=0)
                main_cam.ty.set(lock=0)
                main_cam.tz.set(lock=0)
                main_cam.rx.set(lock=0)
                main_cam.ry.set(lock=0)
                main_cam.rz.set(lock=0)
                all_keys = sorted(pm.keyframe(main_cam, q=True) or [])
                cut_in = all_keys[0]
                cut_out = all_keys[-1]
                main_cam.tx.set(lock=1)
                main_cam.ty.set(lock=1)
                main_cam.tz.set(lock=1)
                main_cam.rx.set(lock=1)
                main_cam.ry.set(lock=1)
                main_cam.rz.set(lock=1)
        pm.playbackOptions(min=cut_in, animationStartTime=cut_in, max=cut_out, animationEndTime=cut_out)
        cmds.inViewMessage(amg='- Assembl импортирован\n- Настройки рендера применены\n- Удалены unknown-ноды\n'
                           '- Установлен диапазон кадров',
                           pos='botCenter', fade=1, fst=6000, fot=6000)

def assembly_cerebro(task_info, arg):
    assembly()

def import_env():
    task_fields = lconfig.task_fields(cmds.file(q=True, sn=True))
    env_path = os.path.join(lconfig.project_path(), "episodes", task_fields["episode"], task_fields["scene"],
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

def import_assembl():
    task_fields = lconfig.task_fields(cmds.file(q=True, sn=True))
    assembl_dir = os.path.join(lconfig.project_path(), "episodes", task_fields["episode"], task_fields["scene"],
                            task_fields["shot"], "assembl").replace("\\", "/")
    print("[DEBUG] Find assembl scene", assembl_dir + "/*_B.mb")
    assembl_paths = glob.glob(assembl_dir + "/*_B.mb")
    if assembl_paths:
        print("[DEBUG] Found %s" % assembl_paths[-1])
        if os.path.isfile(assembl_paths[-1]):
            base_name = os.path.basename(assembl_paths[-1])
            name, ext = os.path.splitext(base_name)
            cmds.file(assembl_paths[-1], r=True, namespace=name)

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
