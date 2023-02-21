import os
import glob
import maya.cmds as cmds
import lconfig
if lconfig.is_dev():
    from importlib import reload
    reload(lconfig)


def do():
    if not cmds.ls(type="reference"):
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
    cmds.delete(cmds.ls(type='unknown'))