"""utils func for tournament"""
try:
    from model_tournaments import ModelCreateTournaments
except ModuleNotFoundError:
    from model.model_tournaments import ModelCreateTournaments


def extract_tournaments_data():
    """
    Extracts tournament data.

    Returns:
        dict: Tournament data.
    """
    tournament = ModelCreateTournaments()
    tournament_data = tournament.tournament_data
    return tournament_data
