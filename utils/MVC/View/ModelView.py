import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent du parent du parent au chemin de recherche de modules
import utils

import os, subprocess
from pprint import pprint



class TerminalMenu:
    def __init__(self):

        command = 'cls' if os.name == 'nt' else 'clear'
        
        try:
            subprocess.call(command, shell=True)
        except Exception as e:
            print(f"Erreur lors de l'effacement du terminal : {e}")



    def show_main_menu(self):
        print("====== MENU ======")
        print("1. Add new player")
        print("2. Print all players")
        print("3. Start tournaments")
        print("4. Quit")
        print("==================")
    
    def show_add_new_player_menu(self):
        print("======= ADD NEW PLAYER =======")
        
        first_name = input("Enter the player's first name : ")
        last_name = input("Enter the player's last name : ")
        birth_date = input("Enter the player's birth date (format: DD/MM/YYYY) : ")
        identification_code = input("Enter the identification code : ")
        """
        first_name="jean"
        last_name="dupont"
        birth_date="04/03/1906"
        identification_code="ab12345"
        """
        print("=========================================")
        input("Press Enter to return to the main menu...")
        return first_name, last_name, birth_date, identification_code

    def print_all_player(self, list_players):
        print("======= LIST OF PLAYERS =======")
        print(list_players)
        print("=================================")
        input("Press Enter to return to the main menu...")

    def tournaments_menu(self):
        print("============ TOURNAMENTS ============")
        print("1. Create new tournament")
        print("2. Select tournament")
        print("3. Option 3")
        print("4. Return to main menu")
        print("==================================")
        
    def tournaments_create(self):
        print("======= CREATE NEW TOURNAMENTS =======") # part 1 création du tournois
        
        name = input("Enter the name of the tournament : ")
        location = input("Enter the location of the tournament : ")
        date_start = input("Enter the start date of the tournament : ")
        date_end = input("Enter the end date of the tournament : ")
        num_rounds = input("Enter the number of revolutions (default = 4) : ")
        """
        name="tata"
        location="tutu"
        date_start="19/12/2020"
        date_end="10/10/2023"
        num_rounds="4"
        """
        print("=========================================")
        input("Press Enter to return to the main menu...")
        return name, location, date_start, date_end, num_rounds
    
    def select_tournament(self, list_tournaments):
        print("======= SELECT TOURNAMENT =======")
        print(list_tournaments)
        print("=================================")
        select_tournament = input("Select your tournament : ")
        return select_tournament

    def launch_tournament(self, list_players, dftournament):
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
    
    def print_pair_players(self, pair_list, round):
        print(f"====================== {round} =======================")
        print(pair_list)
        
    def standby_start_round(self):
        print("======================================================")
        input("Press a button to start the round...")
    
    def set_result_match(self, pair_list, round):
        print(f"================== END OF {round} ===================")
        print(pair_list)
        return input("Who is the winner ? (1=player1, 2=player2, 3=equal)")
    
    def clear_terminal(self):
        command = 'cls' if os.name == 'nt' else 'clear'
        
        try:
            subprocess.call(command, shell=True)
        except Exception as e:
            print(f"Terminal clear error : {e}")
# Exemple d'utilisation :
def print_menu():
    menu = TerminalMenu()
    menu.show_main_menu()
