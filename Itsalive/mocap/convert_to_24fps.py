# -*- coding: utf-8 -*-
import subprocess
import sys
import glob
import os
from pathlib import Path

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
        if not os.path.isdir(path_to_sequence):
            os.mkdir(path_to_sequence)
            ffmpeg_exe = str(Path((__file__)).parent.parent.parent.joinpath(r"ffmpeg\bin\ffmpeg.exe"))
            print(ffmpeg_exe)
            subprocess.run([ffmpeg_exe, "-i", mov] + ["-r", "24"] + [
                path_to_sequence + "/" + name_no_ext + ".%4d" + ".png"])
        sequence_folders.append(path_to_sequence)
    return sequence_folders
