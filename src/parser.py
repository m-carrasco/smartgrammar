import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from .lexer import tokens
from .expressions import Script, Event, Action, Target
# resume of productions
# remember that newlines, tab and spaces are ignored

# script : CREATURE SCRIPT COLON ENTRY EQUAL NUMBER AT SMART_EVENT_TYPE eventconf DO SMART_ACTION_TYPE actionconf ON SMART_TARGET_TYPE targetconf

# eventconf : eventparam eventconf
# eventconf : 
# eventparam : ID EQUAL NUMBER
# eventparam : LINK EQUAL NUMBER
# eventparam : EVENT_PHASE_MASK EQUAL NUMBER
# eventparam : EVENT_CHANCE EQUAL NUMBER
# eventparam : EVENT_FLAGS EQUAL NUMBER
# eventparam : PARAM_1 EQUAL NUMBER
# eventparam : PARAM_2 EQUAL NUMBER
# eventparam : PARAM_3 EQUAL NUMBER
# eventparam : PARAM_4 EQUAL NUMBER

# actionconf : actionparam actionconf
# actionconf : 
# actionparam : PARAM_1 EQUAL NUMBER
# actionparam : PARAM_2 EQUAL NUMBER
# actionparam : PARAM_3 EQUAL NUMBER
# actionparam : PARAM_4 EQUAL NUMBER
# actionparam : PARAM_5 EQUAL NUMBER
# actionparam : PARAM_6 EQUAL NUMBER

# targetconf : targetparam targetconf
# targetconf :
# targetparam : PARAM_1 EQUAL NUMBER
# targetparam : PARAM_2 EQUAL NUMBER
# targetparam : PARAM_3 EQUAL NUMBER
# targetparam : PARAM_X EQUAL NUMBER
# targetparam : PARAM_Y EQUAL NUMBER
# targetparam : PARAM_Z EQUAL NUMBER
# targetparam : PARAM_O EQUAL NUMBER

def p_script(p):
  'script : CREATURE SCRIPT COLON ENTRY EQUAL NUMBER AT SMART_EVENT_TYPE eventconf DO SMART_ACTION_TYPE actionconf ON SMART_TARGET_TYPE targetconf'
  # 0           1      2      3     4    5     6      7   8           9      10   11            12     13   14           15 
  eConf = p[9]
  eType = p[8]

  aType = p[11]
  aConf = p[12]

  tType = p[14]
  tConf = p[15]

  p[0] = Script(entry=p[6]["value"],
                event=Event(eventType=eType, eventConf=eConf), 
                action=Action(actionType=aType, actionConf= aConf), 
                target=Target(targetType=tType, targetConf=tConf))

def p_event_conf_1(p):
  # 0            1          2
  'eventconf : eventparam eventconf'
  
  eConf = p[2] # event parameters parsed up to now - it is bottom up.
  (paramName, paramValue) = p[1]
  if eConf is None:
    p[0] = {paramName : paramValue}
  else:
    eConf[paramName] = paramValue
    p[0] = eConf

def p_event_conf_2(p):
  'eventconf : '
  p[0] = None

def p_event_param_1(p):
  'eventparam : ID EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_event_param_2(p):
  'eventparam : LINK EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_event_param_3(p):
  'eventparam : EVENT_PHASE_MASK EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])
  
def p_event_param_4(p):
  'eventparam : EVENT_CHANCE EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_event_param_5(p):
  'eventparam : EVENT_FLAGS EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_event_param_6(p):
  'eventparam : PARAM_1 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_event_param_7(p):
  'eventparam : PARAM_2 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_event_param_8(p):
  'eventparam : PARAM_3 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_event_param_9(p):
  'eventparam : PARAM_4 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_action_conf_1(p):
  'actionconf : actionparam actionconf'
  aConf = p[2] #  parameters parsed up to now - it is bottom up.
  (paramName, paramValue) = p[1]

  if aConf is None:
    p[0] = {paramName : paramValue}
  else:
    aConf[paramName] = paramValue
    p[0] = aConf

def p_action_conf_2(p):
  'actionconf : '
  p[0] = None

def p_action_param_1(p):
  'actionparam : PARAM_1 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_action_param_2(p):
  'actionparam : PARAM_2 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_action_param_3(p):
  'actionparam : PARAM_3 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])
  
def p_action_param_4(p):
  'actionparam : PARAM_4 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_action_param_5(p):
  'actionparam : PARAM_5 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_action_param_6(p):
  'actionparam : PARAM_6 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_target_conf_1(p):
  'targetconf : targetparam targetconf'
  tConf = p[2] #  parameters parsed up to now - it is bottom up.
  (paramName, paramValue) = p[1]

  if tConf is None:
    p[0] = {paramName : paramValue}
  else:
    tConf[paramName] = paramValue
    p[0] = tConf

def p_target_conf_2(p):
  'targetconf : '
  p[0] = None

def p_target_param_1(p):
  'targetparam : PARAM_1 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_target_param_2(p):
  'targetparam : PARAM_2 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])
  
def p_target_param_3(p):
  'targetparam : PARAM_3 EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])
  
def p_target_param_x(p):
  'targetparam : PARAM_X EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

def p_target_param_y(p):
  'targetparam : PARAM_Y EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])
  
def p_target_param_z(p):
  'targetparam : PARAM_Z EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])
  
def p_target_param_o(p):
  'targetparam : PARAM_O EQUAL NUMBER'
  p[0] = (p[1], p[3]["value"])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def parse(str):
    """Dado un string, me lo convierte a SVG."""
    return parser.parse(str)
