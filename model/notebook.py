from datetime import datetime
from model.note import Note

"""Класс, реализующий создание записной книжки"""


class Notebook:

    def __init__(self):
        self.__notes = []  # список заметок

    def size(self):  # метод возвращает количество заметок
        return len(self.__notes)

    def add_note(self, text_note):  # метод добавляет новую заметку
        note = Note(datetime.today().strftime('%d.%m.%Y'), text_note)
        self.__notes.append(note)

    def remove(self, index):  # метод удаления заметки по индексу
        del self.__notes[index]

    def change_note(self, index, update_text):  # метод для изменения заметки по индексу
        self.__notes[index].change_text(update_text)

    def __str__(self):  # Метод возвращает строковое представление заметок
        notes_string = "\nСписок заметок:\n"
        for i, note in enumerate(self.__notes, start=1):
            notes_string += f"\t{i}. {note}\n"
        return notes_string

    def is_full(self):  # Метод проверяет есть ли заметки
        return bool(self.__notes)

    def get_notes(self):  # метод возвращает список заметок
        return self.__notes
