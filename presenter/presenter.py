from model.file_reader import FileReader


class Presenter:
    def __init__(self, view, notebook, path):
        self.__view = view
        self.__notebook = notebook
        self.__view.set_presenter(self)
        self.file = FileReader(path)

    def get_notebook(self):  # Метод, возвращает заметки из записной книжки
        return self.__notebook

    def open_file(self):  # Метод, реализующий чтения файла с заметками
        self.__notebook = self.file.file_read(self.__notebook)

    def save(self): # Сохранение изменений
        self.file.save_changes(self.__notebook)
    
    def is_full(self): # Метод для просмотра наличия записей в файле с заметками
        return self.__notebook.is_full()

    def add_note(self, text_note):# Метод для добавления заметок
        self.__notebook.add_note(text_note)

    def remove_note(self, index): # Метод для удаления заметок
        self.__notebook.remove(index)

    def change_note(self, index, update_text): # Метод, реализующий изменения текста заметки
        self.__notebook.change_note(index, update_text)

    def get_size_notebook(self): # Метод, возвращающий количество заметок записной книжки
        return self.__notebook.size()

