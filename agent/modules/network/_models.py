from dataclasses import dataclass, field

@dataclass
class NetInterfaceIO:
    interface:      str = ""
    bytes_sent:     int = 0
    bytes_recv:     int = 0
    packets_sent:   int = 0
    packets_recv:   int = 0
    errin:          int = 0
    errout:         int = 0
    dropin:         int = 0
    dropout:        int = 0


@dataclass
class NetAddress:
    ip:     str = ""
    port:   int = 0


@dataclass
class NetConnection:
    family: int             = 0
    kind:   int             = 0
    laddr:  NetAddress      = field(default_factory=NetAddress)
    raddr:  NetAddress      = field(default_factory=NetAddress)
    status: str             = ""
    pid:    int             = 0