import os
import subprocess
from simple_term_menu import TerminalMenu

try:
    from view.view_main import ClearTerminal
except ModuleNotFoundError:
    from view_main import ClearTerminal

class PlayerView:
    """
    Class for displaying player-related views and collecting user inputs.
    """

    def start_view_add_player(self):
        """
        Displays the view for adding a new player.

        Returns:
            tuple: A tuple containing the details of the new player entered by the user.
        """
        ClearTerminal()

        print("======= ADD NEW PLAYER =======")
        first_name = input("Enter the player's first name : ")
        last_name = input("Enter the player's last name : ")
        birth_date = input("Enter the player's birth date (format: DD/MM/YYYY) : ")
        identification_code = input("Enter the identification code : ")
        print("=========================================")
        input("Press keyboard")
        return first_name, last_name, birth_date, identification_code

    def show_players(self, dataframe):
        """
        Displays the list of players.

        Args:
            dataframe (DataFrame): The DataFrame containing player data.
        """
        print("=========================================")
        print(dataframe)
        print("=========================================")
        input("Press keyboard")

if __name__ == '__main__':
    affichage = PlayerView()
    affichage.start_view_add_player()
