from models         import BaseCollector
from ._models       import RamMemory, SwapMemory, Memory
from psutil         import virtual_memory, swap_memory



class RamMemoryCollector(BaseCollector):
    def collect(self) -> RamMemory:
        ram = virtual_memory()
        return RamMemory(
            total       = ram.total,
            free        = ram.free,
            used        = ram.used,
            percent     = ram.percent,
            active      = ram.active,
            available   = ram.available,
            buffers     = ram.buffers,
            cached      = ram.cached,
            inactive    = ram.inactive,
            shared      = ram.shared,
            slab        = ram.slab,
        )


class SwapMemoryCollector(BaseCollector):
    def collect(self) -> SwapMemory:
        swap = swap_memory()
        return SwapMemory(
            total   = swap.total,
            free    = swap.free,
            used    = swap.used,
            percent = swap.percent,
            sin     = swap.sin,
            sout    = swap.sout,
        )


class MemoryCollector(BaseCollector):
    def collect(self) -> Memory:
        return Memory(
            ram     = RamMemoryCollector().collect(),
            swap    = SwapMemoryCollector().collect(),
        )
