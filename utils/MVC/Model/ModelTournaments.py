import sys
sys.path.append("../../../utils")  # Ajoute le chemin du module parent au chemin de recherche de modules
import utils
import datetime, re, time, json, os, random, itertools
from colorama import Fore
from pprint import pprint


class SetTournamentToFinishInBdd:
    def __init__(self):
        pass
        
    def change_to_finish(self, file_path, index):
        #if self.tournament_selected['finish'] == False:
        print(file_path)
        print(index) 

        # Étape 1 : Ouvrir le fichier en mode lecture
        with open(file_path, 'r') as fichier:
            # Étape 2 : Charger le contenu JSON dans une structure de données Python
            donnees = json.load(fichier)
            
            # Étape 3 : Modifier la structure de données
            donnees['Tournaments'][index]['finish'] = True

        # Étape 4 : Ouvrir le fichier en mode écriture et écrire les modifications
        with open(file_path, 'w') as fichier:
            json.dump(donnees, fichier, indent=2)

    

class ModelCreateTournaments:
    def __init__(self, name="", location="", date_start=None, date_end=None, num_rounds=4):
        self._name = name

        self._location = location
        self._date_start = date_start
        self._date_end = date_end
        self._num_rounds = num_rounds
        self._finish_tournament = False

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
    def get_tournament_is_finish(self) -> bool:
        return self._finish_tournament

    
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
    
    def set_is_finish(self, json_file_path_tournaments, index):
        self._finish_tournament = True
        i = SetTournamentToFinishInBdd.change_to_finish(self,file_path=json_file_path_tournaments,index=index)
        





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

    def write_tournament(self, name, location, date_start, date_end, num_rounds, is_finish):
        # Charger les données existantes depuis le fichier JSON
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        # Créer un nouvel enregistrement pour le tournois
        Tournaments_record = {
            'name': name,
            'location': location,
            'date_start': date_start,
            'date_end': date_end,
            'num_rounds': num_rounds,
            'finish': is_finish
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

class MemorizePair:
    def __init__(self):
        self.actual_pair = None
        self.old_pairs = []
        

    def set_actual_pair(self, new_pairs):
        self.actual_pair = new_pairs
        print(100*'/')
        pprint(f"OLD_PAIR = {self.old_pairs}")
        print(100*'/')
        print(100*'/')
        pprint(f"ACTUAL_PAIR = {self.actual_pair}")
        print(100*'/')
        if self.actual_pair in self.old_pairs:
            return False
        else:
            self.old_pairs.append(self.actual_pair)
            return True
        



class RandomizePlayerListAndCreatePair:
    def __init__(self, players_list=None):
        self.players_list = players_list
        random.shuffle(self.players_list)
        self.pair_memorizer = MemorizePair()

    def generate_random_pairs(self):
        if self.players_list is None:
            return None

        # Génération des paires
        pairs = self._generate_pairs()

        

        return pairs
    
    def generate_pairs_by_score(self):
        if self.players_list is None:
            return None

        # Trie des joueurs par score décroissant
        sorted_players = sorted(self.players_list, key=lambda x: x['score'], reverse=True)
        self.players_list = sorted_players
        # Génération des paires avec la liste triée
        pairs = self._generate_pairs()
        if pairs == None:
            return None
        

        return pairs

    def _generate_pairs(self):
        
        
        pairs = []
        iterator = iter(self.players_list)
        while True:
            try:
                player_pair = next(iterator)
                player_impair = next(iterator, None)
                
                new_pair = (player_pair, player_impair)
                
                pairs.append(new_pair)
                check_if_created = self.pair_memorizer.set_actual_pair(new_pair)
                print(100*'*')
                print(check_if_created)
                print(100*'*')
                if check_if_created == False:
                    # Réessayer avec une nouvelle paire
                    random.shuffle(self.players_list)
                    iterator = iter(self.players_list)
                    check_if_created = self.pair_memorizer.set_actual_pair(new_pair)
                    if check_if_created == False:
                        pairs = None
                        break
                """
                else:
                    # Réessayer avec une nouvelle paire
                    random.shuffle(self.players_list)
                    iterator = iter(self.players_list)
                    check_if_created = self.pair_memorizer.set_actual_pair(new_pair)
                """   
            except StopIteration:
                break

        


        return pairs

    def _pairs_are_duplicate(self, new_pairs):
        # Vérifie si les nouvelles paires sont en double par rapport aux anciennes
        if hasattr(self, 'previous_pairs') and new_pairs == self.previous_pairs:
            return True
        self.previous_pairs = new_pairs
        return False



class StartMatch:#RENOMMER STARTMATCH EN ADDSCORE
    def __init__(self, player_dict=dict):
        self.score = 0
        self.player = player_dict
        
    def attribut_score(self):
        self.player['score'] = self.score
        
        return self.player
            
def trier_par_score(liste):
    return sorted(liste, key=lambda x: x['score'], reverse=True)
    
