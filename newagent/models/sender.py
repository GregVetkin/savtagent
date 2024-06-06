from abc        import ABC, abstractmethod
from typing     import Any
from .saver     import BaseSaver


class BaseSender(ABC):
    """
    Абстрактное представление класса передатчика.
    Его задача - передать полученные данные получателю.
    """

    @abstractmethod
    def send(data: Any, receiver: BaseSaver):
        pass

