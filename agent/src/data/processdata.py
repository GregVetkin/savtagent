from dataclasses import dataclass


@dataclass
class ProcessData:
    pid:            int     = 0
    name:           str     = ""
    user:           str     = ""
    status:         str     = ""
    memory_usage:   int     = 0
    cpu_usage:      int     = 0

