import os
import json
import random
import pickle
import pandas as pd
import datetime
from pprint import pprint
from model.model_match import Match  # Import the Match class here
from view.view_rounds import roundsView


class Round():
    """Manages rounds in a tournament."""

    def __init__(self, players, tournament, file_dir='data/tournaments_play'):
        """Initialize Round object.

        Args:
            players (list): List of players participating in the tournament.
            tournament (dict): Information about the tournament.
            file_dir (str, optional): Directory path to store match data files. Defaults to 'data/tournaments_play'.
        """
        self.tournament = tournament
        self.list_players = [player for player in players if player['identification_code'] in self.tournament['players_id']]
        self.actual_round = 1
        random.shuffle(self.list_players)
        self.MAX_SCORE_DIFFERENCE = 2
        self.score = 0
        self.num_rounds = tournament['num_rounds']
        self.players_pair = []
        self.file_dir = file_dir

        num_pairs = len(self.list_players) // 2
        for i in range(num_pairs):
            pair = (self.list_players[i], self.list_players[num_pairs + i])
            self.players_pair.append(pair)

    def set_score(self):
        """Set initial scores for players."""
        for player in self.list_players:
            player.update({'score': self.score})

    def affrontement(self):
        """Handle matches between players."""
        while self.actual_round <= int(self.num_rounds):
            for pair in self.players_pair:
                date_launch_match = datetime.datetime.now()

                # Convert pair to DataFrame
                pair_df = pd.DataFrame(pair)

                # Get match result from roundsView
                rounds_view = roundsView()
                result_index = rounds_view.resultRoundsView(pair_df, pair_df['first_name'].tolist() + ['equal'])
                result_options = ["win", "loss", "draw"]
                match_result = result_options[result_index]

                # Create Match instance with players in the pair
                match = Match(player1=pair[0], player2=pair[1])

                # Update player scores based on match result
                match.result_match(match_result)

                date_end_match = datetime.datetime.now()

                # Save match result
                self.save_match_result({
                    "player1": pair[0],
                    "player2": pair[1],
                    "result": match_result,
                    "date_start": str(date_launch_match),
                    "date_end": str(date_end_match)
                })
            self.actual_round += 1

    def new_combinaison_by_score(self):
        """Arrange new pairs based on player scores."""
        self.list_players.sort(key=lambda x: x['score'], reverse=True)

        players = []
        for player in self.list_players:
            players.append(player)

        new_pair = []

        for player in range(0, len(players), 2):
            new_pair.append((players[player], players[player+1]))

        self.players_pair = new_pair
        self.actual_round = 1

    def save_match_result(self, match_result):
        """Save match result to a JSON file."""
        # Create directory for the tournament if it doesn't exist
        tournament_dir = os.path.join(self.file_dir, str(self.tournament['name']))
        if not os.path.exists(tournament_dir):
            os.makedirs(tournament_dir)

        # Create or open file to save match results
        match_file = os.path.join(tournament_dir, f"round_{self.actual_round}_{match_result['player1']['identification_code']}_vs_{match_result['player2']['identification_code']}_matches.json")
        if not os.path.exists(match_file):
            with open(match_file, "w") as f:
                # Start with an empty list if the file doesn't exist yet
                json.dump([], f)

        # Load previous results if they exist
        with open(match_file, "r") as f:
            previous_results = json.load(f)

        # Add new result to the list of previous results
        previous_results.append(match_result)

        # Write all results to the JSON file, encapsulated in a list
        with open(match_file, "w") as f:
            json.dump(previous_results, f, indent=4)
