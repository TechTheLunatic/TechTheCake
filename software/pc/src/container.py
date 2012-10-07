import os,sys

#retrouve le chemin de la racine "software/pc"
directory = os.path.dirname(os.path.abspath(__file__))
racine = "software/pc"
chemin = directory[:directory.index(racine)]+racine

#répertoires d'importation
sys.path.insert(0, os.path.join(chemin, "src/"))

#module d'injection de dépendances
from assemblage import assembler

#modules
from read_ini import Config
from robot import *
from deplacements import DeplacementsSimulateur, DeplacementsSerie
from serie import Serie
from scripts import Script, ScriptBougies
from log import Log

class Container:
    def __init__(self):
        self.assembler = assembler()
        
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
        
        #enregistrement du service Serie
        self.assembler.register("serie", Serie, requires = ["log"])
        
        #enregistrement du service des déplacements
        if (self.config["mode_simulateur"]):
            self.assembler.register("deplacements",DeplacementsSimulateur, requires=["config","log"])
        else:
            self.assembler.register("deplacements",DeplacementsSerie, requires=["serie","config","log"])
        
        #enregistrement du service robot
        self.assembler.register("robot", Robot, requires=["deplacements","config","log"])
        
        """
        #enregistrement du service donnant des infos sur la table
        self.assembler.register("table", Table, requires=["config","log"])
        
        #enregistrement du service de recherche de chemin
        self.assembler.register("recherche_chemin", RechercheChemin, requires=["table","log"])
        
        #enregistrement du service de scripts
        self.assembler.register("script", Script, requires=["robot","config","log"])
        """
        
    def get_service(self,id):
        return self.assembler.provide(id)
        