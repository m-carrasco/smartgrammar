import sys
sys.path.append('../')

import context
import src.lexer as lexer

import unittest

# Theses are lexer test. They don't necessary have a correct semantic
class TestLexer(unittest.TestCase):

    def test_1(self):
        script = ''' 
            CREATURE SCRIPT: ENTRY = 25
            AT SMART_EVENT_UPDATE_IC
                eventId=1
                eventLink=0
                eventPhaseMask=8
                eventFlags=SMART_EVENT_FLAG_NOT_REPEATABLE
                eventChance=50
            DO SMART_ACTION_CAST
                param1=30
                param2=0
            ON SMART_TARGET_CLOSEST_CREATURE
                param1=0
                param2=100
        '''
        # manually checked
        res = '''[LexToken(CREATURE,'CREATURE',2,14), LexToken(SCRIPT,'SCRIPT',2,23), LexToken(COLON,':',2,29), LexToken(ENTRY,'ENTRY',2,31), LexToken(EQUAL,'=',2,37), LexToken(NUMBER,{'type': 'int', 'value': 25},2,39), LexToken(AT,'AT',3,54), LexToken(SMART_EVENT_TYPE,{'value': 0, 'name': 'SMART_EVENT_UPDATE_IC'},3,57), LexToken(ID,'eventId',4,95), LexToken(EQUAL,'=',4,102), LexToken(NUMBER,{'type': 'int', 'value': 1},4,103), LexToken(LINK,'eventLink',5,121), LexToken(EQUAL,'=',5,130), LexToken(NUMBER,{'type': 'int', 'value': 0},5,131), LexToken(EVENT_PHASE_MASK,'eventPhaseMask',6,149), LexToken(EQUAL,'=',6,163), LexToken(NUMBER,{'type': 'int', 'value': 8},6,164), LexToken(EVENT_FLAGS,'eventFlags',7,182), LexToken(EQUAL,'=',7,192), LexToken(SMART_EVENT_FLAG,{'value': 1.0, 'name': 'SMART_EVENT_FLAG_NOT_REPEATABLE'},7,193), LexToken(EVENT_CHANCE,'eventChance',8,241), LexToken(EQUAL,'=',8,252), LexToken(NUMBER,{'type': 'int', 'value': 50},8,253), LexToken(DO,'DO',9,268), LexToken(SMART_ACTION_TYPE,{'value': 11, 'name': 'SMART_ACTION_CAST'},9,271), LexToken(PARAM_1,'param1',10,305), LexToken(EQUAL,'=',10,311), LexToken(NUMBER,{'type': 'int', 'value': 30},10,312), LexToken(PARAM_2,'param2',11,331), LexToken(EQUAL,'=',11,337), LexToken(NUMBER,{'type': 'int', 'value': 0},11,338), LexToken(ON,'ON',12,352), LexToken(SMART_TARGET_TYPE,{'value': 19, 'name': 'SMART_TARGET_CLOSEST_CREATURE'},12,355), LexToken(PARAM_1,'param1',13,401), LexToken(EQUAL,'=',13,407), LexToken(NUMBER,{'type': 'int', 'value': 0},13,408), LexToken(PARAM_2,'param2',14,426), LexToken(EQUAL,'=',14,432), LexToken(NUMBER,{'type': 'int', 'value': 100},14,433)]'''
        #self.assertEqual(str(lexer.apply(script)), res)
        print(str(lexer.apply(script)))
if __name__ == '__main__':
    unittest.main()