
from view.commands.command_abstract import Command


class CommandOpen(Command):  # Заполнение записной книги из файла

    def __init__(self, console):
        self.console = console

    @property
    def description(self):  # Возвращение описания команды
        return "Открыть записную книгу"

    def execute(self): # Запуск метода заполнения записной книги из файла
        self.console.open_notebook()
