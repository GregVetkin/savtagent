from .basecollector     import DataCollector
from .cpudata           import CpuUsageData
from psutil             import cpu_percent
from statistics         import mean


class CpuUsageDataCollector(DataCollector):
    def collect() -> CpuUsageData:
        cpu = cpu_percent(percpu=True, interval=1.0)
        return CpuUsageData(
            cores   = cpu,
            mean    = mean(cpu),
        )