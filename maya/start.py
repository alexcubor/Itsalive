# -*- coding: utf-8 -*-
import argparse
import os
import sys
import platform
import subprocess
from pathlib import Path

"""
Через этот скрипт запускается приложение с инструментарием Itsalive
"""


class App(object):
    def __init__(self):
        os.environ["TOOLS_PATH"] = str(Path(os.path.dirname(__file__)).parent.parent).replace("\\", "/")
        print("[It's alive] Start tools from " + os.environ["TOOLS_PATH"])
        print("[It's alive] Maya initialization...")
        os.environ["MAYA_VERSION"] = "2022"
        maya_locations = {"Windows": "C:/Program Files/Autodesk/Maya" + os.environ["MAYA_VERSION"]}
        os.environ["MAYA_LOCATION"] = maya_locations[platform.system()]
        put_env("PATH", os.environ["MAYA_LOCATION"] + "/bin")
        put_env("MAYA_MODULE_PATH", os.path.dirname(__file__))
        self.plugins_path = os.path.dirname(__file__) + "/plugins"
        self.project_name = self.get_project_name()
        self.install_cgru()
        self.install_studio_library()
        self.install_megascan_livelink()

    @staticmethod
    def install_cgru():
        cgru_version = "3.3.0"
        os.environ['CGRU_LOCATION'] = "C:/cgru." + cgru_version
        os.environ["MAYA_CGRU_LOCATION"] = os.environ['CGRU_LOCATION'] + "/plugins/maya"
        os.environ["MAYA_CGRU_MENUS_NAME"] = "CGRU"
        put_env("MAYA_SCRIPT_PATH", os.environ["MAYA_CGRU_LOCATION"] + "/mel/AETemplates")
        # put_env("MAYA_PLUG_IN_PATH", os.environ["MAYA_CGRU_LOCATION"] + "/mll/" + os.environ["MAYA_VERSION"])
        os.environ["XBMLANGPATH"] = os.environ["MAYA_CGRU_LOCATION"] + "/icons"
        # sys.path.append(os.environ["MAYA_CGRU_LOCATION"] + "/afanasy/python")
        # sys.path.append(os.environ["MAYA_CGRU_LOCATION"] + "/lib/python")
        put_env("PYTHONPATH", os.environ["MAYA_CGRU_LOCATION"] + "/afanasy")
        put_env("PYTHONPATH", os.environ["CGRU_LOCATION"] + "/lib/python")
        put_env("PYTHONPATH", os.environ['CGRU_LOCATION'] + "/afanasy/python")
        put_env("PYTHONPATH", os.environ['CGRU_LOCATION'] + "/plugins/maya")
        put_env("PYTHONPATH", os.environ['CGRU_LOCATION'] + "/plugins/maya/afanasy")
        print("[It's alive] Install CGRU " + cgru_version)

        def _fix():
            pyfile = os.environ["MAYA_CGRU_LOCATION"] + "/afanasy/__init__.py"
            if not os.path.isfile(pyfile):
                return
            pyread = open(pyfile, 'r')
            code = pyread.read()
            template = """cmd_buffer.append('-proj "%s"' % os.path.normpath(self.project))"""
            if template not in code:
                return  # Значит код уже исправлен
            codefix = code.replace(template, """cmd_buffer.append('-proj "%s"' % self.project)""")
            pyread.close()
            pyset = open(pyfile, 'w')
            pyset.write(codefix)
            pyset.close()
        _fix()

    @staticmethod
    def install_studio_library():
        put_env("PYTHONPATH", os.environ["TOOLS_PATH"] + "/Studio Library 2.9.6.b3/src")
        print("[It's alive] Install Studio Library 2.9.6.b3")

    def install_megascan_livelink(self):
        put_env("MAYA_MODULE_PATH", self.plugins_path + "/MSLiveLink")
        print("[It's alive] Install MegaScan LiveLink 7.0")

    @staticmethod
    def get_project_name():
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", help="Project.")
        args, unknown = parser.parse_known_args()
        if args.p:
            os.environ["PROJECT_NAME"] = args.p
        print("[It's alive] Project name: " + args.p)
        return args.p

    # Запуск Maya
    @staticmethod
    def run():
        maya_app = {'Windows': r'bin/maya.exe'}[platform.system()]
        app_path = os.path.join(os.getenv("MAYA_LOCATION"), maya_app)
        p = subprocess.Popen([app_path])
        wait = p.wait()
        exit(wait)


def put_env(env_var, val, at_begin=False):
    if os.getenv(env_var, None) is None:
        os.environ[env_var] = val
        return
    curr_vals = os.getenv(env_var, "").split(os.pathsep)
    norm_vals = [os.path.normpath(v) for v in curr_vals if v != ""]

    val = os.path.normpath(val)
    if val not in norm_vals:
        if at_begin:
            os.environ[env_var] = os.pathsep.join([val] + curr_vals)
        else:
            os.environ[env_var] = os.pathsep.join(curr_vals + [val])


if __name__ == '__main__':
    App().run()
