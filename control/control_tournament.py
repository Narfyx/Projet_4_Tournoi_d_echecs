"""controler tournaments"""
import os
import json
import pandas as pd

from model.model_player import PlayerModel
from model.tournament_manager import extract_tournaments_data
from model.model_tournaments import ModelCreateTournaments
from model.model_round import Round

from view.view_tournament import TournamentView
from view.view_rounds import RoundsView


class ControlTournament():
    """controlTournament"""
    def tournament(self):
        """tournament"""
        choice_tournament = TournamentView.start_tournament_view(self)
        if choice_tournament == 0:  # Create tournament
            ControlTournament.create_tournament(self)
        elif choice_tournament == 1:  # Select and start tournament -> Generate player pairs
            data_tournament = extract_tournaments_data()
            df = pd.DataFrame(data_tournament)
            selector_tournaments = [tournament['name'] for tournament in data_tournament]
            choice_tournament_select = TournamentView.show_tournaments(
                self,
                dataframe=df,
                selector=selector_tournaments
            )
            tournament_select = data_tournament[choice_tournament_select]
            ControlTournament.lancement_des_affrontements(self, tournament_select)
        elif choice_tournament == 2:  # Return to main menu
            pass

    def lancement_des_affrontements(self, tournament_select):
        """Lance les affrontements pour le tournoi sélectionné.

        Cette méthode commence par charger l'état actuel du tournoi en utilisant la fonction
        load_status du contrôleur de tournoi. Ensuite, elle affiche les paires de joueurs
        pour le tour actuel à l'aide de la vue des rounds. Les affrontements sont ensuite
        déclenchés en appelant la méthode affrontement de l'instance de Round. Si le nombre
        de paires de joueurs est supérieur à un, la méthode reconstitue les paires de joueurs
        en fonction des scores des joueurs, puis lance à nouveau les affrontements. Enfin, elle
        affiche les résultats finaux du tournoi triés par score et revient à la vue principale.

        Args:
            tournament_select (dict): Les informations sur le tournoi sélectionné.

        """
        tournament_select_rounds = ControlTournament.load_status(self, tournament=tournament_select)
        pair_information = tournament_select_rounds.players_pair
        RoundsView.display_pairs(self, data_pair=pair_information)
        tournament_select_rounds.affrontement()
        if len(tournament_select_rounds.players_pair) > 1:
            tournament_select_rounds.new_combinaison_by_score()
            pair_information = tournament_select_rounds.players_pair
            RoundsView.display_pairs(self, data_pair=pair_information)
            tournament_select_rounds.affrontement()
        # affichage de la fin du tournois
        tournament_select_rounds.list_players.sort(key=lambda x: x['score'], reverse=True)
        RoundsView.print_result(self, data_end_tournament=tournament_select_rounds.list_players)

    def load_status(self, tournament):
        """Charge l'état actuel du tournoi à partir des fichiers de résultats des matchs.

        Cette méthode charge l'état actuel du tournoi en récupérant les résultats des matchs
        précédents à partir des fichiers de résultats des matchs. Elle détermine le dernier
        tour joué en analysant les noms de fichiers pour extraire le numéro de tour le plus
        élevé. Ensuite, elle parcourt les fichiers de résultats des matchs pour mettre à jour
        les scores des joueurs en fonction des résultats des matchs précédents. Si aucun fichier
        de résultats n'est trouvé, elle crée une nouvelle instance de tour et initialise les
        scores des joueurs à zéro.

        Args:
            tournament (dict): Les informations du tournoi.

        Returns:
            Round: Une instance de la classe Round représentant l'état actuel du tournoi.

        """
        try:
            tournament_dir = f"data/tournaments_play/{tournament['name']}/"
            match_files = [
                f for f in os.listdir(tournament_dir) if f.startswith("round") and f.endswith("_matches.json")
            ]
            round_numbers = []
            for filename in match_files:
                round_number = int(filename.split('_')[1])  # Extraire le numéro du round du nom de fichier
                round_numbers.append(round_number)
            max_round = max(round_numbers)
            matches_data = []
            # Parcourir tous les fichiers de résultats des matchs
            for match_file in match_files:
                with open(os.path.join(tournament_dir, match_file), "r", encoding="utf-8") as f:
                    matches_data.append(json.load(f))
            player_scores = {}  # exemple {'AB12345': 1, 'AC12345': 4} -> identification_code : score
            # Parcours des données de match
            for matches in matches_data:
                for match in matches:
                    # Obtention des informations des joueurs et de leurs scores dans le match
                    player1_info = match['player1']
                    player2_info = match['player2']
                    # Mise à jour du score le plus élevé de chaque joueur

                    player_scores[player1_info['identification_code']] = max(
                        player_scores.get(
                            player1_info['identification_code'], float('-inf')), player1_info['score'])

                    player_scores[player2_info['identification_code']] = max(
                        player_scores.get(
                            player2_info['identification_code'], float('-inf')), player2_info['score'])

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
        """Crée un nouveau tournoi en récupérant les informations nécessaires depuis la vue.

        Cette méthode récupère les informations nécessaires à la création d'un tournoi à partir
        de la vue create_tournament_view. Elle utilise ensuite ces données pour instancier un objet
        ModelCreateTournaments, valide les informations fournies à l'aide de la méthode
        setter_tournament, et si toutes les informations sont valides, sauvegarde le tournoi
        au format JSON à l'aide de la méthode save_tournament_to_json.

        Returns:
            None

        """
        input_view_create_tournament = TournamentView.create_tournament_view(self)
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
        if return_result is not False:
            tournament.save_tournament_to_json()
