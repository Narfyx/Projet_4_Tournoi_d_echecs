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
        print("======= AJOUTER UN NOUVEAU JOUEUR =======")
        
        first_name = input("Entrez le prénom du joueur : ")
        last_name = input("Entrez le nom du joueur : ")
        birth_date = input("Entrez la date de naissance du joueur (format : JJ/MM/AAAA) : ")
        identification_code = input("Entrez le code d'identification : ")
        """
        first_name="jean"
        last_name="dupont"
        birth_date="04/03/1906"
        identification_code="ab12345"
        """
        print("=========================================")
        input("Appuyez sur Entrée pour revenir au menu principal...")
        return first_name, last_name, birth_date, identification_code

    def print_all_player(self, list_players):
        print("======= LISTE DES JOUEURS =======")
        print(list_players)
        print("=================================")
        input("Appuyez sur Entrée pour revenir au menu principal...")

    def tournaments_menu(self):
        print("============ TOURNOIS ============")
        print("1. Create new tournament")
        print("2. Select tournament")
        print("3. Option 3")
        print("4. Return to main menu")
        print("==================================")
        
    def tournaments_create(self):
        print("======= CREER NOUVEAU TOURNOIS =======") # part 1 création du tournois
        
        name = input("Entrez le nom du tournois : ")
        location = input("Entrez le lieu du tournois : ")
        date_start = input("Entrez la date de commencement du tournois : ")
        date_end = input("Entrez la date de fin du tournois : ")
        num_rounds = input("Entrez le nombre de tours (défaut = 4) : ")
        """
        name="tata"
        location="tutu"
        date_start="19/12/2020"
        date_end="10/10/2023"
        num_rounds="4"
        """
        print("=========================================")
        input("Appuyez sur Entrée pour revenir au menu principal...")
        return name, location, date_start, date_end, num_rounds
    
    def select_tournament(self, list_tournaments):
        print("======= SELECT TOURNAMENT =======")
        print(list_tournaments)
        print("=================================")
        select_tournament = input("Select your tournament : ")
        return select_tournament

    def launch_tournament(self, list_players, dftournament):
        print("================ TOURNOIS SELECTIONNE =================")
        print(dftournament)
        print("======= LISTE DES JOUEURS DANS LA BASE DE DONNEE=======")
        print(list_players)
        print("=======================================================")
        print("1. Ajouter nouveau joueur")
        print("2. Lancement des matchs")
        print("3. Return to main menu")
        print("=======================================================")
        choice = input("Select option : ")
        return choice
    
    def print_pair_players(self, pair_list, round):
        print(f"====================== {round} =======================")
        print(pair_list)
        
    def standby_start_round(self):
        print("======================================================")
        input("Appuyez sur une touche pour lancer le round...")
    
    def set_result_match(self, pair_list, round):
        print(f"================== FIN DU {round} ===================")
        print(pair_list)
        return input("Who is the winner ? (1=player1, 2=player2, 3=equal)")
# Exemple d'utilisation :
def print_menu():
    menu = TerminalMenu()
    menu.show_main_menu()
