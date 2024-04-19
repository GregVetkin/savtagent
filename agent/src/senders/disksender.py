from .basesender    import DataSender
from ..data         import Disk
from typing         import List


class DisksSender(DataSender):
    def send(disks: List[Disk], receiver):
        receiver.save_disks_data(disks)
