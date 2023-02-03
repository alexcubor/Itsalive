import subprocess
import glob
import os
import re
from pathlib import Path
try:
    import config, sys
except:
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    import config


def do(directory):
    fbx_files = glob.glob(directory + "/*.fbx")
    ma_files = []
    for num, fbx in enumerate(fbx_files):
        copy_fbx = fbx
        # Если в файле указаны теги шота, перемещает содержимое в папку шота
        folder = fbx.replace("\\", "/").split("/")[-1]
        group_names = re.match(".*(?P<episode>ep\w+).+(?P<scene>sc\w+).+(?P<shot>sh[0-9&a-z&A-Z]+)", folder)
        if group_names:
            template = config.find_template({"folder_path": "$(url[0])/episodes", "task_activity": ""})
            fields = group_names.groupdict()
            if "sc" not in fields["shot"]:
                fields["shot"] = fields["scene"] + "_" + fields["shot"]
            fields.update(
                {"project_path": config.project_path(), "task_activity_name": "mocap_data", "name": folder})
            copy_fbx = template.apply_fields_publish(fields)
        if group_names:
            print("[Itsalive] Успех! Файл сохранён в %s" % copy_fbx)
        else:
            print("[Itsalive] %s успех! Если хотите что бы обработанный файл переместился в шоты, "
                  "укажите в его имени эпизод, сцену и шот. Например: eva_ep01_sc01_sh01.bla или "
                  "eva_ep01.sc01-sh01_vvv." % copy_fbx)
        ma_files.append(copy_fbx)
    return ma_files
