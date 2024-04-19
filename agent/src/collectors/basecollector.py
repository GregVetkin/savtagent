from abc        import  ABC, abstractmethod
from typing     import  List, Union
from ..data     import  DataClass


class DataCollector(ABC):
    @abstractmethod
    def collect() -> Union[List[DataClass], DataClass]:
        pass


