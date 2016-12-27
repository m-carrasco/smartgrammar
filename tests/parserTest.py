import context
import src.parser as parser
import src.expressions as exp

import unittest

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
        self.assertEqual(script.event.params[0],[exp.Number(1000,'int')])
        self.assertEqual(script.event.params[1],[exp.Number(1000,'int')])
        self.assertEqual(script.event.params[2],[exp.Number(1000,'int')])
        self.assertEqual(script.event.params[3],[exp.Number(1000,'int')])

        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],[exp.Number(1,'int')])
        self.assertEqual(script.action.params[1],[exp.Number(2,'int')])
        self.assertEqual(script.action.params[2],[exp.Number(4,'int')])
        self.assertEqual(script.action.params[3],[exp.Number(0,'int')])
        self.assertEqual(script.action.params[4],[exp.Number(0,'int')])
        self.assertEqual(script.action.params[5],[exp.Number(0,'int')])

        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})
        self.assertEqual(script.target.params[0],[exp.Number(0,'int')])
        self.assertEqual(script.target.params[1],[exp.Number(0,'int')])
        self.assertEqual(script.target.params[2],[exp.Number(0,'int')])
        self.assertEqual(script.target.paramX,[exp.Number(0,'int')])
        self.assertEqual(script.target.paramY,[exp.Number(0,'int')])
        self.assertEqual(script.target.paramZ,[exp.Number(0,'int')])
        self.assertEqual(script.target.paramO,[exp.Number(0,'int')])

    def test_2(self):
        inputScript = """
            CREATURE SCRIPT: ENTRY=11897
            AT SMART_EVENT_UPDATE_IC
                eventId=0
                param1=5000
                param2=8000
                param3=12000
                param4=15000
            DO SMART_ACTION_CAST
                param1=77522
            ON SMART_TARGET_VICTIM
            AT SMART_EVENT_RANGE
                eventId=1
                param1=0
                param2=8
                param3=15000
                param4=25000
            DO SMART_ACTION_CAST
                param1=8281
            ON SMART_TARGET_SELF
        """
        script = parser.parse(inputScript)[0]

        self.assertEqual(script.entry.value, 11897)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_UPDATE_IC', 'value': 0})
        self.assertEqual(script.event.eventId,[exp.Number(0,'int')])
        self.assertEqual(script.event.params[0],[exp.Number(5000,'int')])
        self.assertEqual(script.event.params[1],[exp.Number(8000,'int')])
        self.assertEqual(script.event.params[2],[exp.Number(12000,'int')])
        self.assertEqual(script.event.params[3],[exp.Number(15000,'int')])
        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],[exp.Number(77522,'int')])
        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_VICTIM', 'value': 2})

        script = parser.parse(inputScript)[1]

        self.assertEqual(script.entry.value, 11897)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_RANGE', 'value': 9})
        self.assertEqual(script.event.eventId,[exp.Number(1,'int')])
        self.assertEqual(script.event.params[0],[exp.Number(0,'int')])
        self.assertEqual(script.event.params[1],[exp.Number(8,'int')])
        self.assertEqual(script.event.params[2],[exp.Number(15000,'int')])
        self.assertEqual(script.event.params[3],[exp.Number(25000,'int')])
        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],[exp.Number(8281,'int')])
        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})

    def test_3(self):
        inputScript = """
            CREATURE SCRIPT: ENTRY=11897
            AT SMART_EVENT_UPDATE_IC
                eventId=0
                *initialMin=5000
                *initialMax=8000
                *repeatMin=12000
                *repeatMax=15000
            DO SMART_ACTION_CAST
                *spellId=77522
            ON SMART_TARGET_VICTIM
            AT SMART_EVENT_RANGE
                eventId=1
                *minDist=0
                *maxDist=8
                *repeatMin=15000
                *repeatMax=25000
            DO SMART_ACTION_CAST
                param1=8281
            ON SMART_TARGET_SELF
        """
        script = parser.parse(inputScript)[0]

        self.assertEqual(script.entry.value, 11897)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_UPDATE_IC', 'value': 0})
        self.assertEqual(script.event.eventId,[exp.Number(0,'int')])
        self.assertEqual(script.event.params[0],[exp.Number(5000,'int')])
        self.assertEqual(script.event.params[1],[exp.Number(8000,'int')])
        self.assertEqual(script.event.params[2],[exp.Number(12000,'int')])
        self.assertEqual(script.event.params[3],[exp.Number(15000,'int')])
        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],[exp.Number(77522,'int')])
        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_VICTIM', 'value': 2})

        script = parser.parse(inputScript)[1]

        self.assertEqual(script.entry.value, 11897)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_RANGE', 'value': 9})
        self.assertEqual(script.event.eventId,[exp.Number(1,'int')])
        self.assertEqual(script.event.params[0],[exp.Number(0,'int')])
        self.assertEqual(script.event.params[1],[exp.Number(8,'int')])
        self.assertEqual(script.event.params[2],[exp.Number(15000,'int')])
        self.assertEqual(script.event.params[3],[exp.Number(25000,'int')])
        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],[exp.Number(8281,'int')])
        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})

    def test_4(self):
        inputScript=""" GAMEOBJECT SCRIPT: GUID=150197
                   AT SMART_EVENT_GOSSIP_HELLO
                    eventFlags=SMART_EVENT_FLAG_DIFFICULTY_0|SMART_EVENT_FLAG_DIFFICULTY_1
                   DO SMART_ACTION_INVOKER_CAST
                    *spellId=71281
                   ON SMART_TARGET_ACTION_INVOKER"""

        script = parser.parse(inputScript)[0]

        self.assertEqual(script.entry.value,-150197)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_GOSSIP_HELLO', 'value': 64})
        self.assertEqual(script.event.eventId,[exp.Number(0,'int')])
        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_INVOKER_CAST', 'value': 85})
        self.assertEqual(script.action.params[0],[exp.Number(71281,'int')])
        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_ACTION_INVOKER', 'value': 7})

        self.assertEqual(exp.orFlags(script.event.eventFlags), 6)
if __name__ == '__main__':
    unittest.main()
