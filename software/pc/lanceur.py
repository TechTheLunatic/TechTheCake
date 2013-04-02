
#passage de la couleur
couleur = ""
while couleur != "rouge" and couleur != "bleu":
    couleur = input("Quelle couleur? bleu ou rouge >")
import builtins
builtins.couleur_robot = couleur

#module d'injection de dépendances
from src.container import *
from time import time


ennemi_fait_toutes_bougies = ""
while ennemi_fait_toutes_bougies != "1" and ennemi_fait_toutes_bougies != "0":
    ennemi_fait_toutes_bougies = input("L'ennemi fait-il toutes les bougies? 1 (oui) ou 0 (non) >")
    
container = Container()

#module de la stratégie
config = container.get_service("config")
config["couleur"] = couleur
config["ennemi_fait_toutes_bougies"] = bool(int(ennemi_fait_toutes_bougies))
strategie = container.get_service("strategie")
robot = container.get_service("robot")
robot.recaler()

# si le jumper est simulé
if "capteurs_actionneurs" in config["cartes_simulation"]:
    timer = container.get_service("threads.timer")
    input("Jumper simulé")
    timer.date_debut = time()
    timer.match_demarre = True

strategie.boucle_strategie()
