from .baseseder     import DataSender
from ..collectors   import CpuUsageData


class CpuUsageDataSender(DataSender):
    def send(cpu: CpuUsageData, receiver):
        receiver.save_cpu_usage_data(cpu)