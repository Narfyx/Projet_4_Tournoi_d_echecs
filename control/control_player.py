"""Controler players"""
import time
import pandas as pd

from model.model_player import PlayerModel

from view.view_player import PlayerView


class ControlPlayer():
    """controlPlayer"""
    def create_player(self):
        """Crée un nouveau joueur.

        Cette méthode démarre la vue pour ajouter un joueur en utilisant PlayerView.start_view_add_player,
        puis crée une instance de PlayerModel. Ensuite, elle appelle la méthode setter_player pour définir
        les attributs du joueur avec les informations fournies par l'utilisateur. Si la création du joueur
        échoue, elle attend 1 seconde et revient à la vue principale. Sinon, elle enregistre le joueur
        dans un fichier JSON à l'aide de la méthode save_player_to_json de la classe PlayerModel.

        """
        create_player = PlayerView.start_view_add_player(self)
        player = PlayerModel()

        status_create_player = player.setter_player(
            input_first_name=create_player[0],
            input_last_name=create_player[1],
            input_birth_date=create_player[2],
            input_identification_code=create_player[3])

        if status_create_player is False:
            time.sleep(1)
        else:
            player.save_player_to_json()

    def print_players(self):
        """Affiche les informations des joueurs.

        Cette méthode récupère les données des joueurs à partir du modèle PlayerModel,
        les convertit en DataFrame à l'aide de pandas, puis affiche les joueurs à l'aide
        de la méthode show_players de la vue des joueurs. Enfin, elle retourne à la vue
        principale.

        """
        df = pd.DataFrame(PlayerModel().players_data)
        PlayerView.show_players(self, dataframe=df)
