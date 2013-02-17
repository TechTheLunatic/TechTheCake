import math

class Laser:
    
    def __init__(self, robot, serie, config, log):
        self.robot = robot
        self.serie = serie
        self.config = config
        self.log = log
    
    def allumer(self):
        self.serie.communiquer("laser", ["motor_on"], 0)
        self.serie.communiquer("laser", ["laser_on"], 0)
        
    def eteindre(self):
        self.serie.communiquer("laser", ["laser_off"], 0)
        self.serie.communiquer("laser", ["motor_off"], 0)
        
    def ping_balise(self):
        pass
        
    def frequence_moteur(self):
        reponse = self.serie.communiquer("laser", ["freq"], 1)
        return reponse[0]
        
    def position_balise(self, id_balise):
        # Récupération de la position de la balise dans le repère du robot
        reponse = self.serie.communiquer("laser", ["valeur", id_balise], 1)
        rayon = reponse[0]
        angle = reponse[1]
        
        # Changement dans le repère de la table
        x = float(self.robot.x) + rayon * math.cos(angle + self.robot.orientation)
        y = float(self.robot.y) + rayon * math.sin(angle + self.robot.orientation)
        
        return [x, y]

