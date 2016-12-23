import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from .lexer import tokens
from .expressions import Script, Event, Action, Target

# resume of productions
# remember that newlines, tab and spaces are ignored

# initial : CREATURE SCRIPT COLON ENTRY EQUAL NUMBER script

# script : AT SMART_EVENT_TYPE params DO SMART_ACTION_TYPE params ON SMART_TARGET_TYPE params script | lambda

# theses productions generate a dictionary that is indexed by the string name of a parameter
# params : PARAM_NAME EQUAL value params | lambda

# value generates a list.
# value : val PIPE value | val
# val : NUMBER | SMART_EVENT_FLAG | SMARTCAST_FLAG

# handling custom errors

def error(line,msg):
  raise Exception("Line:%d Error: %s" % (line,msg))

def p_initial(p):
  # 0          1        2      3    4      5      6      7
  'initial : CREATURE SCRIPT COLON ENTRY EQUAL NUMBER script'
  scriptList = p[7]

  p[0] = [Script(entry=p[6], event=ev, action=ac, target=ta) for (ev, ac, ta) in scriptList]

def p_script_1(p):
  # 0        1      2             3     4  5                6      7    8                 9      10
  'script : AT SMART_EVENT_TYPE params DO SMART_ACTION_TYPE params ON SMART_TARGET_TYPE params script'
  eConf = p[3]
  eType = p[2]

  aType = p[5]
  aConf = p[6]

  tType = p[8]
  tConf = p[9]

  t = (Event(eventType=eType, eventConf=eConf), Action(actionType=aType, actionConf= aConf), Target(targetType=tType, targetConf=tConf))
  p[10].insert(0,t)
  p[0] = p[10]

def p_script_2(p):
  'script : '
  p[0] = []

def p_params_1(p):
  'params : PARAM_NAME EQUAL value params'
  # add new parameter with its value to the dictionary

  # dParams are the map for paramName -> paramValue
  # lParams is the order of paramNames
  (dParams, lParams) = p[4]

  if p[1] in dParams.keys():
    error(p.lineno(1), "Parameter defined twice or more.")

  lParams.insert(0, p[1])
  dParams[p[1]] = p[3]

  p[0] = (dParams, lParams)

def p_params_2(p):
  'params : '
  p[0] = ({},[])

def p_value_1(p):
  'value : val'
  p[0] = [p[1]]

def p_value_2(p):
  'value : val PIPE value'

  lValue = p[3]
  lValue.append(p[1])
  p[0] = lValue

def p_val(p):
  '''val : NUMBER
         | SMART_EVENT_FLAG
         | SMARTCAST_FLAG'''
  p[0] = p[1]

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
    """Dado un string, me lo convierte a SVG."""
    return parser.parse(str)
