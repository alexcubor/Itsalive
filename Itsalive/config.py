# -*- coding: utf-8 -*-
"""
Описывает структуру проекта. Расшифровывает тип, деятельность, номер задачи и другие её параметры.
Необходимый модуль для работы с файлами и путями вне Cerebro, по скольку не у всех будет доступен этот менеджер задач.
"""

import json
import os
from pathlib import Path


class FilePath(object):
    def __init__(self, file_path):
        self.config = get_config_json()
        self.project_path = project_path().split("/")
        self.file_path = file_path.replace("\\", "/").split("/")
        self.file_relative_path = self.file_path[len(self.project_path):]
        self.cerebro_fields = None
        self.fields = None
        self.template = None
        self.version = None
        self.version_type = None
        templates = self.config["file_path"]

        # Вычисляем шаблон по полученному пути
        for template in templates:

            # Если в шаблоне путь не подошёл ни к версии ни к публикации, переходит к следующему шаблону
            valid_template = False
            for version_type in ["publish", "version"]:
                check_template_path = template[version_type].split("/")

                # 1) Отсеиваем шаблон пути, если количество вложенностей не совпадает. Самая быстрая проверка.
                def _check_length_path():
                    if len(check_template_path) != len(self.file_relative_path) - 1:
                        return False
                    return True

                check_length_path = _check_length_path()
                if not check_length_path:
                    continue

                # 2) Отсеиваем шаблон пути, если явные имена папок не совпадают
                def _check_names():
                    for num, folder in enumerate(check_template_path):
                        if "$" not in folder and folder != self.file_relative_path[num]:
                            return False
                    return True

                valid_folders = _check_names()
                if not valid_folders:
                    continue

                # Здесь мы определились, версия это и публикация
                valid_template = True
                self.version_type = version_type

            if not valid_template:  # Если в шаблоне путь не подошёл ни к версии ни к публикации,
                continue  # переходит к следующему шаблону

            # 3) Отсеиваем шаблон пути, если явно указана его активность и она не совпадает с активностью в пути.
            def _check_active():
                if template["task_activity"]:
                    for num, folder in enumerate(check_template_path):
                        if folder == "$(task_activity_name)" \
                                and template["task_activity"] != self.file_relative_path[num]:
                            return False
                return True

            valid_activity = _check_active()
            if not valid_activity:
                continue

            if valid_template:
                # Здесь шаблон точно определён, записываем его в переменные.
                if self.version_type == "version":
                    self.version = True
                    # self.template_path = self.template[self.version_type]
                else:
                    self.version = False
                self.template = template
                self.template_path = self.template[self.version_type].split("/")

        if self.template:
            # Осталось вычислить по полученному шаблону поля.
            self.cerebro_fields = {self.template["name"]: self.file_relative_path[-1]}
            for num, folder in enumerate(self.template_path):
                self.cerebro_fields[folder] = self.file_relative_path[num]

            # Поля получены, осталось расшифровать их значение. В Cerebro нет понятия шота, ассета или сущности,
            # там только есть понятие вложенности. По этому расшифровывать сущности мы будем сами, так как это
            # может быть полезно.
            self.fields = {}
            if "assets" in self.cerebro_fields:
                self.fields["task_type"] = "asset"
                self.fields["asset_type"] = self.cerebro_fields["$(url[2])"]
                self.fields["asset_name"] = self.cerebro_fields["$(url[3])"]
            if "episodes" in self.cerebro_fields:
                self.fields["task_type"] = "episode"
                self.fields["episode"] = self.cerebro_fields["$(url[2])"]
                self.fields["scene"] = self.cerebro_fields["$(url[3])"]
                self.fields["shot"] = self.cerebro_fields["$(url[4])"]
            self.fields["task_activity_name"] = self.cerebro_fields["$(task_activity_name)"]
            if self.version:
                self.fields["version_folder"] = self.cerebro_fields["work"]
            self.fields["name"] = self.cerebro_fields["$(task_name)"]


class Template(object):
    def __init__(self, template_dict):
        self.dict = template_dict
        self.task_type = get_task_type(self.dict["folder_path"])
        publish = self.path_format(self.dict["publish"]).split("/")
        self.publish_format_cerebro = "/".join([project_path()] + publish + [self.dict["name"]])
        self.publish_format = self.path_format(self.publish_format_cerebro)
        version = self.path_format(self.dict["version"]).split("/")
        self.version_format_cerebro = "/".join([project_path()] + version + [self.dict["name"]])
        self.version_format = self.path_format(self.version_format_cerebro)

    def path_format(self, template_path):
        if self.task_type in "asset":
            template_path = template_path.replace("$(url[2])", "{asset_type}")
            template_path = template_path.replace("$(url[3])", "{asset_name}")
        if self.task_type in "episode":
            template_path = template_path.replace("$(url[2])", "{episode}")
            template_path = template_path.replace("$(url[3])", "{scene}")
            template_path = template_path.replace("$(url[4])", "{shot}")
            template_path = template_path.replace("$(task_activity_name)", "{task_activity_name}")
            template_path = template_path.replace("$(task_name)", "{name}")
        return template_path

    def apply_fields_publish(self, fields):
        return self.publish_format.format(**fields)


def task_fields(path):
    return FilePath(path).fields


def task_cerebro_fields(path):
    return FilePath(path).cerebro_fields


def project_path():
    if os.getenv("PROJECT_NAME"):
        return os.path.join("//alpha/projects", os.getenv("PROJECT_NAME")).replace("\\", "/")
    else:
        config = get_config_json()
        project_path = config["project_path"][0]["paths"][0]
        return project_path

def library_path():
    return os.path.join(project_path(), "library").replace("\\", "/")


def get_task_type(path_or_template_path):
    if "assets" in path_or_template_path:
        return "asset"
    elif "episodes" in path_or_template_path:
        return "episode"
    else:
        return None


def find_template(dict_matches):
    templates = get_config_json()["file_path"]
    for template in templates:
        def _compare():
            for match in dict_matches:
                if dict_matches[match] != template[match]:
                    return False
            return True

        if _compare():
            return Template(template)
        else:
            return None


# Проверяет, находитесь ли вы в режиме разработчика.
def is_dev():
    if "/alpha/" in __file__.replace("\\", "/"):
        return False
    else:
        return True


def get_config_json():
    path_config = Path(os.path.abspath(__file__)).parent.joinpath("path_config.json")
    with open(path_config, "r") as read_file:
        data = json.load(read_file)
        return data
