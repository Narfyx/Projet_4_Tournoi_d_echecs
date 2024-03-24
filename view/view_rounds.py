import os
import subprocess
import pandas as pd
from simple_term_menu import TerminalMenu

try:
    from view.view_main import ClearTerminal
except ModuleNotFoundError:
    from view_main import ClearTerminal


class RoundsView:
    """
    Class for displaying round-related views and collecting user inputs.
    """

    def result_rounds_view(self, dataframe, selector):
        """
        Displays the result of rounds view.

        Args:
            dataframe (DataFrame): The DataFrame containing round data.
            selector (list): List of round results.

        Returns:
            int: The index of the selected round result.
        """
        print("=========================================")
        print(dataframe)
        print("=========================================")

        options = [(selector[0] + " gagne"), (selector[1] + " gagne"), "equal"]

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        input("Press keyboard")
        return menu_entry_index

    def display_pairs(self, data):
        """
        Displays the pairs for the round.

        Args:
            data (list): List of player pairs for the round.
        """
        ClearTerminal()
        print("=========================================")
        for pair in data:
            print("\n")
            dataframe = pd.DataFrame(pair)
            print(f"Affrontement {pair[0]['first_name']} VS {pair[1]['first_name']}")
            print(dataframe)
            print("\n")

        print("=========================================")
        input("Press keyboard")

    def print_result(self, data):
        """
        Prints the result of the round.

        Args:
            data (list): List containing the result of the round.
        """
        ClearTerminal()
        print("=========================================")
        print(f"Winner is {data[0]['first_name']} !")
        print("=========================================")
        dataframe = pd.DataFrame(data)
        print(dataframe)
        print("=========================================")
        input("Press keyboard")


if __name__ == '__main__':
    data = [
        (
            {
                'birth_date': '10/10/2000',
                'first_name': 'Tutu',
                'identification_code': 'AG12345',
                'last_name': 'TYTY',
                'score': 0
            },
            {
                'birth_date': '10/10/2000',
                'first_name': 'Zozo',
                'identification_code': 'AK12345',
                'last_name': 'ZAZA',
                'score': 0
            }
        ),
        (
            {
                'birth_date': '10/10/2000',
                'first_name': 'Toto',
                'identification_code': 'AB12345',
                'last_name': 'ABC',
                'score': 0
            },
            {
                'birth_date': '10/10/2000',
                'first_name': 'Titi',
                'identification_code': 'AC12345',
                'last_name': 'XYZ',
                'score': 0
            }
        )
    ]
    # RoundsView().display_pairs(data=data)
