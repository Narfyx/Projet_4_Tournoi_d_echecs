import utils


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None  # À la fin du match, les joueurs reçoivent des points selon leurs résultats. ---○ Le gagnant reçoit 1 point. ---○ Le perdant reçoit 0 point. ---○ Chaque joueur reçoit 0,5 point si le match se termine par un match nul.

    def create_match(self, player1, player2): # Chaque match consiste en une paire de joueurs.
        match = Match(player1, player2)
        self.rounds[self.current_round_number - 1].matches.append(match)
    
    def record_match_result(self, match_index, result):
        match = self.rounds[self.current_round_number - 1].matches[match_index]
        match.result = result
        self._update_player_scores(match)  # Un tournoi a un nombre de tours défini. ---○ Chaque tour est une liste de matchs.