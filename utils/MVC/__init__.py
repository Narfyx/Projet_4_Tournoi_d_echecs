
#Fichiers
# Dans le fichier __init__.py du module

import os

def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Répertoire créé : {directory_path}")
    else:
        print(f"Le répertoire existe déjà : {directory_path}")

# Répertoire du script
script_directory = os.path.dirname(os.path.abspath(__file__))

parent_parent_directory = os.path.dirname(os.path.dirname(script_directory))
# Vérifiez la présence du fichier python.py
python_file_path = os.path.join(parent_parent_directory, "python.py")
if os.path.exists(python_file_path):
    print(f"Fichier python.py trouvé dans le répertoire : {script_directory}")
else:
    print("Erreur : Fichier python.py introuvable dans le répertoire.")
    input("Appuyez sur Entrée pour quit...")
    quit()

# Définissez les chemins des répertoires à créer
players_directory = os.path.join(script_directory, "../../data/players/")
tournaments_directory = os.path.join(script_directory, "../../data/tournaments/")

# Exécution du script pour créer les répertoires
create_directory_if_not_exists(players_directory)
create_directory_if_not_exists(tournaments_directory)



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


#Ordre d'exécution
#--View
input("Appuyez sur Entrée pour revenir au menu principal...")