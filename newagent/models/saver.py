from abc        import ABC, abstractmethod
from typing     import Any



class BaseSaver(ABC):
    """
    Абстрактное представление класса сохранения.
    Его задача - сохранить данные (в базе данных, в файл и т.д.)
    """

    @abstractmethod
    def save(data: Any):
        pass






