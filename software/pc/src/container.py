import os,sys

#retrouve le chemin de la racine "software/pc"
directory = os.path.dirname(os.path.abspath(__file__))
racine = "software/pc"
chemin = directory[:directory.index(racine)]+racine

#répertoires d'importation
sys.path.insert(0, os.path.join(chemin, "src/"))

#module d'injection de dépendances
from assemblage import assembler
from mutex import Mutex

#module pour les threads
from threading import Thread
#fonction lancée dans le thread de MAJ
from thread_MAJ import fonction_MAJ

#modules -> services
from read_ini import Config
from robot import *
from robotChrono import RobotChrono
from deplacements import DeplacementsSimulateur, DeplacementsSerie
from capteurs import CapteursSerie, CapteursSimulateur
from actionneurs import ActionneursSerie, ActionneursSimulateur
from serie import Serie
from table import Table
from suds.client import Client
from recherche_de_chemin.rechercheChemin import RechercheChemin
from strategie import Strategie
from log import Log

class Container:
    def __init__(self):
        self.assembler = assembler()
        self.mutex = Mutex()
        
        #enregistrement du service de configuration
        def make_conf():
            conf = Config()
            conf.set_chemin(chemin+"/config")
            return conf
        self.assembler.register("config",Config,factory=make_conf)
        
        #utilisation du service de configuration pour la suite
        self.config = self.get_service("config")
        
        #enregistrement du service des logs
        def make_log(config):
            log = Log(self.config)
            log.set_chemin(chemin)
            return log
        self.assembler.register("log", Log, requires = ["config"], factory=make_log)
        
        #services différents en fonction du mode simulateur on/off :
        if (self.config["mode_simulateur"]):
            #enregistrement du service Simulateur
            def make_simu():
                #client SOAP pour le simulateur
                client=Client("http://localhost:8090/INTechSimulator?wsdl")
                #initialisation de la table
                client.service.reset()
                client.service.setTableDimension(self.config["table_x"],self.config["table_y"])
                client.service.defineCoordinateSystem(1,0,0,-1,self.config["table_x"]/2,self.config["table_y"])
                #déclaration du robot
                client.service.defineRobot({"list":[{"float":[-200.,-200.]},{"float":[-200.,200.]},{"float":[200.,200.]},{"float":[200.,-200.]}]})
                #déclaration d'un robot adverse
                client.service.addEnemy(30,"black")
                return client.service
                
            self.assembler.register("simulateur",  None, factory=make_simu)
            #enregistrement du service des capteurs pour le simulateur
            self.assembler.register("capteurs",CapteursSimulateur, requires=["simulateur","config","log"])
            #enregistrement du servide des actionneurs pour le simulateur
            self.assembler.register("actionneurs",ActionneursSimulateur, requires=["simulateur","config","log"])
            #enregistrement du service des déplacements pour le simulateur
            self.assembler.register("deplacements",DeplacementsSimulateur, requires=["simulateur","config","log"])
            
        else:
            #enregistrement du service Serie
            self.assembler.register("serie", Serie, requires = ["log"])
            #enregistrement du service des capteurs pour la série
            self.assembler.register("capteurs",CapteursSerie, requires=["serie","config","log"])
            #enregistrement du service des actionneurs pour la série
            self.assembler.register("actionneurs",ActionneursSerie, requires=["serie","config","log"])
            #enregistrement du service des déplacements pour la série
            self.assembler.register("deplacements",DeplacementsSerie, requires=["serie","config","log"])
        
        #enregistrement du service robot
        self.assembler.register("robot", Robot, requires=["capteurs","actionneurs","deplacements","config","log"])
        
        #enregistrement du service robotChrono
        self.assembler.register("robotChrono", RobotChrono, requires=["log"])
        
        #enregistrement du service donnant des infos sur la table
        self.assembler.register("table", Table, requires=["config","log"])
        
        #enregistrement du service de recherche de chemin
        self.assembler.register("rechercheChemin", RechercheChemin, requires=["table","config","log"])
        
        #enregistrement du service de stratégie
        self.assembler.register("strategie", Strategie, requires=["robot", "robotChrono","rechercheChemin", "config", "log"])
        
        #lancement des threads
        self.start_threads()
        
        
    def start_threads(self):
        
        #fonction qui lance les threads
        def lancement_des_threads():
            #lancement du thread de mise à jour des coordonnées
            thread_MAJ = Thread(None, fonction_MAJ, None, (), {"container":self})
            thread_MAJ.start()
            #attente d'une première mise à jour pour la suite
            robot = self.get_service("robot")
            while not robot.pret:
                sleep(0.1)
        
        #conditions sur le lancement des threads
        if self.config["mode_simulateur"]:
            #si on est en mode simulateur...
            lancement_des_threads()
        else:
            #...ou si l'asservissement en série est présent
            serie = self.get_service("serie")
            if hasattr(serie.peripheriques["asservissement"],'serie'):
                lancement_des_threads()
                
                
    def get_service(self,id):
        #mutex pour éviter la duplication d'un service à cause d'un thread (danger !)
        with self.mutex:
            return self.assembler.provide(id)
        
