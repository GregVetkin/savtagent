from .basecollector     import DataCollector
from ..data             import CpuUsage
from psutil             import cpu_percent
from statistics         import mean


class CpuUsageCollector(DataCollector):
    def collect() -> CpuUsage:
        cpu = cpu_percent(percpu=True, interval=1.0)
        return CpuUsage(
            cores   = cpu,
            mean    = mean(cpu),
        )