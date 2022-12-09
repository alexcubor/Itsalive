import subprocess
import glob
import os


def create_ma(directory):
    fbx = glob.glob(directory + "/*.fbx")
    if fbx:
        ma = fbx[0].replace(".fbx", ".ma")
        if os.path.isfile(ma):
            return
        command = "import pymel.core as pm; "
        command += "import maya.cmds as cmds; "
        command += "import maya.mel as mm; "
        command += "cmds.currentUnit(time='240fps'); "
        command += "cmds.file('%s', i=True); " % fbx[0]
        command += "cmds.select('Hips', r=1); "
        command += "mm.eval('hikCreateDefinition'); "
        # command += "mm.eval('select -r Hips'; "
        command += "mm.eval('setCharacterObject(\"Head\", \"Character1\", 15, 0)'); "
        command += "mm.eval('setCharacterObject(\"Hips\", \"Character1\", 1, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftArm\", \"Character1\", 9, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftFoot\", \"Character1\", 4, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftForeArm\", \"Character1\", 10, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftHand\", \"Character1\", 11, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftLeg\", \"Character1\", 3, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftShoulder\", \"Character1\", 18, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftToeBase\", \"Character1\", 16, 0)'); "
        command += "mm.eval('setCharacterObject(\"LeftUpLeg\", \"Character1\", 2, 0)'); "
        command += "mm.eval('setCharacterObject(\"Neck\", \"Character1\", 20, 0)'); "
        command += "mm.eval('setCharacterObject(\"Reference\", \"Character1\", 0, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightArm\", \"Character1\", 12, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightFoot\", \"Character1\", 7, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightForeArm\", \"Character1\", 13, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightHand\", \"Character1\", 14, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightLeg\", \"Character1\", 6, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightShoulder\", \"Character1\", 19, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightToeBase\", \"Character1\", 17, 0)'); "
        command += "mm.eval('setCharacterObject(\"RightUpLeg\", \"Character1\", 5, 0)'); "
        command += "mm.eval('setCharacterObject(\"Spine\", \"Character1\", 8, 0)'); "
        command += "mm.eval('setCharacterObject(\"Spine1\", \"Character1\", 23, 0)'); "
        command += "mm.eval('setCharacterObject(\"Spine2\", \"Character1\", 24, 0)'); "
        command += "mm.eval('setCharacterObject(\"Spine3\", \"Character1\", 25, 0)'); "
        command += "cmds.file(rename='%s'); " % ma
        command += "cmds.file(save=True); "
        subprocess.run([r"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe", "-c", command])
