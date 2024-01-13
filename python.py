"""
manque plus que:
-PEP 8
-flake8-html
-enregistrement en temps réel ou cas le programme est arrêter
-finir/corriger la partie qui évite que deux joueur s'affronte de nouveau
-modifier les franglais -> anglais
"""

#créer database pour les tournois et la création automatique dans le __init__.py
import utils.MVC.Control.ModelControl as home

def app():
    home.run()


if __name__ == '__main__':
    app()