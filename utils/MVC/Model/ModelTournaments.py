import utils




class ModelTournaments:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round_number = 1
        self.rounds = [ModelRound(round_number) for round_number in range(1, num_rounds + 1)]
        self.registered_players = []
        self.description = description

    def register_player(self, player):
        self.registered_players.append(player)


    

    def display_tournament_info(self):
        print("Tournament Information:")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Number of Rounds: {self.num_rounds}")
        print(f"Current Round: {self.current_round_number}")
        print(f"Description: {self.description}")
        print("\nRegistered Players:")
        for player in self.registered_players:
            print(f"{player.get_first_name()} {player.get_last_name()} (Score: {player.get_score()})")  # DÉROULEMENT DE BASE DU TOURNOI: ---○ Une liste des joueurs enregistrés.

        print("\nRound Information:")
        for round in self.rounds:
            print(f"\nRound {round.round_number} Matches:")
            for match in round.matches:
                print(f"{match.player1.get_first_name()} {match.player1.get_last_name()} vs. "
                      f"{match.player2.get_first_name()} {match.player2.get_last_name()}: {match.result}")


# Example usage:
if __name__ == "__main__":
    # Create an instance of the ModelTournaments
    tournament = ModelTournaments(
        name="Chess Tournament",
        location="City Hall",
        start_date="2023-01-01",
        end_date="2023-01-07",
        num_rounds=3,
        description="Chess competition for all levels"
    )

    # Register players
    player1 = PlayerModel("John", "Doe", ('15', '05', 1990))
    player2 = PlayerModel("Alice", "Smith", ('20', '08', 1995))
    tournament.register_player(player1)
    tournament.register_player(player2)

    # Create matches for the first round
    tournament.create_match(player1, player2)

    # Record match results
    tournament.record_match_result(0, "draw")

    # Display tournament information
    tournament.display_tournament_info()