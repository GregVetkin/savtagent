from .baseseder     import DataSender
from ..collectors   import DiskData
from typing         import List


class DisksDataSender(DataSender):
    def send(disks: List[DiskData], receiver):
        receiver.save_disks_data(disks)
