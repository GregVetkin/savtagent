from abc        import ABC, abstractmethod
from typing     import Any


class BaseCollector(ABC):
    """
    Абстрактное представление класса сборщика.
    Его задача - собрать и вернуть нужные данные.
    """

    @abstractmethod
    def collect(self) -> Any:
        pass
