try:
    from model_player import PlayerModel
except ModuleNotFoundError:
    from model.model_player import PlayerModel
from pprint import pprint
from colorama import Fore


def validate_players_id(list_player=[]):
    """
    Validates the identification codes of players.

    Args:
        list_player (list): List of player identification codes.

    Returns:
        list or None: List of validated player identification codes (all uppercase) or None if validation fails.
    """
    players_data = PlayerModel().players_data
    list_player_upper = []
    for player_id in list_player:
        found = False

        for player in players_data:
            if player_id.upper() == player['identification_code']:
                found = True
                list_player_upper.append(player_id.upper())
                break

        if not found:
            print(Fore.RED + f"ERROR {player_id} is not found in players database" + Fore.RESET)
            return None
    return list_player_upper
    

if __name__ == '__main__':
    result = validate_players_id(list_player=["ab12345", "ac12345"])
    print(result)
