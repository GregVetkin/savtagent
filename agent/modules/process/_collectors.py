from models             import BaseCollector
from ._models           import Process
from psutil             import process_iter, NoSuchProcess, ZombieProcess, AccessDenied, cpu_count
from typing             import List
from time               import sleep



class ProcessesCollector(BaseCollector):
    def __init__(self, interval=None):
        self._interval = interval

    def collect(self) -> List[Process]:
        processes = []

        if self._interval:
            # записать в кэш тайминги процессора на процессах
            for process in process_iter():
                process.cpu_percent()
            # подождать, чтобы иметь разницу работы процессора на процессах за время
            sleep(self._interval)

        #number_cpu = cpu_count(logical=True)
        for process in process_iter():
            try:
                processes.append(
                    Process(
                        pid             = process.pid,
                        name            = process.name(),
                        user            = process.username(),
                        status          = process.status().__str__(),
                        memory_usage    = process.memory_info().rss,
                        cpu_usage       = process.cpu_percent() #/ number_cpu, # cpu_percent может вернуть число больше 100 если процесс многопроцессорный
                    )
                )
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                continue
        return processes