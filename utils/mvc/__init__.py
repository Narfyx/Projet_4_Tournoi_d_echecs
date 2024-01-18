"""
Ce module regroupe des fonctionnalités liées à la conception du modèle MVC (Modèle-Vue-Contrôleur)
pour la gestion de matchs, joueurs, tours et tournois dans une application de tournoi d'échec.

Il inclut les modules suivants :
- ModelMatch : Gestion des données relatives aux matchs.
- ModelPlayer : Gestion des données relatives aux joueurs.
- ModelRound : Gestion des données relatives aux tours.
- ModelTournaments : Gestion des données relatives aux tournois.
- ModelView : Implémentation de la vue pour la représentation graphique des données.
- ModelControl : Contrôleur pour la liaison entre les Modeles et la Vue.

Ce module utilise les modules externes suivants :
- json : Pour la sérialisation et la désérialisation des données au format JSON.
- os : Pour les opérations liées au système d'exploitation.
- pprint : Pour une impression plus lisible des structures de données.
"""


import json
import os
from pprint import pprint
import utils.mvc.Model.ModelMatch
import utils.mvc.Model.ModelPlayer
import utils.mvc.Model.ModelRound
import utils.mvc.Model.ModelTournaments
import utils.mvc.View.ModelView
import utils.mvc.Control.ModelControl


PLAYER_DIRECTORY = "data/players/"
TOURNAMENTS_DIRECTORY = "data/tournaments/"
script_directory = os.path.dirname(os.path.abspath(__file__))

def create_directory_if_not_exists(directory_path : str):
    """_summary_

    Args:
        directory_path (str): _File directory_
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Répertoire créé : {directory_path}")
    else:
        print(f"Le répertoire existe déjà : {directory_path}")





class JSONDatabase:
    """_JSONDatabase_"""

    def __init__(self, directory_path, entity):
        self.file_path = os.path.join(directory_path, entity + '.json')
        self.data = {}
        # Répertoire du script
        directory = os.path.dirname(os.path.abspath(__file__))

        parent_parent_directory = os.path.dirname(os.path.dirname(directory))

        if "data/players/" in directory_path:
            python_file_path = os.path.join(parent_parent_directory, "python.py")


        if "data/tournaments/" in directory_path:
            python_file_path = os.path.join(parent_parent_directory, "tournaments.py")




        if os.path.exists(python_file_path):
            print(f"Fichier python.py trouvé dans le répertoire : {directory}")


    def create_database(self):
        """_create JSON database_"""
        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if os.path.exists(self.file_path):
            print(f"La base de données existe déjà dans {directory}")
        else:
            with open(self.file_path,'w', encoding="utf-8") as file:
                json.dump(self.data, file)
            print(f"Base de données créée avec succès à l'emplacement : {self.file_path}")

# répertoires à créer
players_directory = os.path.join(script_directory, "../../" + PLAYER_DIRECTORY)
tournaments_directory = os.path.join(script_directory, "../../" + TOURNAMENTS_DIRECTORY)

# créer les répertoires
create_directory_if_not_exists(players_directory)
create_directory_if_not_exists(tournaments_directory)

# JSON Player:
db = JSONDatabase(directory_path=PLAYER_DIRECTORY, entity='players')
db.create_database()
# JSON Tournaments:
db = JSONDatabase(directory_path=TOURNAMENTS_DIRECTORY, entity='tournaments')
db.create_database()


input("Appuyez sur Entrée pour revenir au menu principal...")
