import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils
import datetime, re, time, json, os
from colorama import Fore


class PlayerModel:
    def __init__(self, first_name="", last_name="", birth_date=None, identification_code=""):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = self._validate_birth_date(birth_date)
        self._identification_code = identification_code
        


    # Getter methods
    def get_first_name(self) -> str:
        if self._first_name is not None:
            return (self._first_name).capitalize()
        else:
            return None

    def get_last_name(self) -> str:
        if self._last_name is not None:
            return (self._last_name).upper()
        else:
            return None

    def get_birth_date(self) -> str:
        return self._birth_date

    def get_identification_code(self) -> str:
        return self._identification_code

    



    # Setter methods
    def set_first_name(self, first_name):
        self._first_name = self._validate_name(first_name)

    def set_last_name(self, last_name):
        self._last_name = self._validate_name(last_name)

    def set_birth_date(self, birth_date):
        self._birth_date = self._validate_birth_date(birth_date)

    def set_identification_code(self, identification_code):

        self._identification_code = self._validate_identification_code(identification_code)

    


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
        

        pattern_code_alpha = re.compile("[A-Za-z]+")
        

        if (len(identification_code_str) != 7 
                or (pattern_code_alpha.fullmatch(identification_code_str[:2]) == None 
                or pattern_code.fullmatch(identification_code_str) == None)):

            print(Fore.RED + "ERROR identification_code invalid" + Fore.RESET)
            return None


        else:
            return (identification_code_str.upper())


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
            return f"{self._birth_date[0]}, {self._birth_date[1]:02d}, {self._birth_date[2]}"




class WriteForBddPlayer:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_player(self, first_name, last_name, birth_date, identification_code):
        # Charger les données existantes depuis le fichier JSON
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # Créer un nouvel enregistrement pour le joueur
        player_record = {
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date,
            'identification_code': identification_code
        }

        # Ajouter le nouvel enregistrement à la liste des joueurs
        data['players'] = data.get('players', []) + [player_record]

        # Écrire les données mises à jour dans le fichier JSON
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=2)

