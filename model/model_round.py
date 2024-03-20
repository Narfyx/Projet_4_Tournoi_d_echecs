"""
Module datetime - Fonctionnalités de gestion des dates et heures.
"""
import datetime

class ModelRound:
    """_ModelRound_"""
    def __init__(self):
        self.matches = []
        self.debut = None
        self.fin = None
        self.tour_actuel = 1
        self.nom = f"Round {self.tour_actuel}"


    def marquer_commence(self):
        """_marquer_commence_"""
        self.debut = datetime.datetime.now
        self.nom = f"Round {self.tour_actuel}"


    def marquer_termine(self):
        """_marquer_termine_"""
        self.fin = datetime.datetime.now
        self.tour_actuel += 1
