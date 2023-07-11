from view.commands.command_abstract import Command


class CommandAdd(Command):  # Добавление заметки

    def __init__(self, console):
        self.console = console

    @property
    def description(self):  # Возвращение описания команды
        return "Добавить заметку"

    def execute(self):  # Запуск метода добавления заметки
        self.console.add_note()
