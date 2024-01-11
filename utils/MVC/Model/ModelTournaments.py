import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils
import datetime, re, time, json, os, random
from colorama import Fore



class ModelCreateTournaments:
    def __init__(self, name="", location="", date_start=None, date_end=None, num_rounds=4):
        self._name = name

        self._location = location
        self._date_start = date_start
        self._date_end = date_end
        self._num_rounds = num_rounds

    #Getter methods

    def get_name(self) -> str:
        if self._name is not None:
            return (self._name).capitalize()
        else:
            return None
    def get_location(self) -> str:
        if self._location is not None:
            return (self._location).capitalize()
        else:
            return None
    def get_date_start(self) -> str:
        return self.formatted_date(self._date_start)
    def get_date_end(self) -> str:
        return self.formatted_date(self._date_end)
    def get_num_rounds(self) -> int:
        return self._num_rounds

    
    # Setter methods
    def set_name(self, name):
        self._name = self._validate_full_alpha(name)


    def set_location(self, location):
        self._location = self._validate_full_alpha(location)

    def set_date_start(self, date_start):
        self._date_start = self._validate_date(date_start)
    
    def set_date_end(self, date_end):
        self._date_end = self._validate_date(date_end)

    def set_num_rounds(self, num_rounds):
        self._num_rounds = self._validate_num_rounds(num_rounds)



    # Validate func
    def _validate_full_alpha(self, alpha):
        pattern_alpha = re.compile("[A-Za-z]+")
        pattern_alpha.fullmatch(alpha)

        if pattern_alpha.fullmatch(alpha) is None:
            print(Fore.RED + f"ERROR '{alpha}' are invalid. Please enter alphabetic characters only !" + Fore.RESET)
            return None
        else:
            return alpha

    def _validate_date(self, date_str):
        if date_str is None:
            return None

        # Utilisez strptime pour parser la date à partir de la chaîne
        try:
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(Fore.RED + f"ERROR invalid '{date_str}' date. Date should be in the format 'DD/MM/YYYY'." + Fore.RESET)

        # Récupérez les composants de la date
        day = date.day
        month = date.month
        year = date.year

        return (day, month, year)

    def _validate_num_rounds(self, rounds):
        pattern_rounds = re.compile("[0-9]+")
        pattern_rounds.fullmatch(str(rounds))

        if pattern_rounds.fullmatch(str(rounds)) is None:
            print(Fore.RED + f"ERROR '{rounds}' are invalid. Please enter number only !" + Fore.RESET)
            return None
        else:
            if int(rounds) == 0:
                print(Fore.RED + f"ERROR '{rounds}' are invalid. The minimum for the round = 1 !" + Fore.RESET)
                return None
            return int(rounds)

    # Formatted func
    def formatted_date(self, date):
        if date is None:
            return None
        else:
            return f"{date[0]}, {date[1]:02d}, {date[2]}"
    


class WriteForBddTournaments:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_tournament(self, name, location, date_start, date_end, num_rounds):
        # Charger les données existantes depuis le fichier JSON
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # Créer un nouvel enregistrement pour le tournois
        Tournaments_record = {
            'name': name,
            'location': location,
            'date_start': date_start,
            'date_end': date_end,
            'num_rounds': num_rounds
        }

        # Ajouter le nouvel enregistrement à la liste des tournois
        data['Tournaments'] = data.get('Tournaments', []) + [Tournaments_record]

        # Écrire les données mises à jour dans le fichier JSON
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=2)



class ReadBddTournamentIfDuplicate:
    def __init__(self, file_path):
        self.file_path = file_path

    def is_bdd_not_empty(self):
            try:
                # Charger les données existantes depuis le fichier JSON
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                # Vérifier si la liste de tournois n'est pas vide
                return bool(data.get('Tournaments', []))

            except FileNotFoundError:
                # Le fichier n'existe pas, donc la base de données est vide
                return False

    def check_duplicate(self, name, location, date_start):
        # Charger les données existantes depuis le fichier JSON
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # Vérifier la présence d'un doublon 
        for Tournaments in data.get('Tournaments', []):
            if (Tournaments['name'] == name and 
                Tournaments['location'] == location and
                Tournaments['date_start'] == date_start):
                print(Fore.RED + "Doublon détecté : Ce tournois est déjà utilisé." + Fore.RESET)
                return True


        # Aucun doublon détecté
        return False


class ReadBddTournaments:
    def __init__(self, file_path):
        self.file_path = file_path
        
    
    def is_bdd_not_empty(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            try:
                # Charger les données existantes depuis le fichier JSON
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                # Vérifier si la liste de tournois n'est pas vide
                return bool(data.get('Tournaments', []))

            except FileNotFoundError:
                # Le fichier n'existe pas, donc la base de données est vide
                return False
    
    def read_bdd_Tournaments(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data



class RandomizePlayerListAndCreatePair:
    def __init__(self, players_list=None):
        self.players_list = players_list
        random.shuffle(self.players_list)

    def generate_random_pairs(self):
        
        if self.players_list == None:
            return None

        
        # Assurez-vous que la liste de joueurs a une longueur paire
        if len(self.players_list) % 2 != 0:
            raise ValueError("Le nombre de joueurs doit être pair.")#GERER LE CAS D UN NOMBRE IMPAIRE DE JOUEUR QUI VA EXCLURE UN JOUEUR DU TOURNOIS

        pair = []
        
        iterator = iter(self.players_list)

        while True:#Obliger pour cette méthode car un for i in range(0, len(self.players_list), 2) créer une erreur NoneType du au random.shuffle(self.players_list)
            try:
                player_impair = next(iterator)
                player_pair = next(iterator)
                pair.append((player_impair, player_pair))
            except StopIteration:
                # Arrête la boucle s'il n'y a plus d'éléments dans la liste
                break
        return pair


class StartMatch:#RENOMMER STARTMATCH EN ADDSCORE
    def __init__(self, player_dict=dict):
        self.score = 0
        self.player = player_dict
        
    def attribut_score(self):
        self.player['score'] = self.score
        
        return self.player
            

    
