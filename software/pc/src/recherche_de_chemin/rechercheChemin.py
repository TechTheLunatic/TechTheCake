import os,sys

#retrouve le chemin de la racine "software/pc"
directory = os.path.dirname(os.path.abspath(__file__))
racine = "software/pc"
chemin = directory[:directory.index(racine)]+racine
#répertoires d'importation
sys.path.insert(0, os.path.join(chemin, "src/"))

try:
    import recherche_de_chemin.visilibity as vis
except:
    input("\n\nProblème avec la bibliothèque compilée _visilibity.so !\nConsultez le README dans src/recherche_de_chemin/visilibity/\n")
import math
import recherche_de_chemin.collisions as collisions

class Cercle:
    def __init__(self,centre,rayon):
        self.centre = centre
        self.rayon = rayon
        
    def copy(self):
        return Cercle(vis.Point(self.centre.x, self.centre.y), self.rayon)
        
class Environnement:
    
    def __init__(self):
        self.cercles = []
        self.polygones = []
        
        # côté des polygones qui représentent des cercles, en mm (petit : précision, grand : complexité moindre)
        self.cote_polygone = 100
        
    def copy(self):
        new = Environnement()
        new.cercles = list(map(lambda c: c.copy(), self.cercles))
        for poly in self.polygones:
            newPoly = []
            for k in range(poly.n()):
                newPoly.append(vis.Point(poly[k].x, poly[k].y))
            new.polygones.append(vis.Polygon(newPoly))
        #new.polygones = list(map(lambda poly: list(map(lambda point: vis.Point(point.x, point.y), poly)), self.polygones))
        return new
    
    def _polygone_du_cercle(self,cercle):
        """
        méthode de conversion cercle -> polygone
        """
        nbSegments = math.ceil(2*math.pi*cercle.rayon/self.cote_polygone)
        listePointsVi = []
        for i in range(nbSegments):
            theta = -2*math.pi*i/nbSegments
            x = cercle.centre.x + cercle.rayon*math.cos(theta)
            y = cercle.centre.y + cercle.rayon*math.sin(theta)
            listePointsVi.append(vis.Point(x,y))
        return vis.Polygon(listePointsVi)
        
    def _cercle_circonscrit_du_rectangle(self,rectangle):
        """
        méthode de conversion rectangle -> cercle circonscrit
        """
        centre = vis.Point((rectangle[0].x + rectangle[2].x)/2,(rectangle[0].y + rectangle[2].y)/2)
        rayon = math.sqrt((rectangle[0].x - rectangle[2].x)**2 + (rectangle[0].y - rectangle[2].y)**2)/2.
        return Cercle(centre,rayon)
        
    def _cercle_circonscrit_du_polygone(self,polygone):
        """
        méthode de conversion polygone -> cercle circonscrit
        """
        parcourt = {"lgr":0}
        for i in range(polygone.n()):
            for j in range(i,polygone.n()):
                lgr = math.sqrt((polygone[i].x - polygone[j].x)**2 + (polygone[i].y - polygone[j].y)**2)
                if lgr > parcourt["lgr"]:
                    parcourt["lgr"] = lgr
                    parcourt["point1"] = polygone[i]
                    parcourt["point2"] = polygone[j]
            
        centre = vis.Point((parcourt["point1"].x + parcourt["point2"].x)/2,(parcourt["point1"].y + parcourt["point2"].y)/2)
        rayon = parcourt["lgr"]/2.
        return Cercle(centre,rayon)
        
    def ajoute_cercle(self, cercle):
        self.cercles.append(cercle)
        self.polygones.append(self._polygone_du_cercle(cercle))
    
    def ajoute_rectangle(self, rectangle):
        self.polygones.append(rectangle)
        self.cercles.append(self._cercle_circonscrit_du_rectangle(rectangle))
        
    def ajoute_polygone(self, listePoints):
        polygone = vis.Polygon(list(map(lambda p: vis.Point(p.x,p.y), listePoints)))
        self.polygones.append(polygone)
        self.cercles.append(self._cercle_circonscrit_du_polygone(polygone))
        
    
class RechercheChemin:
    
    def __init__(self,table,config,log):
        
        #services nécessaires
        self.table = table
        self.config = config
        self.log = log
        
        # tolerance de précision (différent de 0.0)
        self.tolerance = 0.001
        
        # bords de la carte
        self.bords = vis.Polygon([vis.Point(-1500,0), vis.Point(1500,0), vis.Point(1500,2000), vis.Point(-1500,2000)])
        
        # environnement initial : obstacles fixes sur la carte
        self.environnement_initial = Environnement()
        # Définition des polygones des obstacles fixes. Ils doivent être non croisés et définis dans le sens des aiguilles d'une montre.
        self.environnement_initial.ajoute_rectangle(vis.Polygon([vis.Point(100, 300),vis.Point(100, 500),vis.Point(150, 500),vis.Point(150, 300)]))
        self.environnement_initial.ajoute_rectangle(vis.Polygon([vis.Point(0, 875),vis.Point(0, 1125),vis.Point(775, 1125),vis.Point(775, 875)]))
        self.environnement_initial.ajoute_rectangle(vis.Polygon([vis.Point(-775, 875),vis.Point(-775, 1125),vis.Point(-525, 1125),vis.Point(-525, 875)]))
        
        # environnement dynamique : liste des obstacles mobiles qui sont mis à jour régulièrement
        self.environnement_complet = self.environnement_initial.copy()
        
        
    ### Pour l'environnement dynamique #########
    def ajoute_obstacle_cercle(self, centre, rayon):
        cercle = Cercle(centre,rayon)
        self.environnement_complet.ajoute_cercle(cercle)
        self._fusionner_avec_obstacles_en_contact()
            
    def retirer_obstacles_dynamiques(self):
        #on retourne à l'environnement initial, en évitant de le modifier
        self.environnement_complet = self.environnement_initial.copy()
    ############################################
    
    def _fusionner_avec_obstacles_en_contact(self):
        #TODO SUPPRIMER :
        #WATCHDOG
        #
        
        #teste tous les polygones avec le dernier ajouté
        for i in range(len(self.environnement_complet.polygones)-1):
            #alias pour la clarté. Les polygones NE SONT PAS dupliqués (pointeurs)
            cercle1 = self.environnement_complet.cercles[i]
            cercle2 = self.environnement_complet.cercles[-1]
            #test rapide de collision entre les cercles circonscrits aux 2 polygones
            if not collisions.collision_2_cercles(cercle1,cercle2):
                self.log.warning("pas de collision cercle")
                continue
            
            polygone1 = self.environnement_complet.polygones[i]
            polygone2 = self.environnement_complet.polygones[-1]
            #identifiants des points de parcourt
            a1 = None
            #élection d'un point de polygone1 qui n'est pas dans polygone2
            for k in range(polygone1.n()):
                if not collisions.collisionPolygonePoint(polygone2,polygone1[k]):
                    a1 = k
                    break
            if type(a1) == int:
                #on note poly1 le polygone où commence le parcourt, en partant de a1
                poly1 = polygone1
                poly2 = polygone2
            else:
                #élection d'un point de polygone2 qui n'est pas dans polygone1
                for k in range(polygone2.n()):
                    if not collisions.collisionPolygonePoint(polygone1,polygone2[k]):
                        a1 = k
                        break
                if type(a1) == int:
                    #on note poly1 le polygone où commence le parcourt, en partant de a1
                    poly1 = polygone2
                    poly2 = polygone1
                else:
                    #les deux polygones sont strictement inclus l'un dans l'autre
                    self.log.critical("WTF IS GOING ON ???")
                    raise Exception
            
            def avancerSurPolygone(poly,position):
                if position < poly.n()-1: return position + 1
                else: return 0
                    
            #création de l'obstacle de merge
            mergeObstacle = []
            #on va considérer le segment allant jusqu'au point voisin de a1
            b1 = avancerSurPolygone(poly1,a1)
            WATCHDOG = 0
            auMoinsUneCollision = False
            condition = True
            while condition :
                WATCHDOG += 1
                #tests de collision du segment [a1,b1] de poly1 avec les segments de poly2
                collision = False
                pointCollision = None
                for a2 in range(poly2.n()):
                    b2 = avancerSurPolygone(poly2,a2)
                    pCollision = collisions.collisionSegmentSegment(poly1[a1],poly1[b1],poly2[a2],poly2[b2])
                    if pCollision:
                        pointCollision = pCollision[1]
                        collision = True
                        auMoinsUneCollision = True
                        break
                if collision:
                    mergeObstacle.append(pointCollision)
                    #on parcourt l'autre polygone, en inversant les pointeurs sur poly1 et poly2
                    sopalin = poly1
                    poly1 = poly2
                    poly2 = sopalin
                    #toujours dans le sens horaire : vers les indices croissants
                    if 0 in [a2,b2] and poly1.n()-1 in [a2,b2]: a1 = 0
                    else: a1 = max(a2,b2)
                    #TODO : autres collisions sur le segment [pointCollision,a1]
                    #parcourt du segment suivant sur l'ex poly2
                    mergeObstacle.append(poly1[a1])
                    b1 = avancerSurPolygone(poly1,a1)
                else :
                    #parcourt du segment suivant
                    a1 = b1
                    b1 = avancerSurPolygone(poly1,a1)
                    mergeObstacle.append(poly1[a1])
                condition = (poly1[b1] != mergeObstacle[0] and WATCHDOG<100)
            if WATCHDOG == 100:
                self.log.critical("récursion non terminale pour le polygone de fusion !")
                raise Exception
                
            if auMoinsUneCollision:
                self.log.warning("cet obstacle rentre en collision avec un autre obstacle. Ils ont été fusionnés.")
                #remplacement du premier obstacle par l'obstacle de fusion 
                mergePolygon = vis.Polygon(mergeObstacle)
                self.environnement_complet.polygones[i] = mergePolygon
                self.environnement_complet.cercles[i] = self.environnement_complet._cercle_circonscrit_du_polygone(mergePolygon)
                #suppression du deuxième obstacle
                del self.environnement_complet.polygones[-1]
                del self.environnement_complet.cercles[-1]
            else:
                self.log.warning("cet obstacle ne rentre pas en collision avec un autre obstacle.")
                    
        
    def get_obstacles(self):
        return (self.environnement_complet.polygones)
        
    def get_cercles_obstacles(self):
        return list(map(lambda cercle: self.environnement_complet._polygone_du_cercle(cercle), self.environnement_complet.cercles))
        
    def get_chemin(self,depart,arrivee):
        
        #test d'accessibilité du point d'arrivée
        if arrivee.x < -self.config["table_x"]/2 or arrivee.y < 0 or arrivee.x > self.config["table_x"]/2 or arrivee.y > self.config["table_y"]:
            self.log.critical("Le point d'arrivée n'est pas dans la table !")
            raise Exception
        for obstacle in self.environnement_complet.polygones:
            if collisions.collisionPointPoly(arrivee,obstacle):
                self.log.critical("Le point d'arrivée n'est pas accessible !")
                raise Exception
            
        #conversion en type vis.PointVisibility
        departVis = vis.Point(depart.x,depart.y)
        arriveeVis = vis.Point(arrivee.x, arrivee.y)
        
        # Création de l'environnement, le polygone des bords en premier, ceux des obstacles après (fixes et mobiles)
        env = vis.Environment([self.bords]+self.environnement_complet.polygones)
        
        # Vérification de la validité de l'environnement : polygones non croisés et définis dans le sens des aiguilles d'une montre.
        if not env.is_valid(self.tolerance):
            raise Exception
            
        #recherche de chemin
        cheminVis = env.shortest_path(departVis, arriveeVis, self.tolerance)
        
        #conversion en type vis.Point
        chemin = []
        for i in range(cheminVis.size()):
            chemin.append(vis.Point(cheminVis[i].x,cheminVis[i].y))
        return chemin