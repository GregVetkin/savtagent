from dataclasses import dataclass, field

@dataclass
class RamMemory:
    total:      int     = 0
    available:  int     = 0
    percent:    float   = 0
    used:       int     = 0


@dataclass
class SwapMemory:
    total:      int     = 0
    percent:    float   = 0
    used:       int     = 0
    free:       int     = 0


@dataclass
class Memory:
    ram:    RamMemory   = field(default_factory=RamMemory)
    swap:   SwapMemory  = field(default_factory=SwapMemory)