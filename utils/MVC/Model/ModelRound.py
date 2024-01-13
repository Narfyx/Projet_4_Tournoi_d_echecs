"""
Un match unique doit être stocké sous la forme d'un tuple 
contenant deux listes, chacune contenant deux éléments : 
un joueur et un score. Les matchs doivent être stockés sous forme de 
liste dans l'instance du tour auquel ils appartiennent. En plus de la 
liste des matchs, chaque instance du tour doit contenir un nom. Actuellement, 
nous appelons nos tours "Round 1", "Round 2", etc. Elle doit également 
contenir un champ Date et heure de début et un champ Date et heure de fin, 
qui doivent tous deux être automatiquement remplis 
lorsque l'utilisateur crée un tour 
et le marque comme terminé.
"""

import utils, datetime

class ModelRound:
    def __init__(self):
        self.matches = []
        self.debut = None
        self.fin = None
        self.tour_actuel = 1
        self.nom = f"Round {self.tour_actuel}"
        

    def marquer_commence(self):
        self.debut = datetime.datetime.now
        self.nom = f"Round {self.tour_actuel}"
        

    def marquer_termine(self):
        self.fin = datetime.datetime.now
        self.tour_actuel += 1
        


   