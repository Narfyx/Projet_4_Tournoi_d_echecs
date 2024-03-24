import time
import pandas as pd

from pprint import pprint
import os
import pickle
import json

from model.model_player import PlayerModel
from model.tournament_manager import extract_tournaments_data, convert_data_json_to_obj
from model.model_tournaments import ModelCreateTournaments
from model.model_round import Round

from view.view_main import ClearTerminal
from view.view_main import mainView #(StartView, StartTournamentView)
from view.view_player import PlayerView #start_view_add_player
from view.view_tournament import tournamentView #CreateTournamentView
from view.view_rounds import roundsView

from control.control_main import mainView #create_player7


class controlTournament():
    def tournament(self):
        choice_tournament = tournamentView.StartTournamentView(self)
        if choice_tournament == 0: #Create tournament
            controlTournament.create_tournament(self)
        elif choice_tournament == 1: # Select and start tournament -> Generate player pairs 
            data_tournament = extract_tournaments_data()
            df = pd.DataFrame(data_tournament)
            selector_tournaments = [tournament['name'] for tournament in data_tournament]
            choice_tournament_select = tournamentView.show_tournaments(self, dataframe=df, selector=selector_tournaments)
            tournament_select = data_tournament[choice_tournament_select]
            controlTournament.lancement_des_affrontements(self, tournament_select)
        elif choice_tournament == 2: # Return to main menu
            self.run(mainView.StartView(self))
        
    def lancement_des_affrontements(self, tournament_select):
        tournament_select_rounds = controlTournament.load_status(self, tournament=tournament_select)
        pair_information = tournament_select_rounds.players_pair
        roundsView.affiche_pair(self, data=pair_information)
        tournament_select_rounds.affrontement()
        if len(tournament_select_rounds.players_pair) > 1:
            tournament_select_rounds.new_combinaison_by_score()
            pair_information = tournament_select_rounds.players_pair
            roundsView.affiche_pair(self, data=pair_information)
            tournament_select_rounds.affrontement()
        #affichage de la fin du tournois
        tournament_select_rounds.list_players.sort(key=lambda x: x['score'], reverse=True)
        roundsView.print_resultat(self, data=tournament_select_rounds.list_players)
        self.run(mainView.StartView(self))
    
    def load_status(self, tournament):
        try:
            tournament_dir = f"data/tournaments_play/{tournament['name']}/"
            match_files = [f for f in os.listdir(tournament_dir) if f.startswith("round") and f.endswith("_matches.json")]
            round_numbers = []
            for filename in match_files:
                round_number = int(filename.split('_')[1])  # Extraire le numéro du round du nom de fichier
                round_numbers.append(round_number)
            max_round = max(round_numbers)
            matches_data = []
            # Parcourir tous les fichiers de résultats des matchs
            for match_file in match_files:
                with open(os.path.join(tournament_dir, match_file), "r") as f:
                    matches_data.append(json.load(f))
            player_scores = {} # exemple {'AB12345': 1, 'AC12345': 4} -> identification_code : score
            # Parcours des données de match
            for matches in matches_data:
                for match in matches:
                    # Obtention des informations des joueurs et de leurs scores dans le match
                    player1_info = match['player1']
                    player2_info = match['player2']
                    # Mise à jour du score le plus élevé de chaque joueur
                    player_scores[player1_info['identification_code']] = max(player_scores.get(player1_info['identification_code'], float('-inf')), player1_info['score'])
                    player_scores[player2_info['identification_code']] = max(player_scores.get(player2_info['identification_code'], float('-inf')), player2_info['score'])
            round_instance = Round(players=PlayerModel().players_data, tournament=tournament)
            round_instance.set_score()
            new_list_players = []
            for player in round_instance.list_players:
                if player['identification_code'] in player_scores:
                    score_player = player_scores[player['identification_code']]
                    player['score'] = score_player
                    new_list_players.append(player)
            round_instance.list_players = new_list_players
            round_instance.new_combinaison_by_score()
            round_instance.actual_round = max_round
        except FileNotFoundError:
            round_instance = Round(players=PlayerModel().players_data, tournament=tournament)
            round_instance.set_score()
        return round_instance
    
    def create_tournament(self):
        input_view_create_tournament = tournamentView.CreateTournamentView(self)
        tournament = ModelCreateTournaments()
        return_result = tournament.setter_tournament(
            input_name=input_view_create_tournament[0], 
            input_location=input_view_create_tournament[1], 
            input_date_start=input_view_create_tournament[2], 
            input_date_end=input_view_create_tournament[3], 
            input_players_id=input_view_create_tournament[4], 
            input_description=input_view_create_tournament[5],                         
            input_num_rounds=input_view_create_tournament[6]
        )
        if return_result != False:
            tournament.save_tournament_to_json()
