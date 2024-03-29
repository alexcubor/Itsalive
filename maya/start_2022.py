# -*- coding: utf-8 -*-
import os
import sys
import platform
import subprocess
from pathlib import Path
import shutil
import re

"""
Через этот скрипт запускается приложение с инструментарием Itsalive
"""


class App(object):
    def __init__(self):
        os.environ["MAYA_VERSION"] = "2022"
        self.args = sys.argv[1:]
        if "-p" in sys.argv:
            self.project_name = sys.argv[sys.argv.index("-p") + 1]
            self.args.remove("-p"), self.args.remove(self.project_name)
        if "-app" in sys.argv:
            self.app_name = sys.argv[sys.argv.index("-app") + 1]
            self.args.remove("-app"), self.args.remove(self.app_name)
        else:
            self.app_name = "maya"
        os.environ["TOOLS_PATH"] = str(Path(os.path.dirname(__file__)).parent.parent).replace("\\", "/")
        print("[It's alive] Start tools from " + os.environ["TOOLS_PATH"])
        print("[It's alive] Maya initialization...")
        maya_locations = {"Windows": "C:/Program Files/Autodesk/Maya" + os.environ["MAYA_VERSION"],
                          "Darwin": f"/Applications/Autodesk/Maya{os.environ['MAYA_VERSION']}/Maya.app/Contents"}
        os.environ["MAYA_LOCATION"] = maya_locations[platform.system()]
        put_env("PATH", os.environ["MAYA_LOCATION"] + "/bin")
        put_env("MAYA_MODULE_PATH", os.path.dirname(__file__))
        self.plugins_path = os.path.dirname(__file__).replace("\\", "/") + "/plugins"
        self.install_studio_library()
        self.install_megascan_livelink()
        self.install_cgru()

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

            pyfile = os.environ["MAYA_CGRU_LOCATION"] + "/afanasy/maya_ui_proc.py"
            if not os.path.isfile(pyfile):
                return
            pyread = open(pyfile, 'r')
            code = pyread.read()
            template = "	labels.reverse()"
            if template not in code:
                return  # Значит код уже исправлен
            codefix = code.replace(template, "	#labels.reverse()")
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

    # Запуск Maya
    def run(self):
        maya_apps = {"Windows": "bin/%s.exe" % self.app_name,
                     "Darwin": "bin/" + self.app_name}
        maya_app = maya_apps[platform.system()]
        app_path = os.path.join(os.getenv("MAYA_LOCATION"), maya_app).replace("\\", "/")
        command = [app_path] + self.args
        print("[It's alive] Start command: ", command)
        p = subprocess.Popen(command)
        #for line in p.stdout:
        #    print(line.strip())
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
