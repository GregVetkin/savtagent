from .basesender    import DataSender
from ..data         import CpuUsage


class CpuUsageSender(DataSender):
    def send(cpu: CpuUsage, receiver):
        receiver.save_cpu_usage_data(cpu)