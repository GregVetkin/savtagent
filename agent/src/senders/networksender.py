from .basesender    import DataSender
from ..data         import NetInterfaceIOData
from typing         import List


class NetInterfacesesIODataSender(DataSender):
    def send(net_io: List[NetInterfaceIOData], receiver):
        receiver.save_net_io_data(net_io)
