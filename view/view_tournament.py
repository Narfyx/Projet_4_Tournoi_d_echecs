import os
import subprocess
from simple_term_menu import TerminalMenu

try:
    from view.view_main import ClearTerminal
except ModuleNotFoundError:
    from view_main import ClearTerminal

class tournamentView():
    def CreateTournamentView(self):

        ClearTerminal()
        players = []

        print("======= CREATE TOURNAMENT =======")
        name = input("Enter the name : ")
        place = input("Enter the place : ")
        date_start = input("Enter date start tournament (format: DD/MM/YYYY) : ")
        date_end = input("Enter date end tournament (format: DD/MM/YYYY) : ")
        number_players = input("Enter number players : ")

        if number_players != '':
            for player in range(1,(int(number_players)+1)):
                players.append(input(f"Enter identification code player {player} : "))
        else:
            number_players = None

        description = input("Please type a description for general remarks from the tournament director : ")
    
        print("The number of players must be greater than the number of rounds")
        num_rounds = input("Enter the number of revolutions (default = 4) : ")
        if num_rounds == '':
            num_rounds = '4'

        print("=========================================")
        input("Press Enter to return to the main menu...")
        return name, place, date_start, date_end, players, description, num_rounds




if __name__ == '__main__':
    affichage = tournamentView()
    name, place, date_start, date_end, players, description, num_rounds = affichage.CreateTournamentView()

    print(name)
    print(place)
    print(date_start)
    print(date_end)
    print(players)
    print(description)
    print(num_rounds)