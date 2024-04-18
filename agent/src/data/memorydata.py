from dataclasses import dataclass

@dataclass
class RamMemoryData:
    total:      int     = 0
    available:  int     = 0
    percent:    float   = 0
    used:       int     = 0


@dataclass
class SwapMemoryData:
    total:      int     = 0
    percent:    float   = 0
    used:       int     = 0
    free:       int     = 0


@dataclass
class MemoryData:
    ram:    RamMemoryData
    swap:   SwapMemoryData