import context
import src.parser as parser

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

        script = parser.parse(inputScript)

        self.assertEqual(script.entry, 25)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_UPDATE_OOC', 'value': 1})
        self.assertEqual(script.event.eventId,6)
        self.assertEqual(script.event.eventLink,5)
        self.assertEqual(script.event.eventChance,100)
        self.assertEqual(script.event.eventPhase,0)     
        self.assertEqual(script.event.eventFlags,10)
        self.assertEqual(script.event.param1,1000)        
        self.assertEqual(script.event.param2,1000)
        self.assertEqual(script.event.param3,1000)
        self.assertEqual(script.event.param4,1000)

        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.param1,1)
        self.assertEqual(script.action.param2,2)
        self.assertEqual(script.action.param3,4)
        self.assertEqual(script.action.param4,0)
        self.assertEqual(script.action.param5,0)
        self.assertEqual(script.action.param6,0)

        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})
        self.assertEqual(script.target.param1,0)
        self.assertEqual(script.target.param2,0)
        self.assertEqual(script.target.param3,0)
        self.assertEqual(script.target.paramX,0)
        self.assertEqual(script.target.paramY,0)
        self.assertEqual(script.target.paramZ,0) 
        self.assertEqual(script.target.paramO,0)

if __name__ == '__main__':
    unittest.main()