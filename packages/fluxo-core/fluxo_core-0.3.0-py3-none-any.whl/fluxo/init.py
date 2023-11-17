import os
import multiprocessing
from fluxo.settings import settings_path_files_python
from fluxo.task import execute_tasks
from fluxo.database.db import _verify_if_db_exists


def execute_fluxos():
    _verify_if_db_exists()
    path = settings_path_files_python.PATH_FILES_PYTHON
    processes = []

    for file in os.listdir(path):
        if file.endswith(".py"):
            process = multiprocessing.Process(
                target=execute_tasks, args=(path, file,))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()
