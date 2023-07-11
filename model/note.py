from datetime import datetime
"""Класс для создания и изменения заметок"""


class Note:
    def __init__(self, data, text_note):
        self.__text_note = text_note  # текст заметок
        self.__data = data  # дата создания заметки

    def __str__(self):  # Метод, возвращающий заметку в виде строки
        return f"{self.__data} {self.__text_note}"

    def change_text(self, new_text: str):  # Метод для изменения текста заметки
        self.__text_note = new_text
