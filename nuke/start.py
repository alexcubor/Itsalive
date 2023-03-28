# -*- coding: utf-8 -*-
import argparse
import os
import sys
import platform
import subprocess
from pathlib import Path

"""
Через этот скрипт запускается Приложение с инструментарием Itsalive
"""


class App(object):
    def __init__(self):
        os.environ["TOOLS_PATH"] = str(Path(os.path.dirname(__file__)).parent.parent).replace("\\", "/")
        print("[It's alive] Start tools from " + os.environ["TOOLS_PATH"])
        print("[It's alive] Nuke initialization...")
        self.location = {"Windows": "C:/Program Files/Nuke13.2v5",
                         "Darwin": "/Applications/Nuke13.1v1"}[platform.system()]
        try:
            self.install_cgru()
        except:
            pass

    @staticmethod
    def install_cgru():
        cgru_version = "3.3.0"
        os.environ['CGRU_LOCATION'] = {"Windows": "C:/cgru." + cgru_version}[platform.system()]
        put_env("NUKE_PATH", os.environ['CGRU_LOCATION'] + "/plugins/nuke")
        put_env("NUKE_PATH", os.path.dirname(__file__))
        put_env("NUKE_CGRU_PATH", os.environ['CGRU_LOCATION'] + "/plugins/nuke")
        put_env("PYTHONPATH", os.environ['NUKE_CGRU_PATH'])
        put_env("PYTHONPATH", os.environ["NUKE_CGRU_PATH"] + "/afanasy")
        put_env("PYTHONPATH", os.environ["CGRU_LOCATION"] + "/lib/python")
        put_env("PYTHONPATH", os.environ['CGRU_LOCATION'] + "/afanasy/python")
        put_env("PYTHONPATH", os.environ['CGRU_LOCATION'] + "/plugins/nuke")
        put_env("PYTHONPATH", os.environ['CGRU_LOCATION'] + "/plugins/nuke/scripts")
        print("[It's alive] Install CGRU " + cgru_version)

    @staticmethod
    def get_project_name():
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", help="Project.")
        args, unknown = parser.parse_known_args()
        if args.p:
            os.environ["PROJECT_NAME"] = args.p
        print("[It's alive] Project name: " + args.p)
        return args.p

    # Запуск приложения
    def run(self):
        app_name = {'Windows': 'Nuke13.2.exe', "Darwin": "Nuke13.1v1.app/Contents/MacOS/Nuke13.1"}[platform.system()]
        app_path = os.path.join(self.location, app_name)
        p = subprocess.Popen([app_path, "--nukex"])
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
