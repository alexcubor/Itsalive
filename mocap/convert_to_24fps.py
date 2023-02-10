# -*- coding: utf-8 -*-
import subprocess
import sys
import glob
import os
import re
from pathlib import Path
try:
    import lconfig, sys
except:
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    import lconfig

"""
Конвертирует все mov-файлы в полученной папке в 24 кадров/сек в виде png-сиквенции
"""


def convert(directory=None):
    args = sys.argv
    if not directory:
        directory = args[-1]
    sequence_folders = []
    for mov in glob.glob(directory + "/*.mov"):
        path_to_sequence = mov.rsplit(".", 1)[0]
        name_no_ext = path_to_sequence.replace("\\", "/").split("/")[-1]
        # Если в файле указаны теги шота, перемещает содержимое в папку шота
        group_names = re.match(".*(?P<episode>ep\w+).+(?P<scene>sc\w+).+(?P<shot>sh[0-9&a-z&A-Z]+)", name_no_ext)
        if group_names:
            template = lconfig.find_template({"folder_path": "$(url[0])/episodes", "task_activity": ""})
            fields = group_names.groupdict()
            if "sc" not in fields["shot"]:
                fields["shot"] = fields["scene"] + "_" + fields["shot"]
            fields.update(
                {"project_path": lconfig.project_path(), "task_activity_name": "mocap_data", "name": name_no_ext})
            path_to_sequence = template.apply_fields_publish(fields)
        if os.path.isdir(path_to_sequence):
            print("[Itsalive] Секвенция %s уже существует!" % path_to_sequence)
            continue
        else:
            os.makedirs(path_to_sequence)
        ffmpeg_exe = str(Path((__file__)).parent.parent.parent.joinpath(r"ffmpeg\bin\ffmpeg.exe"))
        command = [ffmpeg_exe, "-i", mov] + ["-r", "24", "-q:v", "10"] + [os.path.normpath(path_to_sequence + "/" + name_no_ext + ".%4d" + ".jpg")]
        print("[It's alive] " + " ".join(command))
        subprocess.run(command)
        if group_names:
            print("[Itsalive] Успех! Секвенция сохранена в %s" % path_to_sequence)
        else:
            print("[Itsalive] %s успех! Если хотите что бы обработанная секвенция переместились в шоты, "
                  "укажите в его имени видео-файла эпизод, сцену и шот. Например: eva_ep01_sc01_sh01.bla или "
                  "eva_ep01.sc01-sh01_vvv." % path_to_sequence)
        sequence_folders.append(path_to_sequence)
    return sequence_folders
