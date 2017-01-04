import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from .lexer import tokens
from .expressions import Script, Event, Action, Target, Number

# resume of productions
# remember that newlines, tab and spaces are ignored

# initial : source SCRIPT COLON entryorguid EQUAL NUMBER script

# script : AT SMART_EVENT_TYPE params DO SMART_ACTION_TYPE params ON SMART_TARGET_TYPE params script | lambda

# theses productions generate a dictionary that is indexed by the string name of a parameter
# params : PARAM_NAME EQUAL value params | lambda

# value generates a list.
# value : val PIPE value | val
# val : NUMBER | SMART_EVENT_FLAG | SMARTCAST_FLAG

# handling custom errors

# --------------------------------------------------- NEW ---------------------------

# initial -> TYPE SOURCE ENTRYORGUID NUMBER c e a t

# c -> PARAM_NAME L_PAREN NUMBER R_PAREN c | lambda
# e -> SMART_EVENT_TYPE L_PAREN l R_PAREN
# a -> SMART_ACTION_TYPE L_PAREN l R_PAREN
# t -> SMART_TARGET_TYPE L_PAREN l R_PAREN

# l -> NUMBER l_prime | PARAM_NAME EQUAL NUMBER l_prime | lambda
# l_prime -> COMMA NUMBER l_prime | COMMA PARAM_NAME EQUAL NUMBER l_prime | lambda

def error(line,msg):
    raise Exception("Line:%d Error: %s" % (line,msg))

def p_initial(p):
    'initial : TYPE SOURCE ENTRYORGUID NUMBER s'

    if p[3] == "GUID":
        p[4] = Number(p[4].value*(-1), p[4].type)

    p[0] = [Script(sourceType = p[2], entry=p[4], event=ev, action=ac, target=ta) for (ev, ac, ta) in p[5]]

    # find better way
    for (idx,sc) in list(enumerate(p[0])):
        sc.event.eventId = Number(idx, 'int')

def p_s_1(p):
    's : c e a t s'
    # c is a dictionary
    # e a t is a tuple of (id, dictionary)
    # s is a list of already processed scripts

    eConfig = p[1]
    (eType, eDict) = p[2]
    (aType, aDict) = p[3]
    (tType, tDict) = p[4]
    scriptList = p[5]

    eDict.update(eConfig)

    t = (Event(eventType=eType, eventConf=eDict), Action(actionType=aType, actionConf= aDict), Target(targetType=tType, targetConf=tDict))
    scriptList.insert(0,t)

    p[0] = scriptList

def p_s_2(p):
    's : '
    p[0] = []

def p_e(p):
    'e : SMART_EVENT_TYPE L_PAREN l R_PAREN'
    r = { ('param'+ str(i+1)) : e for (i, e) in list(enumerate(p[3]))}

    p[0] = (p[1], r)

def p_a(p):
    'a : SMART_ACTION_TYPE L_PAREN l R_PAREN'
    r = { ('param'+ str(i+1)) : e for (i, e) in list(enumerate(p[3]))}
    p[0] = (p[1], r)

def p_t(p):
    't : SMART_TARGET_TYPE L_PAREN l R_PAREN'
    r = { ('param'+ str(i+1)) : e for (i, e) in list(enumerate(p[3]))}
    p[0] = (p[1], r)

def p_c_1(p):
    'c : PARAM_NAME L_PAREN NUMBER R_PAREN c'
    # TODO: check that key does not exist already
    paramName = p[1]
    paramValue = p[3]
    params = p[5]
    params[paramName] = paramValue
    p[0] = params

def p_c_2(p):
    'c : '
    p[0] = {}

def p_l_1(p):
    'l : NUMBER l_prime'

    prevParams = p[2] 
    prevParams.insert(0, p[1])
    p[0] = prevParams

def p_l_2(p):
    #0     1           2     3      4
    'l : PARAM_NAME EQUAL NUMBER l_prime'

    # TODO: CHECK that PARAM_NAME begins with *

    prevParams = p[4]
    prevParams.insert(0, p[3])
    p[0] = prevParams

def p_l_3(p):
    'l : '
    p[0] = []  

def p_l_prime_1(p):
    'l_prime : COMMA NUMBER l_prime'

    prevParams = p[3] 
    prevParams.insert(0, p[2])
    p[0] = prevParams

def p_l_prime_2(p):
    'l_prime : COMMA PARAM_NAME EQUAL NUMBER l_prime'
    # TODO: CHECK that PARAM_NAME begins with *
    prevParams = p[5]
    prevParams.insert(0, p[4])
    p[0] = prevParams

def p_l_prime_3(p):
    'l_prime : '
    p[0] = []  


# ------------------------------------------------- OLD -------------------------------------------
# def p_initial(p):
#   # 0          1        2      3    4         5      6      7
#   'initial : SOURCE SCRIPT COLON ENTRYORGUID EQUAL NUMBER script'
#   scriptList = p[7]

#   # guids are stored as negative values
#   if p[4] == "GUID":
#     p[6] = Number(p[6].value*(-1), p[6].type)

#   p[0] = [Script(sourceType = p[1], entry=p[6], event=ev, action=ac, target=ta) for (ev, ac, ta) in scriptList]

# def p_script_1(p):
#   # 0        1      2             3     4  5                6      7    8                 9      10
#   'script : AT SMART_EVENT_TYPE params DO SMART_ACTION_TYPE params ON SMART_TARGET_TYPE params script'
#   eConf = p[3]
#   eType = p[2]

#   aType = p[5]
#   aConf = p[6]

#   tType = p[8]
#   tConf = p[9]

#   t = (Event(eventType=eType, eventConf=eConf), Action(actionType=aType, actionConf= aConf), Target(targetType=tType, targetConf=tConf))
#   p[10].insert(0,t)
#   p[0] = p[10]

# def p_script_2(p):
#   'script : '
#   p[0] = []

# def p_params_1(p):
#   'params : PARAM_NAME EQUAL value params'
#   # add new parameter with its value to the dictionary

#   # dParams are the map for paramName -> paramValue
#   # lParams is the order of paramNames
#   (dParams, lParams) = p[4]

#   if p[1] in dParams.keys():
#     error(p.lineno(1), "Parameter defined twice or more.")

#   lParams.insert(0, p[1])
#   dParams[p[1]] = p[3]

#   p[0] = (dParams, lParams)

# def p_params_2(p):
#   'params : '
#   p[0] = ({},[])

# def p_value_1(p):
#   'value : val'
#   p[0] = [p[1]]

# def p_value_2(p):
#   'value : val PIPE value'

#   lValue = p[3]
#   lValue.append(p[1])
#   p[0] = lValue

# def p_val(p):
#   '''val : NUMBER
#          | SMART_EVENT_FLAG
#          | SMARTCAST_FLAG'''
#   p[0] = p[1]

def p_error(token):
    message = "Syntax error"
    if token is not None:
        message += "\ntype:" + token.type
        message += "\nvalue:" + str(token.value)
        message += "\nline:" + str(token.lineno)
        message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

# Build the parser
parser = yacc.yacc()

def parse(str):
    return parser.parse(str)
