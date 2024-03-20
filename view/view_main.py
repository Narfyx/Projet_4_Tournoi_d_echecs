import os
import subprocess
from simple_term_menu import TerminalMenu

def ClearTerminal():
        command = 'cls' if os.name == 'nt' else 'clear'
        subprocess.call(command, shell=True)

class mainView():

    def StartView(self):
        ClearTerminal()
        print("==================")
        options = ["Add new player", "Tournaments", "Print all players", "Quit"]

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        return menu_entry_index


    def StartTournamentView(self):
        ClearTerminal()
        print("==================")
        options = ["Create tournament", "Generate player pairs", "Enter the results of a round", "Return to main menu"]

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        return menu_entry_index


if __name__ == '__main__':
    affichage = mainView()
    result = affichage.StartTournamentView()
    print(result)