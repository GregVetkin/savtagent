from abc import ABC, abstractmethod
from dataclasses import dataclass


class DataSender(ABC):
    @abstractmethod
    def send(data: dataclass, receiver):
        pass


