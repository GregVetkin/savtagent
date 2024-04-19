from .basesender    import DataSender
from ..data         import NetInterfaceIO, NetConnection
from typing         import List


class NetInterfacesesIOSender(DataSender):
    def send(net_io: List[NetInterfaceIO], receiver):
        receiver.save_net_io_data(net_io)


class NetConnectionsSender(DataSender):
    def send(connections: List[NetConnection], receiver):
        receiver.save_net_connections_data(connections)