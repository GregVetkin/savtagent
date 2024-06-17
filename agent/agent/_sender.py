from abc                    import ABC, abstractmethod
from server._api_urls       import *


class DataSender(ABC):
    @abstractmethod
    def send(self, data: str) -> None:
        pass



class MemorySender(DataSender):
    def __init__(self, database):
        self._db = database

    def send(self, data):
        self._db._connect()
        # 
        # 
        # 
        print(data["ram"])
        print(data["swap"])
        self._db._close()


ROUTE_TO_SENDER = {
    API_MEMORY: MemorySender,
}