import time

from model.model_player import PlayerModel

from model.model_tournaments import ModelCreateTournaments

from view.view_main import ClearTerminal
from view.view_main import mainView #(StartView, StartTournamentView)
from view.view_player import PlayerView #start_view_add_player
from view.view_tournament import tournamentView #CreateTournamentView

from control.control_main import mainView #create_player


class controlTournament():
    def tournament(self):
        choice_tournament = mainView.StartTournamentView(self)
        if choice_tournament == 0: #Create tournament
            input_view_create_tournament = tournamentView.CreateTournamentView(self)
            tournament = ModelCreateTournaments() #path_file="../data/tournaments/tournaments.json"

            return_result = tournament.setter_tournament(
                input_name=input_view_create_tournament[0], 
                input_location=input_view_create_tournament[1], 
                input_date_start=input_view_create_tournament[2], 
                input_date_end=input_view_create_tournament[3], 
                input_players_id=input_view_create_tournament[4], 
                input_description=input_view_create_tournament[5],                         
                input_num_rounds=input_view_create_tournament[6]
            )
                        
            print(tournament.name)
            print(tournament.location)
            if return_result != False:
                tournament.save_tournament_to_json() #path_file="../data/tournaments/tournaments.json"
            exit()
        elif choice_tournament == 1: #Generate player pairs
            pass
        elif choice_tournament == 2: #Enter the results of a round
            pass
        elif choice_tournament == 3: #Return to main menu
            self.run(mainView.StartView())