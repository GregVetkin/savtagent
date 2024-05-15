from .basecollector     import DataCollector
from ..data             import RamMemory, SwapMemory, Memory
from psutil             import virtual_memory, swap_memory


class RamMemoryCollector(DataCollector):
    def collect() -> RamMemory:
        ram = virtual_memory()
        return RamMemory(
            total       = ram.total,
            available   = ram.available,
            used        = ram.total - ram.available,
            percent     = ram.percent
        )
    

class SwapMemoryCollector(DataCollector):
    def collect() -> SwapMemory:
        swap = swap_memory()
        return SwapMemory(
            total   = swap.total,
            free    = swap.free,
            used    = swap.used,
            percent = swap.percent
        )
    
class MemoryCollector(DataCollector):
    def collect() -> Memory:
        return Memory(
            ram     = RamMemoryCollector.collect(),
            swap    = SwapMemoryCollector.collect(),
        )
