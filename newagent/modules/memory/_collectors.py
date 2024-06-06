from models         import BaseCollector
from ._models       import RamMemory, SwapMemory, Memory
from psutil         import virtual_memory, swap_memory



class RamMemoryCollector(BaseCollector):
    def collect(self) -> RamMemory:
        ram = virtual_memory()
        return RamMemory(
            total       = ram.total,
            free        = ram.available,
            used        = ram.total - ram.available,
            percent     = ram.percent
        )


class SwapMemoryCollector(BaseCollector):
    def collect(self) -> SwapMemory:
        swap = swap_memory()
        return SwapMemory(
            total   = swap.total,
            free    = swap.free,
            used    = swap.used,
            percent = swap.percent
        )


class MemoryCollector(BaseCollector):
    def collect(self) -> Memory:
        return Memory(
            ram     = RamMemoryCollector().collect(),
            swap    = SwapMemoryCollector().collect(),
        )
