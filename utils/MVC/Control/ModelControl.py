import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils  # Importe VotreClasse depuis le module MVC.View


import time, json
import pandas as pd
from colorama import Fore
from pprint import pprint

class TerminalMenuChoice:
    def __init__(self):
        self.is_running = True
        

    def handle_choice(self, choice):

        json_file_path_player = 'data/players/players.json'
        writer = utils.MVC.Model.ModelPlayer.WriteForBddPlayer(json_file_path_player)
        readerDuplicate = utils.MVC.Model.ModelPlayer.ReadBddPlayerIfDuplicate(json_file_path_player)
        reader = utils.MVC.Model.ModelPlayer.ReadBddPlayer(json_file_path_player)

        if choice == "1":
            print("You chose Option 1. Add new player.")
            utils.MVC.Control.ModelControl.add_new_player()
            
        elif choice == "2":
            print("You chose Option 2. Print all players.") 
            players_df = utils.MVC.Control.ModelControl.list_players(self)
            print_all_player = utils.MVC.View.ModelView.TerminalMenu.print_all_player(self, list_players = players_df)
            
            
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
            main_menu = utils.MVC.View.ModelView.print_menu()
            user_choice = input("Enter your choice (1-4): ")
            self.handle_choice(user_choice)



class TournamentsMenuChoice:
    def __init__(self):
            self.is_running = True
    def handle_choice(self, choice):

        json_file_path_player = 'data/players/players.json'
        json_file_path_tournaments = 'data/tournaments/tournaments.json'
        writer = utils.MVC.Model.ModelTournaments.WriteForBddTournaments(json_file_path_tournaments)
        readerDuplicate = utils.MVC.Model.ModelTournaments.ReadBddTournamentIfDuplicate(json_file_path_tournaments)
        reader = utils.MVC.Model.ModelTournaments.ReadBddTournaments(json_file_path_tournaments)
        if choice == "1":
            create_tournaments_input = utils.MVC.View.ModelView.TerminalMenu.tournaments_create(self)
            tournaments = utils.MVC.Model.ModelTournaments.ModelCreateTournaments(self)
                
            try:
                    
                    
                tournaments.set_name((create_tournaments_input[0]))     
                tournaments.set_location((create_tournaments_input[1]))
                tournaments.set_date_start((create_tournaments_input[2]))
                tournaments.set_date_end((create_tournaments_input[3]))
                tournaments.set_num_rounds((create_tournaments_input[4]))

                name = tournaments.get_name()     
                location = tournaments.get_location()
                date_start = tournaments.get_date_start()
                date_end = tournaments.get_date_end()
                num_rounds = tournaments.get_num_rounds()

            except ValueError as e:
                print(e)
            if (name is None or 
                location is None or 
                date_start is None or 
                date_end is None or
                num_rounds is None or
                readerDuplicate.check_duplicate(name, 
                                                location, 
                                                date_start)):
                self.handle_choice(choice="1")
            else:
                writer.write_tournament(name,
                                        location,
                                        date_start,
                                        date_end,
                                        num_rounds)    

        elif choice == "2":
            print("You chose Option 2. Select tournament.") 
            
            df = pd.read_json(json_file_path_tournaments, orient='columns')

            
            data = utils.MVC.Model.ModelTournaments.ReadBddTournaments(json_file_path_tournaments).read_bdd_Tournaments()


            if 'Tournaments' in df.columns and isinstance(df['Tournaments'][0], dict):
                list_tournaments = pd.DataFrame(df['Tournaments'].tolist())
                list_tournaments = list_tournaments[['name', 'location', 'date_start', 'date_end', 'num_rounds']]
                
                
                while True:
                    select_tournament = utils.MVC.View.ModelView.TerminalMenu.select_tournament(self, list_tournaments=list_tournaments)

                    
                    try:
                        if int(select_tournament) >= len(data['Tournaments']) or select_tournament.isdigit() == False:
                            print(Fore.RED + "Sélection invalide. Veuillez choisir un numéro de tournoi valide." + Fore.RESET)
                            continue
                             
                        if len(data['Tournaments'][int(select_tournament)]):
                            break

                    except:
                        print(Fore.RED + "Sélection invalide. Veuillez choisir un numéro de tournoi valide." + Fore.RESET)
                        continue


                players_df = utils.MVC.Control.ModelControl.list_players()
                launch_tournament = utils.MVC.View.ModelView.TerminalMenu.launch_tournament(self, list_players=players_df, dftournament=data['Tournaments'][int(select_tournament)]["name"])
                if launch_tournament == "1":
                    print("You chose Option 1. Add new player.")
                    utils.MVC.Control.ModelControl.add_new_player()
                elif launch_tournament == "2":
                    print("You chose Option 2. Start matchs")
                    tournament_selected = data['Tournaments'][int(select_tournament)]
                    
                    obj_players = utils.MVC.Model.ModelPlayer.ReadBddPlayer(json_file_path_player).extract_player_in_bdd()
                    players_list = []
                    for index_to_consult in range(0,len(obj_players)):
                        
                        player_attributes = utils.MVC.Model.ModelPlayer.get_player_attributes_by_index(obj_players, index_to_consult)
                        attribut_score = utils.MVC.Model.ModelTournaments.StartMatch(player_dict=player_attributes).attribut_score()
                        players_list.append(attribut_score)

                        
                    
                    pair_de_joueurs = utils.MVC.Model.ModelTournaments.RandomizePlayerListAndCreatePair(players_list).generate_random_pairs()#côté Model créer la fonction qui rondomize les joueurs et créer des paires
                    
                    nombre_de_round = data['Tournaments'][int(select_tournament)]['num_rounds']
                    
                    data_pairing_players = []
                    for pair in pair_de_joueurs:
                        
                        init_round = utils.MVC.Model.ModelRound.ModelRound(self)
                        init_match = utils.MVC.Model.ModelMatch.Match(player1=pair[0], player2=pair[1])
                        # Créer un DataFrame à partir du tuple
                        df = pd.DataFrame(list(pair))
                        joueur1 = pd.DataFrame({"Joueur 1": (pair[0]["first_name"], pair[0]["last_name"], pair[0]["identification_code"])})
                        vs_df = pd.DataFrame({"VS": ["VS"]}, index=[])
                        joueur2 = pd.DataFrame({"Joueur 2": (pair[1]["first_name"], pair[1]["last_name"], pair[1]["identification_code"])})
                        result_df = pd.concat([joueur1, vs_df, joueur2], axis=1).fillna("")
                        data_pairing_players.append([init_round, init_match, result_df])
                        
                        # Afficher le DataFrame final
                        utils.MVC.View.ModelView.TerminalMenu.print_pair_players(self, pair_list=result_df, round=init_round.nom.upper())
                    utils.MVC.View.ModelView.TerminalMenu.standby_start_round(self)


                    while True:
                        for data_pairing in data_pairing_players:
                            data_pairing[0].marquer_commence()
                            data_pairing[1].init_match()
                            while True:
                                winner_match = utils.MVC.View.ModelView.TerminalMenu.set_result_match(self, data_pairing[2], round=data_pairing[0].nom.upper())
                                if winner_match == "1":#player1 win
                                    data_pairing[1].update_player_scores(result_match="win")
                                    break

                                elif winner_match == "2":#player2 win
                                    data_pairing[1].update_player_scores(result_match="loss")
                                    break
                                elif winner_match == "3":#equal
                                    data_pairing[1].update_player_scores(result_match="draw")
                                    break
                            data_pairing[0].marquer_termine()
                            print(data_pairing[0].tour_actuel)
                            print(data_pairing[0].nombre_total_tours)
                    #utils.MVC.Model.ModelRound.marquer_commence(self)
                    exit()
                    exit()
                    

                    
                elif launch_tournament == "3":
                    self.is_running = False
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

            else:
                print("Le format du fichier JSON n'est pas conforme aux attentes.")
        elif choice == "3":
            self.is_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")




    def run_menu(self):
        while self.is_running:
            main_menu = utils.MVC.View.ModelView.TerminalMenu.tournaments_menu(self)
            user_choice = input("Enter your choice (1-4): ")
            self.handle_choice(user_choice)

                
def add_new_player():
    json_file_path_player = 'data/players/players.json'
    writer = utils.MVC.Model.ModelPlayer.WriteForBddPlayer(json_file_path_player)
    readerDuplicate = utils.MVC.Model.ModelPlayer.ReadBddPlayerIfDuplicate(json_file_path_player)
    reader = utils.MVC.Model.ModelPlayer.ReadBddPlayer(json_file_path_player)
    new_player_menu = utils.MVC.View.ModelView.TerminalMenu.show_add_new_player_menu(self=None)
    player = utils.MVC.Model.ModelPlayer.PlayerModel()
    try:
        player.set_first_name((new_player_menu[0]))     
        player.set_last_name((new_player_menu[1]))
        player.set_birth_date((new_player_menu[2]))
        player.set_identification_code((new_player_menu[3]))

        first_name = player.get_first_name()     
        last_name = player.get_last_name()
        birth_date = player.get_birth_date()
        identification = player.get_identification_code()
    except ValueError as e:
        print(e)
    if (first_name is None or 
        last_name is None or 
        birth_date is None or 
        identification is None or 
        readerDuplicate.check_duplicate(identification, 
                                        first_name, 
                                        last_name)):
        add_new_player()
    else:
        writer.write_player(first_name,
                            last_name,
                            birth_date,
                            identification)                 

def list_players():
    json_file_path_player = 'data/players/players.json'
    df = pd.read_json(json_file_path_player, orient='columns')

    if 'players' in df.columns and isinstance(df['players'][0], dict):
        players_df = pd.DataFrame(df['players'].tolist())
        players_df = players_df[['first_name', 'last_name', 'birth_date', 'identification_code']]
        return players_df
    else:
        print("Le format du fichier JSON n'est pas conforme aux attentes.")

def run():
    menu = TerminalMenuChoice()
    menu.run_menu()