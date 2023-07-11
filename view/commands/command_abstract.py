
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def description(self):
        """Метод, возвращающий описание команды"""

    @abstractmethod
    def execute(self):
        """ Метод для выполнения определенного действия с записной книгой"""
