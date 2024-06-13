from dataclasses            import dataclass, field
from abc                    import ABC, abstractmethod


class DataSender(ABC):
    @abstractmethod
    def send(self, data: str) -> None:
        pass



@dataclass
class HandlerData:
    url:        str
    sender:     DataSender
    data:       str         = ""
    active:     bool        = False
    error:      str         = ""




    