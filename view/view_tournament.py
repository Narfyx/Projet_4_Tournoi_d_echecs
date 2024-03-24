"""tournament game display"""
from simple_term_menu import TerminalMenu

try:
    from view.view_main import ClearTerminal
except ModuleNotFoundError:
    from view_main import ClearTerminal

class TournamentView:
    """
    Class for displaying tournament-related views and collecting user inputs.
    """

    def start_tournament_view(self):
        """
        Displays the start tournament view.

        Returns:
            int: The index of the selected option.
        """
        ClearTerminal()
        print("==================")
        options = ["Create tournament", "Select and start tournament", "Return to main menu"]

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        return menu_entry_index

    def create_tournament_view(self):
        """
        Displays the create tournament view and collects user inputs.

        Returns:
            tuple: A tuple containing the tournament details entered by the user.
        """
        ClearTerminal()
        players = []

        print("======= CREATE TOURNAMENT =======")
        name = input("Enter the name : ")
        place = input("Enter the place : ")
        date_start = input("Enter date start tournament (format: DD/MM/YYYY) : ")
        date_end = input("Enter date end tournament (format: DD/MM/YYYY) : ")
        number_players = input("Enter number players : ")

        if number_players != '':
            for player in range(1, (int(number_players) + 1)):
                players.append(input(f"Enter identification code player {player} : "))
        else:
            number_players = None

        description = input("Please type a description for general remarks from the tournament director : ")

        num_rounds = input("Enter the number of revolutions (default = 4) : ")
        if num_rounds == '':
            num_rounds = '4'

        print("=========================================")
        input("Press keyboard")
        return name, place, date_start, date_end, players, description, num_rounds

    def show_tournaments(self, dataframe, selector):
        """
        Displays the list of tournaments and allows the user to select one.

        Args:
            dataframe (DataFrame): The DataFrame containing tournament data.
            selector (list): List of tournament names.

        Returns:
            int: The index of the selected tournament.
        """
        print("=========================================")
        print(dataframe)
        print("=========================================")
        options = selector

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        input("Press keyboard")
        ClearTerminal()
        return menu_entry_index

if __name__ == '__main__':
    print()
