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


# @dataclass
# class NetInterfaceData:
#     name: str                   = "",
#     io:   NetInterfaceIOData    = field(default_factory=NetInterfaceIOData)

