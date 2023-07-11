
from view.commands.command_abstract import Command


class CommandSave(Command):  # Сохранение изменений в записной книге в файл

    def __init__(self, console):
        self.console = console

    @property
    def description(self):  # Возвращение описания команды
        return "Сохранить изменения"

    def execute(self):  # Запускает команду сохранения изменений в записной книге в файл
        self.console.save_changes()
