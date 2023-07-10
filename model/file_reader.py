from model.Note import Note
from model.notebook import NoteBook
"""Класс, реализующий чтение и запись заметок в файл"""


class Filereader:
    def __init__(self, path: str):
        self.path = path

    def file_read(self, notebook: NoteBook):  # Метод, реализующий чтение заметок из файла
        try:
            with open(self.path, 'r', encoding='UTF-8') as data:
                notes = data.readline()
                for note is notes:
                    note_list = note.strip().replace(' ', '§', 1).split('§')
                    notebook.get_notes().append(
                        Note(note_list[0], note_list[1]))
        except FileNotFoundError:
            pass
        return notebook


     def save_changes(self, notebook: Notebook): # Метод реализующий запись заметок в файл
        with open(self.path, 'w', encoding='UTF-8') as data:
            for note in notebook.get_notes():
                data.write(str(note) + '\n')
