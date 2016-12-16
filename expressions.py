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

        self.id = eventConf.get("eventId", 0)
        self.eventPhase = eventConf.get("eventPhase", 0)
        self.eventChance = eventConf.get("eventChance",100)
        self.eventLink = eventConf.get("eventLink",0)
        self.param1 = eventConf.get("param1", 0)
        self.param2 = eventConf.get("param2", 0)
        self.param3 = eventConf.get("param3", 0)
        self.param4 = eventConf.get("param4", 0)  

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

class Target(Expression):
    def __init__(self, targetType, targetConf):
        self.targetType = targetType
        self.targetConf = targetConf
        if targetConf is None:
            return
        self.param1 = targetConf.get("param1", 0)
        self.param2 = targetConf.get("param2", 0)
        self.param3 = targetConf.get("param3", 0)
        self.paramX = targetConf.get("paramX", 0)
        self.paramY = targetConf.get("paramY", 0)  
        self.paramZ = targetConf.get("paramZ", 0)  
        self.paramO = targetConf.get("paramO", 0)