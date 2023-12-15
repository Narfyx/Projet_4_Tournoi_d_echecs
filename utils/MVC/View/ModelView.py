import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils

import os
import subprocess




class TerminalMenu:
    def __init__(self):

        command = 'cls' if os.name == 'nt' else 'clear'
        
        try:
            subprocess.call(command, shell=True)
        except Exception as e:
            print(f"Erreur lors de l'effacement du terminal : {e}")



    def show_main_menu(self):
        print("===== MENU =====")
        print("1. Add new player")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Quit")
        print("================")
    
    def show_add_new_player_menu(self):
        print("===== AJOUTER UN NOUVEAU JOUEUR =====")
        
        first_name = input("Entrez le prénom du joueur : ")
        last_name = input("Entrez le nom du joueur : ")
        birth_date = input("Entrez la date de naissance du joueur (format : JJ/MM/AAAA) : ")
        identification_code = input("Entrez le code d'identification : ")
        """
        first_name = "jean"
        last_name = "dupont"
        birth_date = "10/10/10000"
        identification_code = "AB12345"
        """
        # Vous pouvez utiliser ces valeurs pour créer un nouvel objet joueur, par exemple
        
        
        # Vous pouvez ensuite effectuer les actions nécessaires avec le nouveau joueur, par exemple l'ajouter à la base de données

        #print("Joueur ajouté avec succès !")
        input("Appuyez sur Entrée pour revenir au menu principal...")
        return first_name, last_name, birth_date, identification_code

    


# Exemple d'utilisation :
def print_menu():
    menu = TerminalMenu()
    menu.show_main_menu()
