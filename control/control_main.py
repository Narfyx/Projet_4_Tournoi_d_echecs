"""main controler"""

from view.view_main import MainView

from control.control_player import ControlPlayer
from control.control_tournament import ControlTournament


class MainControl:
    """Contrôleur principal."""
    def __init__(self):
        self.run(MainView.start_view(self))

    def run(self, choice):
        """Run the App."""
        if choice == 0:  # Add new player
            try:
                ControlPlayer.create_player(self)
            except KeyboardInterrupt:
                MainControl()

            MainControl()
        elif choice == 1:  # Tournaments
            try:
                ControlTournament.tournament(self)
            except TypeError:
                MainControl()
            except KeyboardInterrupt:
                MainControl()
            MainControl()
        elif choice == 2:  # Print all players
            ControlPlayer.print_players(self)
            MainControl()
        elif choice == 3:  # Quit
            exit()
        exit()
