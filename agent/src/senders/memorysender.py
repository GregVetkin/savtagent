from .basesender    import DataSender
from ..data         import Memory, RamMemory, SwapMemory


class RamMemorySender(DataSender):
    def send(ram: RamMemory, receiver):
        receiver.save_ram_data(ram)


class SwapMemorySender(DataSender):
    def send(swap: SwapMemory, receiver):
        receiver.save_swap_data(swap)


class MemorySender(DataSender):
    def send(memory: Memory, receiver):
        receiver.save_memory_data(memory)