from dataclasses import dataclass, field

@dataclass
class NetInterfaceIOData:
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
class NetAddressData:
    ip:     str = ""
    port:   int = 0


@dataclass
class NetConnectionData:
    family: int             = 0
    kind:   int             = 0
    laddr:  NetAddressData  = field(default_factory=NetAddressData)
    raddr:  NetAddressData  = field(default_factory=NetAddressData)
    status: str             = ""
    pid:    int             = 0