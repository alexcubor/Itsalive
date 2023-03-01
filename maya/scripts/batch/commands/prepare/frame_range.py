import sys
import pymel.core as pm
import traceback


def do(mode=None):
    cut_in = 0
    cut_out = 0
    def _from_cerebro():
        from pycerebro import database
        from tentaculo.core import capp, config, clogger
        db = database.Database()
        db.connect_from_cerebro_client()
        log = clogger.CLogger()
        config = config.ConfigLoader()
        task_id = config.task_for_file(capp.file_name(log))
        task = db.task(task_id)
        parent_task = db.task(task[2])
        cut_in = 0
        cut_out = 0
        for tag in db.task_tags(parent_task[1]):
            if "cut in" in tag:
                cut_in = tag[-1]
            if "cut out" in tag:
                cut_out = tag[-1]
            if cut_in and cut_out:
                break
        return cut_in, cut_out

    def _from_camera():
        main_cam = [x for x in pm.ls(type="camera") if ":cam" in x.name().lower()]
        main_cam = main_cam[0].parent(0) if main_cam else None
        cut_in = 0
        cut_out = 0
        if main_cam:
            try:
                main_cam.tx.set(lock=0)
                main_cam.ty.set(lock=0)
                main_cam.tz.set(lock=0)
                main_cam.rx.set(lock=0)
                main_cam.ry.set(lock=0)
                main_cam.rz.set(lock=0)
            except:
                pass
            all_keys = sorted(pm.keyframe(main_cam, q=True) or [])
            cut_in = all_keys[0]
            cut_out = all_keys[-1]
            try:
                main_cam.tx.set(lock=1)
                main_cam.ty.set(lock=1)
                main_cam.tz.set(lock=1)
                main_cam.rx.set(lock=1)
                main_cam.ry.set(lock=1)
                main_cam.rz.set(lock=1)
            except:
                pass
        return cut_in, cut_out

    if mode == "cerebro":
        cut_in, cut_out = _from_cerebro()
    if mode == "camera":
        cut_in, cut_out = _from_camera()
    if not mode:
        if "cerebro" in sys.modules:
            try:
                cut_in, cut_out = _from_cerebro()
            except Exception:
                traceback.print_exc()

        else:
            cut_in, cut_out = _from_camera()
    pm.playbackOptions(min=cut_in, animationStartTime=cut_in, max=cut_out, animationEndTime=cut_out)