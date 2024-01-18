"""
Ce module inclut des utilitaires système et des modules externes nécessaires à l'application.

Il comprend les fonctionnalités suivantes :
- os : Module pour les opérations liées au système d'exploitation.
- subprocess : Module pour l'exécution de processus externes.
"""
import os
import subprocess








class TerminalMenu:
    """_TerminalMenu_"""

    def __init__(self):
        command = 'cls' if os.name == 'nt' else 'clear'
        subprocess.call(command, shell=True)


    def show_main_menu(self):
        """_show_main_menu_"""

        print("====== MENU ======")
        print("1. Add new player")
        print("2. Print all players")
        print("3. Start tournaments")
        print("4. Quit")
        print("==================")


    def show_add_new_player_menu(self) -> str:
        """_show_add_new_player_menu_

        Returns:
            str: _description_
        """

        print("======= ADD NEW PLAYER =======")
        first_name = input("Enter the player's first name : ")
        last_name = input("Enter the player's last name : ")
        birth_date = input("Enter the player's birth date (format: DD/MM/YYYY) : ")
        identification_code = input("Enter the identification code : ")
        print("=========================================")
        input("Press Enter to return to the main menu...")
        return first_name, last_name, birth_date, identification_code


    def print_all_player(self, list_players:str):
        """_print_all_player_

        Args:
            list_players (str): _description_
        """

        print("======= LIST OF PLAYERS =======")
        print(list_players)
        print("=================================")
        input("Press Enter to return to the main menu...")


    def tournaments_menu(self):
        """_tournaments_menu_"""

        print("============ TOURNAMENTS ============")
        print("1. Create new tournament")
        print("2. Select tournament")
        print("3. Option 3")
        print("4. Return to main menu")
        print("==================================")


    def tournaments_create(self) -> str:
        """_tournaments_create_

        Returns:
            str: _description_
        """

        print("======= CREATE NEW TOURNAMENTS =======")

        name = input("Enter the name of the tournament : ")
        location = input("Enter the location of the tournament : ")
        date_start = input("Enter the start date of the tournament : ")
        date_end = input("Enter the end date of the tournament : ")
        num_rounds = input("Enter the number of revolutions (default = 4) : ")

        print("=========================================")
        input("Press Enter to return to the main menu...")
        return name, location, date_start, date_end, num_rounds


    def select_tournament(self, list_tournaments:str) -> str:
        """_select_tournament_

        Args:
            list_tournaments (str): _description_

        Returns:
            str: _description_
        """

        print("======= SELECT TOURNAMENT =======")
        print(list_tournaments)
        print("=================================")
        select_tournament = input("Select your tournament : ")
        return select_tournament


    def launch_tournament(self, list_players:str, dftournament:str) -> str:
        """_launch_tournament_

        Args:
            list_players (str): _description_
            dftournament (str): _description_

        Returns:
            str: _description_
        """

        print("================ SELECTED TOURNAMENTS =================")
        print(dftournament)
        print("======= LIST OF PLAYERS IN THE DATABASE =======")
        print(list_players)
        print("=======================================================")
        print("1. Add new player")
        print("2. Launch matchs")
        print("3. Return to main menu")
        print("=======================================================")
        choice = input("Select option : ")
        return choice


    def print_pair_players(self, pair_list:str, actual_round:str):
        """_print_pair_players_

        Args:
            pair_list (str): _description_
            actual_round (str): _description_
        """

        print(f"====================== {actual_round} =======================")
        print(pair_list)


    def standby_start_round(self):
        """_standby_start_round_"""

        print("======================================================")
        input("Press a button to start the round...")


    def set_result_match(self, pair_list:str, actual_round:str) -> str:
        """_summary_

        Args:
            pair_list (str): _description_
            actual_round (str): _description_

        Returns:
            str: _description_
        """

        print(f"================== END OF {actual_round} ===================")
        print(pair_list)
        return input("Who is the winner ? (1=player1, 2=player2, 3=equal)")


    def clear_terminal(self):
        """_clear_terminal_""" 

        command = 'cls' if os.name == 'nt' else 'clear'

        subprocess.call(command, shell=True)

# Exemple d'utilisation :
def print_menu():
    """_print_menu_"""

    menu = TerminalMenu()
    menu.show_main_menu()
