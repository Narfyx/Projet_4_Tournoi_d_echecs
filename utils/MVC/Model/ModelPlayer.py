import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils

import datetime
import re
import time
from colorama import Fore

class PlayerModel:
    def __init__(self, first_name="", last_name="", birth_date=None, identification_code=""):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = self._validate_birth_date(birth_date)
        self._identification_code = identification_code
        self._score = 0  # Ajout d'un attribut score


    # Getter methods
    def get_first_name(self) -> str:
        if self._first_name is not None:
            return f"First Name: {(self._first_name).capitalize()}"
        else:
            return None

    def get_last_name(self) -> str:
        if self._last_name is not None:
            return f"Last Name: {(self._last_name).upper()}"
        else:
            return None

    def get_birth_date(self) -> str:
        return self._birth_date

    def get_identification_code(self) -> str:
        return self._identification_code

    def get_score(self) -> int:
        return self._score



    # Setter methods
    def set_first_name(self, first_name):
        self._first_name = self._validate_name(first_name)

    def set_last_name(self, last_name):
        self._last_name = self._validate_name(last_name)

    def set_birth_date(self, birth_date):
        self._birth_date = self._validate_birth_date(birth_date)

    def set_identification_code(self, identification_code):

        self._identification_code = self._validate_identification_code(identification_code)

    def set_score(self, score):
        self._score = score


    # Validate func
    def _validate_name(self, name):
        pattern_name = re.compile("[A-Za-z]+")
        pattern_name.fullmatch(name)

        if pattern_name.fullmatch(name) is None:
            print(Fore.RED + "ERROR first name or last name invalid" + Fore.RESET)
            return None
        else:
            return name

    def _validate_identification_code(self, identification_code_str):
        
        pattern_code = re.compile("[A-Za-z0-9]+")
        pattern_code.fullmatch(identification_code_str)
  
        if len(identification_code_str) > 7 or len(identification_code_str) < 7 or pattern_code.fullmatch(identification_code_str) is None:
            print(Fore.RED + "ERROR identification_code invalid" + Fore.RESET)
            return None
        else:
            return f"Identification Code: {(identification_code_str)}"


    def _validate_birth_date(self, birth_date_str):
        if birth_date_str is None:
            return None

        # Utilisez strptime pour parser la date à partir de la chaîne
        try:
            birth_date = datetime.datetime.strptime(birth_date_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(Fore.RED + "ERROR invalid birth date. Date should be in the format 'DD/MM/YYYY'." + Fore.RESET)

        # Récupérez les composants de la date
        day = birth_date.day
        month = birth_date.month
        year = birth_date.year

        return (day, month, year)


    # Formatted func
    def formatted_birth_date(self):
        if self._birth_date is None:
            return None
        else:
            return f"Birth Date: ({self._birth_date[0]}, {self._birth_date[1]:02d}, {self._birth_date[2]})"


    
    

# Example usage:
if __name__ == "__main__":
    # Create an instance of the PlayerModel
    player = PlayerModel()

    # Set player attributes
    try:
        player.set_first_name(("jean"))
        player.set_last_name(("Dupont"))
        player.set_birth_date(("10/01/1999"))
        
    except ValueError as e:
        print(e)

    # Get and print player information
    print(player.get_first_name(), type(player.get_first_name()))
    print(player.get_last_name(), type(player.get_last_name()))
    print(player.formatted_birth_date(), type(player.formatted_birth_date()))
