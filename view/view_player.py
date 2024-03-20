import os
import subprocess
from simple_term_menu import TerminalMenu

try:
    from view.view_main import ClearTerminal
except ModuleNotFoundError:
    from view_main import ClearTerminal

class PlayerView():
    def start_view_add_player(self):
        """_show_add_new_player_menu_

        Returns:
            str: _description_
        """
        ClearTerminal()

        print("======= ADD NEW PLAYER =======")
        first_name = input("Enter the player's first name : ")
        last_name = input("Enter the player's last name : ")
        birth_date = input("Enter the player's birth date (format: DD/MM/YYYY) : ")
        identification_code = input("Enter the identification code : ")
        print("=========================================")
        input("Press Enter to return to the main menu...")
        return first_name, last_name, birth_date, identification_code

    def show_players(self, dataframe):
        print("=========================================")
        print(dataframe)
        print("=========================================")
        input("Press Enter to return to the main menu...")





if __name__ == '__main__':
    affichage = addPlayerView()
    affichage.start_view_add_player()