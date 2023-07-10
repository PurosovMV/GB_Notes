from datetime import datetime
"""Класс для создания и изменения заметок"""


class Note:
    def __init__(self, data, text_note):
         self.__text_note = text_note  # текст заметок
         self.__data = data  # дата создания заметки

    """Метод, возвращающий заметку в виде строки """

    def __str__(self, text_note):
        return f"{self.__data} {self.__text_note}"

        """Метод для изменения текста заметки"""

    def change_text(self, new_text: str):
        self.__text_note = new_text
