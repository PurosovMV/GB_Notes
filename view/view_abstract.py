"""Модуль, реализующий абстрактный класс View"""
from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def set_presenter(self, presenter):
        """_summary_

        Args:
            presenter (_type_): _description_
        """
    

    @abstractmethod
    def start(self):
        """_summary_
        """
        
