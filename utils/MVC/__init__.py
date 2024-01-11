
#Fichiers
# Dans le fichier __init__.py du module

import json
import os
from pprint import pprint
PLAYER_DIRECTORY = "data/players/"
TOURNAMENTS_DIRECTORY = "data/tournaments/"
script_directory = os.path.dirname(os.path.abspath(__file__))

def create_directory_if_not_exists(directory_path, script_directory):
    
    
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Répertoire créé : {directory_path}")
    else:
        print(f"Le répertoire existe déjà : {directory_path}")






class JSONDatabase:
    def __init__(self, directory_path, entity):
        self.file_path = os.path.join(directory_path, entity + '.json')
        self.data = {}
        # Répertoire du script
        script_directory = os.path.dirname(os.path.abspath(__file__))

        parent_parent_directory = os.path.dirname(os.path.dirname(script_directory))

        if "data/players/" in directory_path:
            python_file_path = os.path.join(parent_parent_directory, "python.py")


        if "data/tournaments/" in directory_path:
            python_file_path = os.path.join(parent_parent_directory, "tournaments.py")




        if os.path.exists(python_file_path):
            print(f"Fichier python.py trouvé dans le répertoire : {script_directory}")

    
    def create_database(self):
        # Assurez-vous que le répertoire existe
        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.exists(self.file_path):
            print(f"La base de données existe déjà dans {directory}")
        else:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file)
            print(f"Base de données créée avec succès à l'emplacement : {self.file_path}")

# répertoires à créer
players_directory = os.path.join(script_directory, "../../" + PLAYER_DIRECTORY)
tournaments_directory = os.path.join(script_directory, "../../" + TOURNAMENTS_DIRECTORY)

# créer les répertoires
create_directory_if_not_exists(players_directory,script_directory)
create_directory_if_not_exists(tournaments_directory, script_directory)

# JSON Player:
db = JSONDatabase(directory_path=PLAYER_DIRECTORY, entity='players')
db.create_database()
# JSON Tournaments:
db = JSONDatabase(directory_path=TOURNAMENTS_DIRECTORY, entity='tournaments')
db.create_database()

#--Model
import utils.MVC.Model.ModelMatch
import utils.MVC.Model.ModelPlayer
import utils.MVC.Model.ModelRound
import utils.MVC.Model.ModelTournaments





#--View
import utils.MVC.View.ModelView

#--Control
import utils.MVC.Control.ModelControl



#Modules


#Constantes


#Recharge en mémoire






#--View
input("Appuyez sur Entrée pour revenir au menu principal...")