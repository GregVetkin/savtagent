from .baseseder import DataSender
from ..collectors import RamMemoryData, SwapMemoryData


class RamMemoryDataSender(DataSender):
    def send(ram: RamMemoryData, receiver):
        receiver.save_ram_data(ram)


class SwapMemoryDataSender(DataSender):
    def send(swap: SwapMemoryData, receiver):
        receiver.save_swap_data(swap)


        