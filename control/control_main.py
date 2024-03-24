import time

from view.view_main import ClearTerminal
from view.view_main import mainView #(StartView, StartTournamentView)

from control.control_player import controlPlayer #create_player
from control.control_tournament import controlTournament


class MainControl:
    """Contrôleur principal."""
    def __init__(self):
        self.run(mainView.StartView(self))

    def run(self, choice):
        """Run the App."""
        if choice == 0: # Add new player
            try:
                controlPlayer.create_player(self)
            except KeyboardInterrupt:
                MainControl()

            print("0 OK")
        elif choice == 1: # Tournaments
            try:
                controlTournament.tournament(self)
            except TypeError:
                MainControl()
            except KeyboardInterrupt:
                MainControl()
            
            MainControl()
        elif choice == 2: # Print all players
            controlPlayer.print_players(self)
        elif choice == 3: # Quit
            exit()
        exit()
