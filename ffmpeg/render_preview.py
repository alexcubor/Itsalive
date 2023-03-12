# -*- coding: utf-8 -*-
import subprocess
import sys
import argparse
import glob
import os
import shutil
import re
from pathlib import Path

try:
    import lconfig, sys
except:
    import sys

    sys.path.append(str(Path(__file__).parent.parent))
    import lconfig

"""
Собирает все рендер слои в один mov-файл
"""


def collect(project=None, episode=None, scene=None, shot=None, version=1):
    print("[It's Alive] Start script")
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="Project")
    parser.add_argument("-ep", help="Episode")
    parser.add_argument("-sc", help="Scene")
    parser.add_argument("-sh", help="Shot")
    parser.add_argument("-v", help="Version")
    args, unknown = parser.parse_known_args()
    if not project:
        project = args.p
    if not episode:
        episode = args.ep
    if not scene:
        scene = args.sc
    if not shot:
        shot = args.sh
    if args.v:
        version = int(args.v)
    sequence_paths = []
    projects_path = lconfig.projects_path()
    shot_dir = os.path.join(projects_path, project, "episodes", episode, scene, shot).replace("\\", "/")

    ## Find UE-exr
    #ue_dir = shot_dir + "/render/UE"
    #last_version = sorted(os.listdir(ue_dir))[-1]
    #ue_last_version_dir = ue_dir + "/" + last_version
    #start_frame = re.findall(r".(\d\d\d\d).", os.listdir(ue_last_version_dir)[0])[0]
    #filename = re.sub(r".\d\d\d\d.", ".%04d.", os.listdir(ue_last_version_dir)[0])
    #ue_exr = ue_last_version_dir + "/" + filename
    #sequence_paths.append(ue_exr)

    # Find maya-exr
    maya_dir = shot_dir + "/render/maya"
    last_version = sorted(os.listdir(maya_dir))[-1]
    last_version_dir = maya_dir + "/" + last_version
    start_frame = "0001"
    for layer_dir in [last_version_dir + "/" + x for x in os.listdir(last_version_dir)]:
        beauty_dir = layer_dir + "/" + "beauty"
        start_frame = re.findall(r".(\d\d\d\d).", os.listdir(beauty_dir)[0])[0]
        filename = re.sub(r".\d\d\d\d.", ".%04d.", os.listdir(beauty_dir)[0])
        maya_exr = beauty_dir + "/" + filename
        sequence_paths.append(maya_exr)

    ffmpeg_exe = str(Path((__file__)).parent.parent.parent.joinpath(r"ffmpeg\bin\ffmpeg.exe"))
    command = [ffmpeg_exe]
    for sequence in sequence_paths:
        command += ["-start_number", start_frame, "-apply_trc", "iec61966_2_1", "-i", os.path.normpath(sequence), "-vf", "colormatrix=bt709:bt601"]
    mov = shot_dir + "/preview/%s_render_v%03d.mov" % (shot, version)
    if not os.path.isdir(os.path.dirname(mov)):
        os.makedirs(os.path.dirname(mov))
    command += ["-r", "24", "-c:v", "libx264", "-y", mov]
    #command += ["-filter_complex", "[0:v]copy[out];[out]", "-c:v", "libx264", "-y", mov]
    print("Run command", " ".join(command))
    subprocess.run(command)
    if os.path.isfile(mov):
        print("[Itsalive] Успех! Превью сохранена в %s" % mov)
        #mov_name = os.path.basename(mov)
        #shutil.copyfile(mov, os.path.join(projects_path, project, "episodes", episode, "preview", re.sub(r"_v\d\d\d", "", mov_name.replace("render", "r"))))
    else:
        print("[Itsalive] Что то пошло не так!")


if __name__ == "__main__":
    collect()


# #Local test
# os.environ["PROJECT_NAME"] = "3033"
# episode = "ep01"
# ep_dir = os.path.join(lconfig.projects_path(), os.environ["PROJECT_NAME"], "episodes", episode).replace("\\", "/")
# for scene in os.listdir(ep_dir):
#     shot_dir = ep_dir + "/" + scene
#     if not os.path.isdir(shot_dir):
#         continue
#     for shot in os.listdir(shot_dir):
#         try:
#             collect(project=os.environ["PROJECT_NAME"], episode=episode, scene=scene, shot=shot, version=1)
#         except:
#             print("Not Find EXRs in " + shot)
