from dataclasses import dataclass, field


@dataclass
class DiskUsageData:
    total:      int     = 0
    used:       int     = 0
    free:       int     = 0
    percent:    float   = 0.0
    

@dataclass
class DiskIOData:
    read_count:     int = 0
    write_count:    int = 0
    read_bytes:     int = 0
    write_bytes:    int = 0


@dataclass
class DiskData:
    device:     str     = ""
    mountpoint: str     = ""
    usage:      DiskUsageData = field(default_factory=DiskUsageData)
    io:         DiskIOData    = field(default_factory=DiskIOData)

