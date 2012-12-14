from math import pi
from time import time

_tolerance_distance_mm   = 20
_tolerance_angle_radians = 0.2

class Hook:
    def __init__(self,callback,args):
        #méthode à appeler
        self.callback = callback
        #arguments facultatifs pour le callback
        self.args = args
    
class HookPosition(Hook):
    def __init__(self, position, callback,*args):
        Hook.__init__(self,callback,args)
        #point déclencheur
        self.position_hook = position
    def evaluate(self,robotX,robotY,**useless):
        if ((robotX - self.position_hook.x)**2 + (robotY - self.position_hook.y)**2 <= _tolerance_distance_mm**2):
            self.callback(*self.args)
        
class HookOrientation(Hook):
    def __init__(self, orientation, callback,*args):
        Hook.__init__(self,callback,args)
        #angle déclencheur
        self.orientation_hook = orientation
    def evaluate(self,robotOrientation,**useless):
        delta_angle = abs(robotOrientation - self.orientation_hook)%(2*pi)
        if (delta_angle > pi): delta_angle = (2*pi)-delta_angle
        if (delta_angle <= _tolerance_angle_radians):
            self.callback(*self.args)
            
class HookGenerator():
    def __init__(self, config, log):
        self.config = config
        self.log = log
        self.types = {"position":HookPosition,"orientation":HookOrientation}
        
    def get_hook(self, type, condition, callback,*args):
        return self.types[type](condition, callback,*args)
        