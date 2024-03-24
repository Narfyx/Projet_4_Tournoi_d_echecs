"""fonctionnement d'un match"""


class Match:
    """Classe représentant un match entre deux joueurs."""

    def __init__(self, player1, player2):
        """Initialise un match avec les deux joueurs."""
        self.player1 = player1
        self.player2 = player2

    def result_match(self, result):
        """Met à jour les scores des joueurs en fonction du résultat du match.

        Args:
            result (str): Résultat du match ('draw', 'win', ou 'loss').
        """
        if result == "draw":
            self.player1["score"] += 0.5
            self.player2["score"] += 0.5
        elif result == "win":
            self.player1["score"] += 1
        elif result == "loss":
            self.player2["score"] += 1

        # Afficher les scores mis à jour
