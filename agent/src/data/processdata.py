from dataclasses import dataclass


@dataclass
class Process:
    pid:            int     = 0
    name:           str     = ""
    user:           str     = ""
    status:         str     = ""
    memory_usage:   int     = 0
    cpu_usage:      float   = 0.0

