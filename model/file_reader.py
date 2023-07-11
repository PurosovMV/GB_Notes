from model.note import Note
from model.notebook import Notebook

"""Класс, реализующий чтение и запись заметок в файл"""


class FileReader:

    def __init__(self, path: str):
        self.path = path

    def file_read(self, notebook: Notebook):  # Метод, реализующий чтение заметок из файла
        try:
            with open(self.path, 'r', encoding='UTF-8') as data:
                notes = data.readlines()
                for note in notes:
                    note_list = note.strip().replace(' ', '§', 1).split('§')
                    notebook.get_notes().append(
                        Note(note_list[0], note_list[1]))
        except FileNotFoundError:
            pass
        return notebook

    def save_changes(self, notebook: Notebook):  # Метод реализующий запись заметок в файл
        with open(self.path, 'w', encoding='UTF-8') as data:
            for note in notebook.get_notes():
                data.write(str(note) + '\n')
