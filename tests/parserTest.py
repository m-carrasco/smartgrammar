import context
import src.parser as parser
import src.expressions as exp

import unittest

# Theses are lexer test. They don't necessary have a correct semantic
class TestParser(unittest.TestCase):

    def test_1(self):
        inputScript = ''' 
                CREATURE SCRIPT: ENTRY=25
                AT SMART_EVENT_UPDATE_OOC
                    eventId=6
                    eventLink=5
                    eventChance=100
                    eventPhaseMask=0
                    eventFlags=10
                    param1=1000
                    param2=1000
                    param3=1000
                    param4=1000
                DO SMART_ACTION_CAST
                    param1=1
                    param2=2
                    param3=4
                ON SMART_TARGET_SELF
        '''

        script = parser.parse(inputScript)[0]

        self.assertEqual(script.entry.value, 25)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_UPDATE_OOC', 'value': 1})
        self.assertEqual(script.event.eventId,[exp.Number(6,'int')])
        self.assertEqual(script.event.eventLink,[exp.Number(5,'int')])
        self.assertEqual(script.event.eventChance,[exp.Number(100,'int')])
        self.assertEqual(script.event.eventPhase,[exp.Number(0,'int')])     
        self.assertEqual(script.event.eventFlags,[exp.Number(10,'int')])
        self.assertEqual(script.event.param1,[exp.Number(1000,'int')])        
        self.assertEqual(script.event.param2,[exp.Number(1000,'int')])
        self.assertEqual(script.event.param3,[exp.Number(1000,'int')])
        self.assertEqual(script.event.param4,[exp.Number(1000,'int')])

        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.param1,[exp.Number(1,'int')])
        self.assertEqual(script.action.param2,[exp.Number(2,'int')])
        self.assertEqual(script.action.param3,[exp.Number(4,'int')])
        self.assertEqual(script.action.param4,[exp.Number(0,'int')])
        self.assertEqual(script.action.param5,[exp.Number(0,'int')])
        self.assertEqual(script.action.param6,[exp.Number(0,'int')])

        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})
        self.assertEqual(script.target.param1,[exp.Number(0,'int')])
        self.assertEqual(script.target.param2,[exp.Number(0,'int')])
        self.assertEqual(script.target.param3,[exp.Number(0,'int')])
        self.assertEqual(script.target.paramX,[exp.Number(0,'int')])
        self.assertEqual(script.target.paramY,[exp.Number(0,'int')])
        self.assertEqual(script.target.paramZ,[exp.Number(0,'int')]) 
        self.assertEqual(script.target.paramO,[exp.Number(0,'int')])

if __name__ == '__main__':
    unittest.main()