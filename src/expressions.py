# Clase abstracta
class Expression(object):
    def evaluate(self):
        # Aca se implementa cada tipo de expresion.
        raise NotImplementedError
    def __repr__(self):
        return self.__str__()

class Script(Expression):
    def __init__(self, event, action, target, entry):
        self.entry = entry
        self.event = event
        self.action = action
        self.target = target

    def __str__(self):
        cadena = "Script:"
        cadena += "\n Creature Entry: " + str(self.entry)
        cadena += "\n " + str(self.event)
        cadena += "\n " + str(self.action)
        cadena += "\n " + str(self.target)
        return cadena 

class Event(Expression):
    def __init__(self, eventType, eventConf):
        self.eventType = eventType
        self.eventconf = eventConf

        self.id = eventConf.get("eventId", 0)
        self.eventPhase = eventConf.get("eventPhase", 0)
        self.eventChance = eventConf.get("eventChance",100)
        self.eventLink = eventConf.get("eventLink",0)
        self.param1 = eventConf.get("param1", 0)
        self.param2 = eventConf.get("param2", 0)
        self.param3 = eventConf.get("param3", 0)
        self.param4 = eventConf.get("param4", 0)  

    def __str__(self):
        cadena = "Event:"
        cadena += "\n  eventId: " + str(self.id)
        cadena += "\n  eventType: " + str(self.eventType)
        cadena += "\n  eventPhase: " + str(self.eventPhase)
        cadena += "\n  eventChance: " + str(self.eventChance)
        cadena += "\n  eventLink: " + str(self.eventLink)
        cadena += "\n  param1: " + str(self.param1)
        cadena += "\n  param2: " + str(self.param2)
        cadena += "\n  param3: " + str(self.param3)
        cadena += "\n  param4: " + str(self.param4)
        return cadena 

class Action(Expression):
    def __init__(self, actionType, actionConf):
        self.actionType = actionType
        self.actionConf = actionConf

        self.param1 = actionConf.get("param1", 0)
        self.param2 = actionConf.get("param2", 0)
        self.param3 = actionConf.get("param3", 0)
        self.param4 = actionConf.get("param4", 0)
        self.param5 = actionConf.get("param5", 0)  
        self.param6 = actionConf.get("param6", 0)  

    def __str__(self):
        cadena = "Action:"
        cadena += "\n  actionType: " + str(self.actionType)
        cadena += "\n  param1: " + str(self.param1)
        cadena += "\n  param2: " + str(self.param2)
        cadena += "\n  param3: " + str(self.param3)
        cadena += "\n  param4: " + str(self.param4)
        cadena += "\n  param5: " + str(self.param5)
        cadena += "\n  param6: " + str(self.param6)
        return cadena 

class Target(Expression):
    def __init__(self, targetType, targetConf):
        self.targetType = targetType
        self.targetConf = targetConf

        if targetConf is None:
            targetConf = {}

        self.param1 = targetConf.get("param1", 0)
        self.param2 = targetConf.get("param2", 0)
        self.param3 = targetConf.get("param3", 0)
        self.paramX = targetConf.get("paramX", 0)
        self.paramY = targetConf.get("paramY", 0)  
        self.paramZ = targetConf.get("paramZ", 0)  
        self.paramO = targetConf.get("paramO", 0)

    def __str__(self):
        cadena = "Target:"
        cadena += "\n  targetType: " + str(self.targetType)      
        cadena += "\n  param1: " + str(self.param1)
        cadena += "\n  param2: " + str(self.param2)
        cadena += "\n  param3: " + str(self.param3)
        cadena += "\n  paramX: " + str(self.paramX)
        cadena += "\n  paramY: " + str(self.paramY)
        cadena += "\n  paramZ: " + str(self.paramZ)
        cadena += "\n  paramO: " + str(self.paramO)
        return cadena 