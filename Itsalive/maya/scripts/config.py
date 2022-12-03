# -*- coding: utf-8 -*-
"""
Описывает структуру проекта. Расшифровывает тип, деятельность, номер задачи и другие её параметры.
Необходимый модуль для работы с файлами и путями вне Cerebro, по скольку не у всех будет доступен этот менеджер задач.
"""

import maya.cmds as cmds
import json
import os


class Task(object):
    def __init__(self):
        self.config = self.get_config_json()
        self.project_path = self.config["project_path"][0]["paths"][0]
        self.file_path = cmds.file(q=True, sn=True)
        self.file_relative_path = self.file_path.split(self.project_path + "/")[-1]
        self.task_type, self.task_id, self.task_activity_name, self.task_name = self.file_relative_path.split("/")

    @staticmethod
    def get_config_json():
        path_config = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                   "path_config.json")
        with open(path_config, "r") as read_file:
            data = json.load(read_file)
            return data


def task_data():
    return Task().__dict__


# Проверяет, находитесь ли вы в режиме разработчика.
def is_dev():
    if "Z:" in __file__:
        return False
    else:
        return True
