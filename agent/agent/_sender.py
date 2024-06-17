from abc                    import ABC, abstractmethod



class DataSender(ABC):
    @abstractmethod
    def send(self, data: str) -> None:
        pass




class MemorySender(DataSender):
    def __init__(self, database):
        self._db = database

    def send(self, data):
        self._db._connect()
        # Запись в нужную таблцицу данные
        print(data["ram"])
        print(data["swap"])
        self._db._close()