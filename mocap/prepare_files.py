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
from mocap import copy_fbx


def run(folder=None):
    args = sys.argv
    if not folder:
        folder = args[-1]
    # Конвертирует все mov-файлы в полученной папке в 24 кадра/сек в виде png-сиквенции
    convert_to_24fps.convert(str(folder))
    # Копирует fbx-скелет в шот
    copy_fbx.do(str(folder))


if __name__ == "__main__":
    run()
