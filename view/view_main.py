"""main menu display"""
import os
import subprocess
from simple_term_menu import TerminalMenu


def clear_terminal():
    """
    Clears the terminal screen.
    """
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.call(command, shell=True)


class MainView:
    """
    Class for displaying the main menu view.
    """

    def start_view(self):
        """
        Displays the main menu options and retrieves the user's choice.

        Returns:
            int: The index of the selected option.
        """
        clear_terminal()
        print("==================")
        options = ["Add new player", "Tournaments", "Print all players", "Quit"]

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        return menu_entry_index


if __name__ == '__main__':
    affichage = MainView()
    result = affichage.start_view()
    print(result)
