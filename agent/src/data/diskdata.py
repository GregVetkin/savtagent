from dataclasses import dataclass, field


@dataclass
class DiskUsage:
    total:      int     = 0
    used:       int     = 0
    free:       int     = 0
    percent:    float   = 0.0
    

@dataclass
class DiskIO:
    read_count:     int = 0
    write_count:    int = 0
    read_bytes:     int = 0
    write_bytes:    int = 0


@dataclass
class Disk:
    device:     str         = ""
    mountpoint: str         = ""
    usage:      DiskUsage   = field(default_factory=DiskUsage)
    io:         DiskIO      = field(default_factory=DiskIO)

