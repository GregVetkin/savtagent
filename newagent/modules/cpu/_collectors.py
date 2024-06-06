from models         import BaseCollector
from ._models       import CpuUsage
from psutil         import cpu_percent
from statistics     import mean


class CpuUsageCollector(BaseCollector):
    def __init__(self, interval=None):
        self._interval = interval

    def collect(self) -> CpuUsage:
        cpu = cpu_percent(percpu=True, interval=self._interval)
        return CpuUsage(
            cores   = cpu,
            mean    = mean(cpu),
        )