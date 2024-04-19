from .basesender    import DataSender
from ..data         import Process
from typing         import List


class ProcessesSender(DataSender):
    def send(processes: List[Process], receiver):
        receiver.save_processes_data(processes)
