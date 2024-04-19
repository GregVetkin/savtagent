from .basecollector     import DataCollector
from ..data             import NetInterfaceIO
from psutil             import net_io_counters, net_if_stats, net_if_addrs, net_connections
from typing             import List


class NetInterfacesesIOCollector(DataCollector):
    def collect() -> List[NetInterfaceIO]:
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
