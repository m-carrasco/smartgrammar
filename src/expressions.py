from collections import namedtuple
from .definitions import getSourceType

Number = namedtuple('Number', 'value type')
EventFlag = namedtuple('EventFlag', 'name id')
CastFlag = namedtuple('CastFlag', 'name id')

def error_noline(msg):
    raise Exception("Error: %s" % (msg))

def isNumber(v, p):
    if type(v) is Number:
        return
    error_noline("Parameter: " + p + " must be just one number.")

def isListOfClass(v, p, c):
    for e in v:
        if type(e) is not c:
            error_noline("Parameter: " + p + " must be an event flag or more separated by |.")

def orFlags(flags):
    res = 0
    for f in flags:
        if type(f) is Number:
            res = res | int(f.value)
        else:
            res = res | int(f.id)
    return res

# Clase abstracta
class Expression(object):
    def evaluate(self):
        # Aca se implementa cada tipo de expresion.
        raise NotImplementedError
    def __repr__(self):
        return self.__str__()

class Script(Expression):
    def __init__(self, sourceType, event, action, target, entry):
        self.entry = entry
        self.event = event
        self.action = action
        self.target = target
        self.sourceType = sourceType

    def __str__(self):
        cadena = "Script:"
        cadena += "\n Source: " + str(self.sourceType)
        cadena += "\n Entry: " + str(self.entry)
        cadena += "\n " + str(self.event)
        cadena += "\n " + str(self.action)
        cadena += "\n " + str(self.target)
        return cadena

    def toSQL(self):
        #                        1          2           3    4       5        6                   7              8               9            10              11          12               13          14              15            16               17               18          19      20                   21            22           23         24           25        26     27           28
        sql = """INSERT INTO smart_scripts (entryorguid, source_type, id, link, event_type, event_phase_mask, event_chance, event_flags, event_param1, event_param2, event_param3, event_param4, action_type, action_param1, action_param2, action_param3, action_param4, action_param5,  action_param6, target_type, target_param1, target_param2, target_param3, target_x, target_y, target_z, target_o, comment)
VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {},{},{}, {}, {}, {}, {}, {}, {}, {},{}, {}, {}, {}, {}, {}, {}, {}, {}, {});"""

        e = self.event
        a = self.action
        t = self.target

        #                     (entryorguid,               source_type,                         id,          link,                       event_type,          event_phase_mask,       event_chance,              event_flags,            event_param1,         event_param2,         event_param3,          event_param4,       action_type,           action_param1,         action_param2,        action_param3,           action_param4,  action_param5          action_param6,               target_type,         target_param1,       target_param2,         target_param3,         target_x,       target_y,        target_z,            target_0,    comment)
        sql = sql.format(self.entry.value,     getSourceType(self.sourceType),        e.eventId[0].value, e.eventLink[0].value, e.eventType['value'],  e.eventPhase[0].value,      e.eventChance[0].value,   orFlags(e.eventFlags), e.params[0][0].value, e.params[1][0].value, e.params[2][0].value, e.params[3][0].value,  a.actionType['value'], a.params[0][0].value, a.params[1][0].value, a.params[2][0].value, a.params[3][0].value, a.params[4][0].value, a.params[5][0].value, t.targetType['value'], t.params[0][0].value, t.params[1][0].value, t.params[2][0].value, t.paramX[0].value, t.paramY[0].value,t.paramZ[0].value,t.paramO[0].value, """''""")
        return sql

class Event(Expression):
    eventId = 0
    def __init__(self, eventType, eventConf):
        paramsDict= eventConf
        self.eventType = eventType
        self.eventconf = eventConf

        if paramsDict is None:
            paramsDict = {}

        self.eventId = Number(paramsDict.get("eventId", Number(0,'int')), 'int')
        #Event.eventId += 1
        self.eventPhase = paramsDict.get("PHASE", Number(0,'int'))
        self.eventChance = paramsDict.get("CHANCES",Number(100,'int'))
        self.eventFlags = paramsDict.get("FLAGS",Number(0,'int'))
        self.eventLink = paramsDict.get("LINK",Number(0,'int'))

        isNumber(self.eventId, "eventId")
        isNumber(self.eventPhase, "eventPhase")
        isNumber(self.eventChance, "eventChance")
        isNumber(self.eventLink, "eventLink")

        # initialize with default values
        self.params = [Number(0,'int'), Number(0,'int'), Number(0,'int'), Number(0,'int')]
        for i in range(0, 4):
            self.params[i] = paramsDict.get("param"+str(i+1), Number(0,'int'))

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
        paramsDict = actionConf
        self.actionType = actionType
        self.actionConf = actionConf

        if paramsDict is None:
            paramsDict = {}

        # initialize with default values
        self.params = [Number(0,'int'), Number(0,'int'), Number(0,'int'), Number(0,'int'), Number(0,'int'), Number(0,'int')]

        for i in range(0, 6):
            self.params[i] = paramsDict.get("param"+str(i+1), [Number(0,'int')])


    def __str__(self):
        cadena = "Action:"
        cadena += "\n  actionType: " + str(self.actionType)
        cadena += "\n  param1: " + str(self.params[0])
        cadena += "\n  param2: " + str(self.params[1])
        cadena += "\n  param3: " + str(self.params[2])
        cadena += "\n  param4: " + str(self.params[3])
        cadena += "\n  param5: " + str(self.params[4])
        cadena += "\n  param6: " + str(self.params[5])
        return cadena

class Target(Expression):
    def __init__(self, targetType, targetConf):
        paramsDict = targetConf
        self.targetType = targetType
        self.targetConf = targetConf

        if paramsDict is None:
            paramsDict = {}

        self.paramX = paramsDict.get("param4", Number(0,'int'))
        self.paramY = paramsDict.get("param5", Number(0,'int'))
        self.paramZ = paramsDict.get("param6", Number(0,'int'))
        self.paramO = paramsDict.get("param7", Number(0,'int'))

        # initialize with default values
        self.params = [Number(0,'int'), Number(0,'int'), Number(0,'int')]

        self.params[0] = paramsDict.get("param1", Number(0,'int'))
        self.params[1] = paramsDict.get("param2", Number(0,'int'))
        self.params[2] = paramsDict.get("param3", Number(0,'int'))

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
