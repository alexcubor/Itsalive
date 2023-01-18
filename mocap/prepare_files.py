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
    convert_to_24fps.convert(str(folder))
    # Настраивает fbx-скелет и сохраняет в MA
    create_character_definition.create_ma(str(folder))


if __name__ == "__main__":
    run()
