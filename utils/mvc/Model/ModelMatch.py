"""
Un match unique doit être stocké sous la forme d'un tuple 
contenant deux listes, chacune contenant deux éléments : 
un joueur et un score. Les matchs doivent être stockés sous forme de 
liste dans l'instance du tour auquel ils appartiennent. En plus de la 
liste des matchs, chaque instance du tour doit contenir un nom. Actuellement, 
nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également 
contenir un champ Date 
et heure de début et un champ Date et heure de fin, qui doivent tous 
deux être automatiquement remplis lorsque l'utilisateur crée un tour 
et le marque comme terminé.
"""



import utils



class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.match = None
        self.score = 0  # Ajout d'un attribut score


    def init_match(self):
        # Chaque match consiste en une paire de joueurs.
        self.match = (
            [list(self.player1), 0],
            [list(self.player2), 0]
        )

    def update_player_scores(self, result_match):
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
        
        
        
        


    
    
    
    
    

        
