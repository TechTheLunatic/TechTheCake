import abc # classe abstraite


class Actionneurs(metaclass=abc.ABCMeta):

    @abc.abstractmethod # abstraite : rien dedans mais plante si rien après (def de la méthode abstraite)
    def ouvrir_cadeau(self):
        pass
        
    @abc.abstractmethod
    def fermer_cadeau(self):
        pass

    @abc.abstractmethod
    def gonfler_ballon(self) :
        pass
        
    @abc.abstractmethod
    def initialiser_bras_bougie(self,enHaut) : 
        pass
        
    @abc.abstractmethod
    def enfoncer_bougie(self,enHaut) :
        pass
        
    @abc.abstractmethod
    def rentrer_bras_bougie(self) : 
        pass
        
    @abc.abstractmethod
    def ascenseur_aller_en_haut(self):
        pass
        
    @abc.abstractmethod
    def ascenseur_aller_en_bas(self):
        pass
        
    @abc.abstractmethod
    def ascenseur_ranger(self):
        pass
        
    @abc.abstractmethod
    def ascenseur_serrer(self):
        pass
        
    @abc.abstractmethod
    def ascenseur_deserrer(self):
        pass
        
    @abc.abstractmethod
    def ascenseur_modifier_constantes(self, valeur):
        pass

class ActionneursSerie(Actionneurs) : #héritage

    def __init__(self,serie,config,log):
        #services utilisés
        self.serie = serie
        self.config = config
        self.log = log

    def ouvrir_cadeau(self) :
        self.serie.communiquer("cadeaux",["g",240],0)
    
    def fermer_cadeau(self) :
        self.serie.communiquer("cadeaux",["g",150],0)

    def gonfler_ballon(self) :
        self.log.debug("Gonflage du ballon")
        
    def initialiser_bras_bougie(self,enHaut) : 
        if enHaut:
            self.log.debug("Relève l'actionneur bougie du haut")
            self.serie.communiquer("actionneur_bougies",["haut",67],0)
        else:
            self.log.debug("Relève l'actionneur bougie du bas")
            self.serie.communiquer("actionneur_bougies",["bas",80],0)

    def enfoncer_bougie(self,enHaut) :
        if enHaut:
            self.log.debug("Enfonce une bougie avec l'actionneur du haut")
            self.serie.communiquer("actionneur_bougies",["haut",85],0)
        else:
            self.log.debug("Enfonce une bougie avec l'actionneur du bas")
            self.serie.communiquer("actionneur_bougies",["bas",160],0)

    def rentrer_bras_bougie(self) : 
        self.log.debug("Rentre les 2 actionneurs pour bougies")
        self.serie.communiquer("actionneur_bougies",["haut",170],0)
        self.serie.communiquer("actionneur_bougies",["bas",240],0)

    def ascenseur_aller_en_haut(self):
        self.serie.communiquer("ascenseur", "haut", 0)

    def ascenseur_aller_en_bas(self):
        self.serie.communiquer("ascenseur", "bas", 0)

    def ascenseur_ranger(self):
        self.serie.communiquer("pince_verre", ["g",0,180] , 0)

    def ascenseur_serrer(self):
        self.serie.communiquer("pince_verre", ["g",0,160] , 0)

    def ascenseur_deserrer(self):
        self.serie.communiquer("pince_verre", ["g",0,100] , 0)

    def ascenseur_modifier_constantes(self, valeur):
        """
        Donner le nombre de verres dans l'ascenseur
        0, 1, 2, 3 ou 4
        """

        kp = [0.1 ,0 ,0 ,0.01 ,0.01 ]
        kd = [0.001 ,0 ,0 ,0.001 ,0.0001 ]
        ki = [0 ,0 ,0 ,0.0001 ,0 ]
        pwm = [150 ,0 ,0 ,200 ,255 ]

        envoi = ["changerConstantes"]
        envoi.append(int(pwm[valeur]))
        envoi.append(float(kp[valeur]))
        envoi.append(float(kd[valeur]))
        envoi.append(float(ki[valeur]))
        self.serie.communiquer("ascenseur", envoi, 0)

class ActionneursSimulateur(Actionneurs) :
     
    def __init__(self,simulateur,config,log):
        #services utilisés
        self.simulateur = simulateur
        self.config = config
        self.log = log    
     
    def ouvrir_cadeau(self) :
        self.log.debug("Ouverture actionneur cadeau")
    
    def fermer_cadeau(self) :
        self.log.debug("Fermeture actionneur cadeau")

    def gonfler_ballon(self) :
        self.log.debug("Gonflage du ballon")

    def initialiser_bras_bougie(self,enHaut) : 
        if enHaut:
            self.log.debug("Relève l'actionneur bougie du haut")
        else:
            self.log.debug("Relève l'actionneur bougie du bas")

    def enfoncer_bougie(self,enHaut) :
        if enHaut:
            self.log.debug("Enfonce la bougie avec l'actionneur du haut")
        else:
            self.log.debug("Enfonce la bougie avec l'actionneur du bas")

    def rentrer_bras_bougie(self) : 
        self.log.debug("Rentre les 2 actionneurs pour bougies")

    def ascenseur_aller_en_haut(self):
        self.log.debug("Ascenseur va en bas")

    def ascenseur_aller_en_bas(self):
        self.log.debug("L'ascenseur va en haut")

    def ascenseur_ranger(self):
        self.log.debug("Range pince ascenseur")

    def ascenseur_serrer(self):
        self.log.debug("Serre ascenseur")

    def ascenseur_deserrer(self):
        self.log.debug("Déserre ascenseur")

    def ascenseur_modifier_constantes(self, valeur):
        self.log.debug("Modifier constantes ascenseur pour " + str(valeur) + "verres")
