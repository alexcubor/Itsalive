# -*- coding: utf-8 -*-
import subprocess
import sys
import glob
import os

"""
Конвертирует все mov-файлы в полученной папке в 25 кадров/сек в виде png-сиквенции
"""


def convert(directory):
    print("AAA", directory)
    argv = sys.argv
    if argv:
        directory = argv[0]
    for mov in glob.glob(directory + "/*.mov"):
        path_to_sequence = mov.rsplit(".", 1)[0]
        print(path_to_sequence)
        name_no_ext = path_to_sequence.replace("\\", "/").split("/")[-1]
        if not os.path.isdir(path_to_sequence):
            os.mkdir(path_to_sequence)
            subprocess.run([r"Z:\tools\ffmpeg\bin\ffmpeg.exe", "-i", mov] + ["-r", "25"] + [path_to_sequence + "/" + name_no_ext + ".%4d" + ".png"])
