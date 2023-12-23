import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils  # Importe VotreClasse depuis le module MVC.View


import time, json
import pandas as pd

class TerminalMenuChoice:
    def __init__(self):
        self.is_running = True
        

    def handle_choice(self, choice):

        json_file_path = 'data/players/players.json'
        writer = utils.MVC.Model.ModelPlayer.WriteForBddPlayer(json_file_path)
        readerDuplicate = utils.MVC.Model.ModelPlayer.ReadBddPlayerIfDuplicate(json_file_path)
        reader = utils.MVC.Model.ModelPlayer.ReadBddPlayer(json_file_path)

        if choice == "1":
            print("You chose Option 1. Add new player.")
            new_player_menu = utils.MVC.View.ModelView.TerminalMenu.show_add_new_player_menu(self)
            player = utils.MVC.Model.ModelPlayer.PlayerModel(self)
            try:
                first_name = player.set_first_name((new_player_menu[0]))     
                last_name = player.set_last_name((new_player_menu[1]))
                birth_date = player.set_birth_date((new_player_menu[2]))
                identification = player.set_identification_code((new_player_menu[3]))
            except ValueError as e:
                print(e)
            if (player.get_first_name() is None or 
                player.get_last_name() is None or 
                player.formatted_birth_date() is None or 
                player.get_identification_code() is None or 
                readerDuplicate.check_duplicate(identification_code = player.get_identification_code(), 
                                                first_name = player.get_first_name(), 
                                                last_name = player.get_last_name())):
                self.handle_choice(choice="1")
            else:
                writer.write_player(first_name = player.get_first_name(),
                                    last_name = player.get_last_name(),
                                    birth_date = player.formatted_birth_date(),
                                    identification_code = player.get_identification_code())     
        elif choice == "2":
            print("You chose Option 2. Print all players.") 
            
            df = pd.read_json(json_file_path, orient='columns')

            if 'players' in df.columns and isinstance(df['players'][0], dict):
                players_df = pd.DataFrame(df['players'].tolist())
                players_df = players_df[['first_name', 'last_name', 'birth_date', 'identification_code']]
                print_all_player = utils.MVC.View.ModelView.TerminalMenu.print_all_player(self, list_players = players_df)
            else:
                print("Le format du fichier JSON n'est pas conforme aux attentes.")
            
            
        elif choice == "3":
            print("You chose Option 3. Start tournaments")
            tournaments_menu = TournamentsMenuChoice() 
            tournaments_menu.run_menu()
        elif choice == "4":
            print("Goodbye!")
            self.is_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    def run_menu(self):
        while self.is_running:
            active_menu = utils.MVC.View.ModelView.print_menu()
            user_choice = input("Enter your choice (1-4): ")
            self.handle_choice(user_choice)



class TournamentsMenuChoice:
    def __init__(self):
            self.is_running = True
    def handle_choice(self, choice):

            if choice == "1":
                print()
            elif choice == "2":
                print()
            elif choice == "3":
                print()
            elif choice == "4":
                print()
                self.is_running = False
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def run_menu(self):
        while self.is_running:
            active_menu = utils.MVC.View.ModelView.TerminalMenu.start_tournaments(self)
            user_choice = input("Enter your choice (1-4): ")
            self.handle_choice(user_choice)

                
            


def run():
    menu = TerminalMenuChoice()
    menu.run_menu()