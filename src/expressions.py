from collections import namedtuple

Number = namedtuple('Number', 'value type')
EventFlag = namedtuple('EventFlag', 'name id')
CastFlag = namedtuple('CastFlag', 'name id')

def error_noline(msg):
    raise Exception("Error: %s" % (msg))

def isNumber(v, p):
    if len(v) is 1 and type(v[0]) is Number:
        return
    error_noline("Parameter: " + p + " must be just one number.")

def isListOfClass(v, p, c):
    for e in v:
        if type(e) is not c:
            error_noline("Parameter: " + p + " must be an event flag or more separated by |.")

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
        (paramsDict, paramsList) = eventConf
        self.eventType = eventType
        self.eventconf = eventConf

        if paramsDict is None:
            paramsDict = {}

        self.eventId = paramsDict.get("eventId", [Number(0,'int')])
        self.eventPhase = paramsDict.get("eventPhase", [Number(0,'int')])
        self.eventChance = paramsDict.get("eventChance",[Number(100,'int')])
        self.eventFlags = paramsDict.get("eventFlags",[EventFlag('SMART_EVENT_FLAG_NONE', 0)])       
        self.eventLink = paramsDict.get("eventLink",[Number(0,'int')])

        isNumber(self.eventId, "eventId")
        isNumber(self.eventPhase, "eventPhase")
        isNumber(self.eventChance, "eventChance")
        isNumber(self.eventLink, "eventLink")
        #isListOfClass(self.eventFlags, "eventFlags", EventFlag)

        # initialize with default values
        self.params = [[Number(0,'int')], [Number(0,'int')], [Number(0,'int')], [Number(0,'int')]]

        # preconditions: custom parameter name cannot be mixed with param1, param2, param3, param4 names.
        customParameters = filter(lambda paramName: paramName[0] is '*', paramsList)
        customParameters = list(customParameters) # we later call len

        if len(customParameters) > 0:
            for (idx, param) in enumerate(customParameters):
                self.params[idx] = paramsDict[param]
        else:
            for i in range(0, 4):
                self.params[i] = paramsDict.get("param"+str(i+1), [Number(0,'int')])

    def __str__(self):
        cadena = "Event:"
        cadena += "\n  eventId: " + str(self.eventId)
        cadena += "\n  eventType: " + str(self.eventType)
        cadena += "\n  eventPhase: " + str(self.eventPhase)
        cadena += "\n  eventChance: " + str(self.eventChance)
        cadena += "\n  eventLink: " + str(self.eventLink)
        cadena += "\n  param1: " + str(self.params[0])
        cadena += "\n  param2: " + str(self.params[1])
        cadena += "\n  param3: " + str(self.params[2])
        cadena += "\n  param4: " + str(self.params[3])
        return cadena 

class Action(Expression):
    def __init__(self, actionType, actionConf):
        (paramsDict, paramsList) = actionConf
        self.actionType = actionType
        self.actionConf = actionConf

        if paramsDict is None:
            paramsDict = {}

        # initialize with default values
        self.params = [[Number(0,'int')], [Number(0,'int')], [Number(0,'int')], [Number(0,'int')], [Number(0,'int')], [Number(0,'int')]]

        # preconditions: custom parameter name cannot be mixed with param1, param2, param3, param4 names.
        customParameters = filter(lambda paramName: paramName[0] is '*', paramsList)
        customParameters = list(customParameters) # we later call len

        if len(customParameters) > 0:
            for (idx, param) in enumerate(customParameters):
                self.params[idx] = paramsDict[param]
        else:
            for i in range(0, 6):
                self.params[i] = paramsDict.get("param"+str(i+1), [Number(0,'int')])

    def __str__(self):
        cadena = "Action:"
        cadena += "\n  actionType: " + str(self.actionType)
        cadena += "\n  param1: " + str(self.params[0])
        cadena += "\n  param2: " + str(self.param[1])
        cadena += "\n  param3: " + str(self.param[2])
        cadena += "\n  param4: " + str(self.param[3])
        cadena += "\n  param5: " + str(self.param[4])
        cadena += "\n  param6: " + str(self.param[5])
        return cadena 

class Target(Expression):
    def __init__(self, targetType, targetConf):
        (paramsDict, paramsList) = targetConf
        self.targetType = targetType
        self.targetConf = targetConf

        if paramsDict is None:
            paramsDict = {}

        self.paramX = paramsDict.get("paramX", [Number(0,'int')])
        self.paramY = paramsDict.get("paramY", [Number(0,'int')])  
        self.paramZ = paramsDict.get("paramZ", [Number(0,'int')])  
        self.paramO = paramsDict.get("paramO", [Number(0,'int')])

        # initialize with default values
        self.params = [[Number(0,'int')], [Number(0,'int')], [Number(0,'int')]]

        # preconditions: custom parameter name cannot be mixed with param1, param2, param3, param4 names.
        customParameters = filter(lambda paramName: paramName[0] is '*', paramsList)
        customParameters = list(customParameters) # we later call len

        if len(customParameters) > 0:
            for (idx, param) in enumerate(customParameters):
                self.params[idx] = paramsDict[param]
        else:
            for i in range(0, 3):
                self.params[i] = paramsDict.get("param"+str(i+1), [Number(0,'int')])

    def __str__(self):
        cadena = "Target:"
        cadena += "\n  targetType: " + str(self.targetType)      
        cadena += "\n  param1: " + str(self.params[0])
        cadena += "\n  param2: " + str(self.params[1])
        cadena += "\n  param3: " + str(self.params[2])
        cadena += "\n  paramX: " + str(self.paramX)
        cadena += "\n  paramY: " + str(self.paramY)
        cadena += "\n  paramZ: " + str(self.paramZ)
        cadena += "\n  paramO: " + str(self.paramO)
        return cadena 