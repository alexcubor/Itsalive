import subprocess
import glob
import os


def create_ma(directory):
    fbx_files = glob.glob(directory + "/*.fbx")
    ma_files = []
    for num, fbx in enumerate(fbx_files):
        idx = num + 1
        ma = fbx.replace(".fbx", ".ma")
        if os.path.isfile(ma):
            ma_files.append(ma)
            continue
        command = "import pymel.core as pm; "
        command += "import maya.cmds as cmds; "
        command += "import maya.mel as mm; "
        command += "cmds.file(new=True, force=True); "
        command += "cmds.currentUnit(time='240fps'); "
        command += "cmds.file('%s', i=True); " % fbx
        command += "cmds.select('Hips', r=1); "
        command += "mm.eval('hikCreateDefinition'); "
        # command += "mm.eval('select -r Hips'; "
        command += "mm.eval('setCharacterObject(\"Head\", \"Character%s\", 15, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"Hips\", \"Character%s\", 1, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftArm\", \"Character%s\", 9, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftFoot\", \"Character%s\", 4, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftForeArm\", \"Character%s\", 10, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftHand\", \"Character%s\", 11, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftLeg\", \"Character%s\", 3, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftShoulder\", \"Character%s\", 18, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftToeBase\", \"Character%s\", 16, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"LeftUpLeg\", \"Character%s\", 2, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"Neck\", \"Character%s\", 20, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"Reference\", \"Character%s\", 0, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightArm\", \"Character%s\", 12, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightFoot\", \"Character%s\", 7, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightForeArm\", \"Character%s\", 13, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightHand\", \"Character%s\", 14, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightLeg\", \"Character%s\", 6, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightShoulder\", \"Character%s\", 19, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightToeBase\", \"Character%s\", 17, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"RightUpLeg\", \"Character%s\", 5, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"Spine\", \"Character%s\", 8, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"Spine1\", \"Character%s\", 23, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"Spine2\", \"Character%s\", 24, 0)'); " % idx
        command += "mm.eval('setCharacterObject(\"Spine3\", \"Character%s\", 25, 0)'); " % idx
        command += "cmds.file(rename='%s'); " % ma
        command += "cmds.file(save=True); "
        subprocess.run([r"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe", "-c", command])
        ma_files.append(ma)
    return ma_files
