# -*- coding: utf-8 -*-
from pathlib import Path
try:
    import lconfig
except:
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    import lconfig
from mocap import convert_to_25fps
from mocap import create_character_definition


def after_event(event):
    # Если переключиться в статус "Готово к работе" внутри активности "Animation"
    if event.event_type() == event.EVENT_CHANGING_OF_TASKS_STATUS:
        tasks = event.tasks()
        for task in tasks:
            status = task.status()
            activity_name = task.activity()
            if status[0] == 2927339757821346916 and activity_name[1] == "anim": # ID статуса "Готово к работе"
                folder = Path(lconfig.project_path()).parent.joinpath(task.parent_url()).parent.joinpath("mocap_data")
                # Конвертирует все mov-файлы в полученной папке в 25 кадров/сек в виде png-сиквенции
                convert_to_25fps.convert(str(folder))
                # Настраивает fbx-скелет и сохраняет в MA
                create_character_definition.create_ma(str(folder))
