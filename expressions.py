# Clase abstracta
class Expression(object):
    def evaluate(self):
        # Aca se implementa cada tipo de expresion.
        raise NotImplementedError

class Script(Expression):
    def __init__(self, event, action, target, entry):
        self.entry = entry
        self.event = event
        self.action = action
        self.target = target

class Event(Expression):
    def __init__(self, eventType, eventConf):
        self.eventType = eventType
        self.eventconf = eventConf
        #self.id = id
        #self.eventPhase = eventPhase
        #self.eventChance = eventChance
        #self.eventLink = link      
        #self.param1 = param1
        #self.param2 = param2
        #self.param3 = param3
        #self.param4 = param4  

class Action(Expression):
    def __init__(self, actionType, actionConf):
        self.actionType = actionType
        self.actionConf = actionConf

class Target(Expression):
    def __init__(self, type, param1=None, param2=None, param3=None, paramX=None, paramY=None, paramZ=None, paramO=None):
        self.type = type
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.paramX = paramX
        self.paramY = paramY
        self.paramZ = paramZ
        self.paramO = paramO