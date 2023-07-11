
from view.commands.command_abstract import Command


class CommandShowAll(Command): #  Вывод всех заметок в консоль

    def __init__(self, console):
        self.console = console

    @property
    def description(self): # Возвращение описания команды
        return "Показать все заметки"

    def execute(self): # Запуск метода вывода заметок в консоль
        self.console.show_all()
