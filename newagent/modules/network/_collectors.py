from models             import BaseCollector
from ._models           import NetInterfaceIO, NetConnection, NetAddress
from psutil             import net_io_counters, net_if_stats, net_if_addrs, net_connections
from typing             import List


class NetInterfacesesIOCollector(BaseCollector):
    def collect(self) -> List[NetInterfaceIO]:
        result = []
        net_io = net_io_counters(pernic=True)
        for interface in net_io:
            io = net_io[interface]
            result.append(
                NetInterfaceIO(
                    interface       = interface,
                    bytes_sent      = io.bytes_sent,
                    bytes_recv      = io.bytes_recv,
                    packets_sent    = io.packets_sent,
                    packets_recv    = io.packets_recv,
                    errin           = io.errin,
                    errout          = io.errout,
                    dropin          = io.dropin,
                    dropout         = io.dropout,
                )
            )
        return result


class NetConnectionsCollector(BaseCollector):
    def collect(self) -> List[NetConnection]:
        result      = []
        connections = net_connections()
        for c in connections:
            result.append(
                NetConnection(
                    family  = c.family.__int__(),
                    kind    = c.type.__int__(),
                    status  = c.status,
                    pid     = c.pid,
                    laddr   = NetAddress(
                            ip   = c.laddr.ip   if c.laddr else None,
                            port = c.laddr.port if c.laddr else None,
                    ),
                    raddr   = NetAddress(
                            ip   = c.raddr.ip   if c.raddr else None,
                            port = c.raddr.port if c.raddr else None,
                    )
                )
            )
        return result