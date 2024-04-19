from .basecollector     import DataCollector
from ..data             import Process
from psutil             import process_iter, NoSuchProcess, ZombieProcess, AccessDenied, cpu_count
from typing             import List
from time               import sleep



class ProcessesCollector(DataCollector):
    def collect() -> List[Process]:
        processes_info = []
        # записать в кэш тайминги процессора на процессах
        for process in process_iter():
            process.cpu_percent()
        # подождать 1 секунду, чтобы иметь разницу работы процессора на процессах за время
        sleep(1)
        number_cpu = cpu_count(logical=True)
        for process in process_iter():
            try:
                processes_info.append(
                    Process(
                        pid             = process.pid,
                        name            = process.name(),
                        user            = process.username(),
                        status          = process.status().__str__(),
                        memory_usage    = process.memory_info().rss,
                        cpu_usage       = process.cpu_percent() / number_cpu, # cpu_percent может вернуть число больше 100 если процесс многопроцессорный
                    )
                )
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                continue
        return processes_info