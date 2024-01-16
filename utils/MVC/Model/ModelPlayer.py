import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils
import datetime, re, time, json, os
from colorama import Fore


class PlayerModel:
    def __init__(self, first_name="", last_name="", birth_date=None, identification_code=""):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
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
        return self.formatted_date(self._birth_date)

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
        
        date_limite = datetime.date(1907, 3, 4)
        if birth_date < date_limite: #easter egg
            print(Fore.RED + "The date is earlier than 4 March 1907. You cannot enter a player older than Maria Branyas Morera :)" + Fore.RESET)
                    
            time.sleep(5)
            return None
        return (day, month, year)


    # Formatted func
    def formatted_date(self, date):
        if date is None:
            return None
        else:
            return f"{date[0]}, {date[1]:02d}, {date[2]}"
    @classmethod
    def create_from_dict(cls, player_data):
        # Méthode de classe pour créer une instance de PlayerModel à partir d'un dictionnaire
        return cls(
                        first_name=player_data.get('first_name'),
                        last_name=player_data.get('last_name'),
                        birth_date=player_data.get('birth_date'),
                        identification_code=player_data.get('identification_code')
                    )

    def get_player_info(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'identification_code': self.identification_code,
            'index': self.index
        }




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

        # Ajoute le nouvel enregistrement à la liste des joueurs
        data['players'] = data.get('players', []) + [player_record]

        # Écrire les données mises à jour dans le fichier JSON
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=2)



class ReadBddPlayerIfDuplicate:
    def __init__(self, file_path):
        self.file_path = file_path

    def is_bdd_not_empty(self):
            try:
                # Charge les données existantes depuis le fichier JSON
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                # Vérifie si la liste de joueurs n'est pas vide
                return bool(data.get('players', []))

            except FileNotFoundError:
                # Le fichier n'existe pas, donc la base de données est vide
                return False

    def check_duplicate(self, identification_code, first_name, last_name):
        # Charge les données existantes depuis le fichier JSON
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # Vérifie la présence d'un doublon pour identification_code
        for player in data.get('players', []):
            if player['identification_code'] == identification_code:
                print(Fore.RED + "Duplicate detected: identification_code already used." + Fore.RESET)
                return True
            if player['first_name'] == first_name and player['last_name'] == last_name:
                print(Fore.RED + "Duplicate detected: first_name and last_name combined already in use." + Fore.RESET)
                return True

        # Aucun doublon détecté
        return False


class ReadBddPlayer:
    def __init__(self, file_path):
        self.file_path = file_path
        
    
    def is_bdd_not_empty(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            try:
                # Charger les données existantes depuis le fichier JSON
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                # Vérifie si la liste de joueurs n'est pas vide
                return bool(data.get('players', []))

            except FileNotFoundError:
                # Le fichier n'existe pas, donc la base de données est vide
                return False
    
    def read_bdd_player(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def extract_player_in_bdd(self):
        bdd_player = self.read_bdd_player()
        obj_players = []
        for index, player_data in enumerate(bdd_player.get('players', [])):
            player_instance = PlayerModel().create_from_dict(player_data)
            obj_players.append({'index': index, 'player': player_instance})

        # Exemple d'utilisation : parcourir tous les joueurs
        for entry in obj_players:
            current_index = entry['index']
            current_player = entry['player']
            #print(f"Joueur {current_index}:", current_player.get_first_name(), current_player.get_last_name())

        return obj_players


def get_player_attributes_by_index(obj_players, index_to_consult):
    # Recherchez le joueur avec l'index spécifié
    player_dict = next((player_dict for player_dict in obj_players if player_dict['index'] == index_to_consult), None)

    # Vérifiez si le joueur a été trouvé
    if player_dict:
        # Retournez les attributs du joueur
        return {
            'first_name': player_dict['player']._first_name,
            'last_name': player_dict['player']._last_name,
            'birth_date': player_dict['player']._birth_date,
            'identification_code': player_dict['player']._identification_code,
            'index': player_dict['index']
        }
    else:
        # Si aucun joueur n'est trouvé, retournez None ou une valeur par défaut
        return None


