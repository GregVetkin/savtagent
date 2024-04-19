from abc            import ABC, abstractmethod
from dataclasses    import dataclass
from typing         import List, Union
from ..data         import DataClass

class DataSender(ABC):
    @abstractmethod
    def send(data: Union[List[DataClass], DataClass], receiver):
        pass


