from dataclasses import dataclass, field
from typing import List


@dataclass
class CpuUsageData:
    cores:  List[float] = field(default_factory=list)
    mean:   float       = 0.0