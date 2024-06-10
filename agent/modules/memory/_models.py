from dataclasses import dataclass, field


@dataclass
class _RamMemory:
    total:      int     = 0
    free:       int     = 0
    used:       int     = 0
    percent:    float   = 0

@dataclass
class _SwapMemory:
    total:      int     = 0
    free:       int     = 0
    used:       int     = 0
    percent:    float   = 0



@dataclass
class RamMemory:
    active:         int = 0
    available:      int = 0
    buffers:        int = 0
    cached:         int = 0
    free:           int = 0
    inactive:       int = 0
    percent:        float = 0.0
    shared:         int = 0
    slab:           int = 0
    total:          int = 0
    used:           int = 0
    

@dataclass
class SwapMemory:
    free:       int = 0
    percent:    float = 0.0
    sin:        int = 0
    sout:       int = 0
    total:      int = 0
    used:       int = 0


@dataclass
class Memory:
    ram:    RamMemory   = field(default_factory=RamMemory)
    swap:   SwapMemory  = field(default_factory=SwapMemory)