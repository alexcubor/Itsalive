import sys
import pymel.core as pm


def do():
    cut_in = 0
    cut_out = 0
    if "cerebro" in sys.modules:
        from pycerebro import database
        from tentaculo.core import capp, config, clogger
        db = database.Database()
        db.connect_from_cerebro_client()
        log = clogger.CLogger()
        config = config.ConfigLoader()
        task_id = config.task_for_file(capp.file_name(log))
        task = db.task(task_id)
        parent_task = db.task(task[2])
        for tag in db.task_tags(parent_task[1]):
            if "cut in" in tag:
                cut_in = tag[-1]
            if "cut out" in tag:
                cut_out = tag[-1]
            if cut_in and cut_out:
                break
    else:
        main_cam = [x for x in pm.ls(type="camera") if ":cam" in x.name().lower()]
        main_cam = main_cam[0].parent(0) if main_cam else None
        if main_cam:
            main_cam.tx.set(lock=0)
            main_cam.ty.set(lock=0)
            main_cam.tz.set(lock=0)
            main_cam.rx.set(lock=0)
            main_cam.ry.set(lock=0)
            main_cam.rz.set(lock=0)
            all_keys = sorted(pm.keyframe(main_cam, q=True) or [])
            cut_in = all_keys[0]
            cut_out = all_keys[-1]
            main_cam.tx.set(lock=1)
            main_cam.ty.set(lock=1)
            main_cam.tz.set(lock=1)
            main_cam.rx.set(lock=1)
            main_cam.ry.set(lock=1)
            main_cam.rz.set(lock=1)
    pm.playbackOptions(min=cut_in, animationStartTime=cut_in, max=cut_out, animationEndTime=cut_out)