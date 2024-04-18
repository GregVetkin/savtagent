from .basecollector     import DataCollector
from ..data             import RamMemoryData, SwapMemoryData, MemoryData
from psutil             import virtual_memory, swap_memory


class RamMemoryDataCollector(DataCollector):
    def collect() -> RamMemoryData:
        ram = virtual_memory()
        return RamMemoryData(
            total       = ram.total,
            available   = ram.available,
            used        = ram.used,
            percent     = ram.percent
        )
    

class SwapMemoryDataCollector(DataCollector):
    def collect() -> SwapMemoryData:
        swap = swap_memory()
        return SwapMemoryData(
            total   = swap.total,
            free    = swap.free,
            used    = swap.used,
            percent = swap.percent
        )
    
class MemoryDataCollector(DataCollector):
    def collect() -> MemoryData:
        return MemoryData(
            ram     = RamMemoryDataCollector.collect(),
            swap    = SwapMemoryDataCollector.collect(),
        )
