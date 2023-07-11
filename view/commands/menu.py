

from view.commands.command_add import CommandAdd
from view.commands.command_change import CommandChange
from view.commands.command_exit import CommandExit
from view.commands.command_open import CommandOpen
from view.commands.command_remove import CommandRemove
from view.commands.command_save import CommandSave
from view.commands.command_show_all import CommandShowAll


class Menu:

    def __init__(self, console):
        self.commands = []
        self.commands.append(CommandOpen(console))
        self.commands.append(CommandShowAll(console))
        self.commands.append(CommandAdd(console))
        self.commands.append(CommandChange(console))
        self.commands.append(CommandRemove(console))
        self.commands.append(CommandSave(console))
        self.commands.append(CommandExit(console))

    def __str__(self):

        menu_string = "\n======== Главное меню ========\n"
        for i, cmd in enumerate(self.commands, start=1):
            menu_string += f"\t{i}. {cmd.description}\n"
        return menu_string

    def get_size_menu(self):  # Длина списка меню
        return len(self.commands)

    def execute(self, index):  # Запуск выбранной пользователем команды
        option = self.commands[index]
        option.execute()
