# -*- coding: utf-8 -*-
import argparse
import os
import sys
import platform
import subprocess
from pathlib import Path
import argparse

"""
Через этот скрипт запускается приложение с инструментарием Itsalive
"""


class App(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", help="Project name")
        self.args, self.unknown = parser.parse_known_args()
        os.environ["TOOLS_PATH"] = str(Path(os.path.dirname(__file__)).parent.parent).replace("\\", "/")
        self.app_location = os.getenv("TOOLS_PATH") + "/Arnold/Windows/maya2022-5.2.1"
        print("[It's alive] Start tools from " + os.environ["TOOLS_PATH"])
        print("[It's alive] Arnold initialization...")
        put_env("PATH", "c:/program files/autodesk/maya2022/bin")
        put_env("PATH", "c:/program files/autodesk/maya2022/plug-ins/xgen/bin")
        put_env("ARNOLD_PLUGIN_PATH", self.app_location + "/procedurals")


    # Запуск приложения
    def run(self):
        maya_app = {'Windows': r'bin/kick.exe'}[platform.system()]
        app_path = os.path.join(self.app_location, maya_app).replace("\\", "/")
        command = [app_path] + self.unknown
        print("[It's alive] Start command: ", command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout:
            print(line.strip())
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
