from .basesender    import DataSender
from ..data         import ProcessData
from typing         import List


class ProcessesDataSender(DataSender):
    def send(processes: List[ProcessData], receiver):
        receiver.save_processes_data(processes)
