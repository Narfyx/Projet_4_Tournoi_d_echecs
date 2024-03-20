"""fonctionnement d'un match"""
class Match:
    """_Match_"""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.match = None
        self.score = 0  # Ajout d'un attribut score
        self.result = None


    def init_match(self):
        """_Chaque match consiste en une paire de joueurs._"""

        self.match = (
            [list(self.player1), 0],
            [list(self.player2), 0]
        )

    def update_player_scores(self, result_match:str):
        """_update_player_scores_

        Args:
            result_match (str): _reçoit draw ou win ou loss_
        """
        self.result = result_match

        if result_match == "draw":
            #print("EQUALITE")
            for player_info in self.match:
                player_info[1] += 0.5


        elif result_match == "win":
            #print("JOUEUR 1 GAGNE")
            self.match[0][1] += 1


        elif result_match == "loss":
            #print("JOUEUR 2 GAGNE")
            self.match[1][1] += 1

        self.player1["score"] += self.match[0][1]
        self.player2["score"] += self.match[1][1]
