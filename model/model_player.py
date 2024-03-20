"""Player"""
import datetime
import re
import time
import json
import os
from colorama import Fore











class PlayerModel:
    """_summary_
    """
    def __init__(self, path_file="data/players/players.json"):
        if os.path.exists(path_file):
            with open(path_file) as file:
                self.players_data = json.load(file)
        else:
            self.players_data = []


    def setter_player(self, input_first_name=None, input_last_name=None, input_birth_date=None, input_identification_code=None):
        self.first_name = self._validate_name(input_first_name, "capitalize")
        self.last_name = self._validate_name(input_last_name, "upper")
        self.birth_date = self._validate_birth_date(input_birth_date)
        self.identification_code = self._validate_identification_code(input_identification_code)

        #si aucune des informations traité est considérer comme None dans ce cas il peut continuer
        #si None il s'arrête est demande à controleur recommencer la demande pour nouveau user



        if (self.first_name is None or
            self.last_name is None or
            self.birth_date is None or
            self.identification_code is None):

            
            return False

    def save_player_to_json(self, path_file="data/players/players.json"):
        player_data = {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "birth_date" : self.birth_date,
            "identification_code" : self.identification_code
        }

        self.players_data.append(player_data)

        with open(path_file, 'w') as file:
            json.dump(self.players_data, file, indent=4)
            print(Fore.GREEN + f"save player {self.identification_code} successfully" + Fore.RESET)



 












    # Validate func

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
        print(Fore.RED + "ERROR first name or last name invalid" + Fore.RESET)
        return None

    def _validate_identification_code(self, identification_code_str:str):

        pattern_code = re.compile("[A-Za-z0-9]+")
        pattern_code_alpha = re.compile("[A-Za-z]+")

        if (len(identification_code_str) != 7
                or (pattern_code_alpha.fullmatch(identification_code_str[:2])
                or pattern_code.fullmatch(identification_code_str)) is None):

            print(Fore.RED + "ERROR identification_code invalid" + Fore.RESET)
            return None

        
        for player in self.players_data:

            if player["identification_code"] == identification_code_str.upper():
                print(Fore.RED + "ERROR identification_code is already used" + Fore.RESET)
                return None
            
            return identification_code_str.upper()
        return identification_code_str.upper()
            
            



    


    def _validate_birth_date(self, birth_date_str:str):
        if birth_date_str is None:
            return None

        # Utilisez strptime pour parser la date à partir de la chaîne
        try:
            birth_date = datetime.datetime.strptime(birth_date_str, "%d/%m/%Y").date()

        except ValueError:
            print(Fore.RED + "ERROR birth date invalid" + Fore.RESET)
            return None


        # Récupérez les composants de la date
        day = birth_date.day
        month = birth_date.month
        year = birth_date.year
  
        return f"{day}/{month}/{year}"






if __name__ == '__main__':

   
    player1 = PlayerModel(path_file="../data/players/players.json")

    player1.setter_player(
        input_first_name="toto",
        input_last_name="tata",
        input_birth_date="10/10/2000",
        input_identification_code="ab12345"
    )
    print(player1.first_name)
    print(player1.last_name)
    if player1.setter_player != False:
        player1.save_player_to_json(path_file="../data/players/players.json")


    player2 = PlayerModel(path_file="../data/players/players.json")

    player2.setter_player(
        input_first_name="titi",
        input_last_name="tutu",
        input_birth_date="10/10/2000",
        input_identification_code="ac12345"
    )
    print(player2.first_name)
    print(player2.last_name)
    if player2.setter_player != False:
        player2.save_player_to_json(path_file="../data/players/players.json")

   