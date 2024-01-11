"""
pour la prochaine fois faire:
-match
-tournois
-BDD
-déplacer score de tournois et player vers match
-faire un system de rank dans player

Revue des modèles : match doit en lui-même gérer 
les points et ne pas retourner juste "draft", "win" 
ou "loss" par exemple. Fais en sorte que chacun "gère 
ce qui lui appartient" et parle de la meilleure manière 
à l'autre modèle pour qu'il n'est pas à retravailler les 
données gérées.
Revue d'autres problématiques sur les scores et les players. 
Pour moi si on veut une appli qui puisse évoluer cela doit 
se faire avec des scores de joueurs stockés au niveau du 
tournoi etc. Revérifie bien les critères tout le long pour 
ne pas t'en éloigner

3. Objectifs 'SMART' fixés par l'étudiant et le mentor 
pour la prochaine session

Avance sur la correction des modèles et continue à 
relier tes problématiques métiers et view contrôleur 
à ta logique de modèles



-REFAIRE LE SYSTEM QUI ENVOIE LES JOUEURS VERS LE STARTMATCH POUR QUE CE SOIT L'OBJET JOUEUR LUI MEME QUI EST UN SCORE
-STARTMATCH DOIT CE TROUVER DANS MODELTOURNAMENT
-LES OBJETS JOUEURS ET TOURNOIS DOIT ÊTRE RECHARGÉ EN MÉMOIRE AU LANCEMENT DU PROGRAM GRÂCE À JSON


-MATCH DOIT JUSTE ETRE CE QU IL EST
-ROUND EST CONSTITUER DE UN OU PLUSIEUR MATCH DÉFINIE PAR MODELTOURNAMENT


"""

#créer database pour les tournois et la création automatique dans le __init__.py
import utils.MVC.Control.ModelControl as home

def app():
    home.run()


if __name__ == '__main__':
    app()