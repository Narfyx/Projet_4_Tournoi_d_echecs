import time
import pandas as pd


from model.model_player import PlayerModel
from model.model_tournaments import ModelCreateTournaments

from view.view_main import ClearTerminal
from view.view_main import mainView #(StartView, StartTournamentView)
from view.view_player import PlayerView #start_view_add_player
from view.view_tournament import tournamentView #CreateTournamentView

from control.control_main import mainView #create_player


class controlPlayer():
    def create_player(self):
        create_player = PlayerView.start_view_add_player(self)
        player = PlayerModel()
                
        status_create_player = player.setter_player(
            input_first_name=create_player[0],
            input_last_name=create_player[1],
            input_birth_date=create_player[2],
            input_identification_code=create_player[3])
                
                
        if status_create_player is False:
            time.sleep(1)
            self.run(mainView.StartView(self))
        else:
            player.save_player_to_json()

        
    def print_players(self):
        df = pd.DataFrame(PlayerModel().players_data)
        PlayerView.show_players(self, dataframe=df)
        self.run(mainView.StartView(self))