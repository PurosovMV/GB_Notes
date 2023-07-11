
from view.commands.command_abstract import Command


class CommandChange(Command):  # Изменение заметки

    def __init__(self, console):
        self.console = console

    @property
    def description(self):  # Возвращение описания команды
        return "Изменить заметку"

    def execute(self):  # Запуск метода изменения заметки
        self.console.change_note()
