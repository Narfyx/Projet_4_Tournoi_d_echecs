"""model tournament"""
import datetime
import json
import os
import re
from colorama import Fore
from model.player_manager import validate_players_id


class ModelCreateTournaments:
    """Model for creating tournaments."""
    def __init__(self, path_file="data/tournaments/tournaments.json"):
        """Initialize tournament data."""
        if os.path.exists(path_file):
            with open(path_file, encoding="utf-8") as file:
                self.tournament_data = json.load(file)
        else:
            self.tournament_data = []
        self.name = None
        self.location = None
        self.date_start = None
        self.date_end = None
        self.players_id = None
        self.description = None
        self.num_rounds = None

    def setter_tournament(self, input_name=None, input_location=None, input_date_start=None,
                          input_date_end=None, input_players_id=None, input_description=None,
                          input_num_rounds=None):
        """Set tournament attributes."""
        self.name = self._validate_name(input_name, "upper")
        self.location = self._validate_name(input_location, "capitalize")
        self.date_start = self._validate_date(input_date_start)
        self.date_end = self._validate_date(input_date_end)
        self.players_id = validate_players_id(list_player=input_players_id)
        self.description = input_description
        self.num_rounds = input_num_rounds

        if any(info is None for info in (self.name, self.location, self.date_start,
                                         self.date_end, self.players_id, self.description,
                                         self.num_rounds)):
            print(Fore.RED + "ERROR a variable is invalid set to None" + Fore.RESET)
            return False

    def save_tournament_to_json(self, path_file="data/tournaments/tournaments.json"):
        """Save tournament data to JSON."""
        tournament_data = {
            "name": self.name,
            "location": self.location,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "players_id": self.players_id,
            "description": self.description,
            "num_rounds": self.num_rounds
        }

        self.tournament_data.append(tournament_data)

        with open(path_file, 'w', encoding="utf-8") as file:
            json.dump(self.tournament_data, file, indent=4)
            print(Fore.GREEN + f"save tournament {self.name} successfully" + Fore.RESET)

    def _validate_name(self, name, type_name):
        """Validate name or location."""
        pattern_name = re.compile("[A-Za-z-]+")
        if pattern_name.fullmatch(name):
            if type_name == "capitalize":
                return name.capitalize()
            elif type_name == "upper":
                return name.upper()
            else:
                print(Fore.RED + "ERROR with type_name" + Fore.RESET)
        print(Fore.RED + "ERROR name or location invalid" + Fore.RESET)
        return None

    def _validate_date(self, date_tournament_str: str):
        """Validate tournament date."""
        if date_tournament_str is None:
            return None

        try:
            date_tournament = datetime.datetime.strptime(date_tournament_str, "%d/%m/%Y").date()

        except ValueError:
            print(Fore.RED + "ERROR date invalid" + Fore.RESET)
            return None

        day = date_tournament.day
        month = date_tournament.month
        year = date_tournament.year

        return f"{day}/{month}/{year}"
