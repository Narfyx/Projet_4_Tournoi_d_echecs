try:
    from model_tournaments import ModelCreateTournaments
except ModuleNotFoundError:
    from model.model_tournaments import ModelCreateTournaments
from pprint import pprint
from colorama import Fore
import json
from types import SimpleNamespace

def extract_tournaments_data():
    """
    Extracts tournament data.

    Returns:
        dict: Tournament data.
    """
    tournament = ModelCreateTournaments()
    data = tournament.tournament_data
    return data


def convert_data_json_to_obj(data):
    """
    Convertit des données JSON en objet Python en utilisant SimpleNamespace.

    Args:
        data (str): Une chaîne JSON représentant les données à convertir.

    Returns:
        types.SimpleNamespace: Un objet SimpleNamespace contenant les données converties.

    Examples:
        >>> data = '{
        'name': 'TOURNEMENT-PARIS', 
        'location': 'Paris', 
        'date_start': '10/10/2000', 
        'date_end': '11/10/2000', 
        'players_id': ['AB12345', 'AC12345'], 
        'description': 'ceci est une description', 
        'num_rounds': '4'
    }'
        >>> obj = convert_data_json_to_obj(data)
        >>> obj.name
        'TOURNEMENT-PARIS'
        >>> obj.location
        'Paris'
        >>> obj.date_start
        '10/10/2000'
        >>> obj.date_end
        '11/10/2000'
        >>> obj.players_id
        ['AB12345', 'AC12345']
        >>> obj.description
        'ceci est une description'
        >>> obj.num_rounds
        '4'

    """
    return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


if __name__ == '__main__':
    data = {
        'name': 'TOURNEMENT-PARIS', 
        'location': 'Paris', 
        'date_start': '10/10/2000', 
        'date_end': '11/10/2000', 
        'players_id': ['AB12345', 'AC12345'], 
        'description': 'ceci est une description', 
        'num_rounds': '4'
    }

    obj = convert_data_json_to_obj(json.dumps(data))
    
    print("After conversion:")
    print("Name:", obj.name)
    print("Location:", obj.location)
    print("Date Start:", obj.date_start)
    print("Date End:", obj.date_end)
    print("Players ID:", obj.players_id)
    print("Description:", obj.description)
    print("Num Rounds:", obj.num_rounds)



