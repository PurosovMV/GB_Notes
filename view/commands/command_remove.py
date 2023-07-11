
from view.commands.command_abstract import Command


class CommandRemove(Command):  # Удаление заметки

    def __init__(self, console):
        self.console = console

    @property
    def description(self):  # Возвращение описания команды
        return "Удалить заметку"

    def execute(self):  # Запуск метода удаления заметки
        self.console.remove_note()
