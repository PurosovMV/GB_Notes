
from view.commands.command_abstract import Command


class CommandExit(Command):  # Завершение работы программы

    def __init__(self, console):
        self.console = console

    @property
    def description(self):  # Возвращение описания команды
        return "Завершить работу"

    def execute(self):  # Запуск метода завершения работы программы
        self.console.finish()
