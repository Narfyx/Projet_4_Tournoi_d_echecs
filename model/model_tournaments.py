import datetime
import re
import json
import random
import os
from pprint import pprint
from colorama import Fore
try:
    from player_manager import validate_players_id
except ModuleNotFoundError:
    from model.player_manager import validate_players_id

class ModelCreateTournaments:
    """_summary_
    """
    def __init__(self, path_file="data/tournaments/tournaments.json"):
        if os.path.exists(path_file):
            with open(path_file) as file:
                self.tournament_data = json.load(file)
        else:
            self.tournament_data = []

    def setter_tournament(self, input_name=None, input_location=None, input_date_start=None, input_date_end=None, input_players_id=None, input_description=None, input_num_rounds=None):
        self.name = self._validate_name(input_name, "upper")
        self.location = self._validate_name(input_location, "capitalize")

        self.date_start = self._validate_date(input_date_start)
        self.date_end = self._validate_date(input_date_end)

        self.players_id = validate_players_id(list_player=input_players_id)
        self.description = input_description
        self.num_rounds = input_num_rounds
        
        #si aucune des informations traité est considérer comme None dans ce cas il peut continuer
        #si None il s'arrête est demande à controleur recommencer la demande pour nouveau user



        if (self.name is None or
            self.location is None or
            self.date_start is None or
            self.date_end is None or
            self.players_id is None or
            self.description is None or
            self.num_rounds is None):

            #print("Une valeur est None")
            #print(50*'-')
            #print(self.name)
            #print(self.location)
            #print(self.date_start)
            #print(self.date_end)
            #print(self.players_id)
            #print(self.description)
            #print(self.num_rounds)
            #print(50*'-')
            print(Fore.RED + "ERROR a variable is invalid set to None" + Fore.RESET)
            return False

    def save_tournament_to_json(self, path_file="data/tournaments/tournaments.json"):
            tournament_data = {
                "name" : self.name,
                "location" : self.location,
                "date_start" : self.date_start,
                "date_end" : self.date_end,
                "players_id" : self.players_id,
                "description" : self.description,
                "num_rounds" : self.num_rounds
            }

            self.tournament_data.append(tournament_data)

            with open(path_file, 'w') as file:
                json.dump(self.tournament_data, file, indent=4)
                print(Fore.GREEN + f"save tournament {self.name} successfully" + Fore.RESET)



    def _validate_name(self, name, type_name):
        pattern_name = re.compile("[A-Za-z-]+")
        pattern_name.fullmatch(name)

        if pattern_name.fullmatch(name) is not None:
            if type_name == "capitalize":
                return name.capitalize()
            elif type_name == "upper":
                return name.upper()
            else:
                print(Fore.RED + "ERROR with type_name" + Fore.RESET) #debug
        print(Fore.RED + "ERROR name or location invalid" + Fore.RESET)
        return None


    def _validate_date(self, date_tournament_str:str):
        if date_tournament_str is None:
            return None

        # Utilisez strptime pour parser la date à partir de la chaîne
        try:
            date_tournament = datetime.datetime.strptime(date_tournament_str, "%d/%m/%Y").date()

        except ValueError:
            print(Fore.RED + "ERROR date invalid" + Fore.RESET)
            return None


        # Récupérez les composants de la date
        day = date_tournament.day
        month = date_tournament.month
        year = date_tournament.year
  
        return f"{day}/{month}/{year}"


if __name__ == '__main__':

   
    tournament1 = ModelCreateTournaments() #path_file="../data/tournaments/tournaments.json"

    return_result = tournament1.setter_tournament(
        input_name="tournament-PARIS", 
        input_location="paris", 
        input_date_start="10/10/2000", 
        input_date_end="11/10/2000", 
        input_players_id=["ab12345", "ac12345"], 
        input_description="ceci est une description", 
        input_num_rounds="4"
    )
    
    print(tournament1.name)
    print(tournament1.location)
    if return_result != False:
        tournament1.save_tournament_to_json() #path_file="../data/tournaments/tournaments.json"


    tournament2 = ModelCreateTournaments() #path_file="../data/tournaments/tournaments.json"

    return_result = tournament2.setter_tournament(
        input_name="tournament-BERLIN", 
        input_location="berlin", 
        input_date_start="10/01/2000", 
        input_date_end="11/01/2000", 
        input_players_id=["ab12345", "ac12345", "ag12345", "af12345"], 
        input_description="ceci est une description 2", 
        input_num_rounds="8"
    )
    print(tournament2.name)
    print(tournament2.location)
    if return_result != False:
        tournament2.save_tournament_to_json() #path_file="../data/tournaments/tournaments.json"
