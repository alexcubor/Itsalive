# -*- coding: utf-8 -*-
import re
import shutil
from pathlib import Path

try:
    import config, sys
except:
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    import config
from mocap import convert_to_24fps
from mocap import create_character_definition


def run(folder=None):
    args = sys.argv
    if not folder:
        folder = args[-1]
    # Конвертирует все mov-файлы в полученной папке в 24 кадра/сек в виде png-сиквенции
    sequence_folders = convert_to_24fps.convert(str(folder))
    # Настраивает fbx-скелет и сохраняет в MA
    maya_scenes = create_character_definition.create_ma(str(folder))
    # Перемещает содержимое в папку шота
    for path in sequence_folders + maya_scenes:
        folder = path.replace("\\", "/").split("/")[-1]
        group_names = re.match(".*(?P<episode>ep\w+).+(?P<scene>sc\w+).+(?P<shot>sh[0-9&a-z&A-Z]+)", folder)
        if group_names:
            template = config.find_template({"folder_path": "$(url[0])/episodes", "task_activity": ""})
            fields = group_names.groupdict()
            if "sc" not in fields["shot"]:
                fields["shot"] = fields["scene"] + "_" + fields["shot"]
            fields.update(
                {"project_path": config.project_path(), "task_activity_name": "mocap_data", "name": folder})
            direct_path = template.apply_fields_publish(fields)
            shutil.move(path, direct_path)
            print("[Itsalive] %s успех! Перенесён в %s" % (path, direct_path))
        else:
            print("[Itsalive] %s успех! Если хотите что бы обработанный файл или папка переместились в шоты, "
                  "укажите в его имени эпизод, сцену и шот. Например: eva_ep01_sc01_sh01.bla или "
                  "eva_ep01.sc01-sh01_vvv." % path)


if __name__ == "__main__":
    run()
