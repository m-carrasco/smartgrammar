import context
import src.parser as parser
import src.expressions as exp

import unittest

class TestParser(unittest.TestCase):

    def test_1(self):
        inputScript = '''
            TYPE CREATURE ENTRY 37127

            PHASE(0)
            CHANCE(100)
            SMART_EVENT_UPDATE_IC(1000,8000,8000,10000)
            SMART_ACTION_CAST(71270)
            SMART_TARGET_SELF()
        '''

        script = parser.parse(inputScript)[0]

        self.assertEqual(script.entry.value, 37127)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_UPDATE_IC', 'value': 0})
        self.assertEqual(script.event.eventId,exp.Number(0,'int'))
        self.assertEqual(script.event.eventLink,exp.Number(0,'int'))
        self.assertEqual(script.event.eventChance,exp.Number(100,'int'))
        self.assertEqual(script.event.eventPhase,exp.Number(0,'int'))
        self.assertEqual(script.event.eventFlags,exp.Number(0,'int'))
        self.assertEqual(script.event.params[0],exp.Number(1000,'int'))
        self.assertEqual(script.event.params[1],exp.Number(8000,'int'))
        self.assertEqual(script.event.params[2],exp.Number(8000,'int'))
        self.assertEqual(script.event.params[3],exp.Number(10000,'int'))

        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],exp.Number(71270,'int'))

        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})

    def test_2(self):
        inputScript = '''
            TYPE CREATURE ENTRY 37127

            PHASE(0)
            CHANCE(100)
            SMART_EVENT_UPDATE_IC(1000,8000,8000,10000)
            SMART_ACTION_CAST(71270)
            SMART_TARGET_SELF()

            PHASE(0)
            CHANCE(100)
            SMART_EVENT_UPDATE_OOC(1000,8000,8000,10000)
            SMART_ACTION_CAST(71270)
            SMART_TARGET_SELF()

            PHASE(0)
            CHANCE(100)
            SMART_EVENT_AGGRO()
            SMART_ACTION_CAST(*spellId=71270)
            SMART_TARGET_SELF()
        '''
        scripts = parser.parse(inputScript)
        script = scripts[0]

        self.assertEqual(script.entry.value, 37127)

        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_UPDATE_IC', 'value': 0})
        self.assertEqual(script.event.eventId,exp.Number(0,'int'))
        self.assertEqual(script.event.eventLink,exp.Number(0,'int'))
        self.assertEqual(script.event.eventChance,exp.Number(100,'int'))
        self.assertEqual(script.event.eventPhase,exp.Number(0,'int'))
        self.assertEqual(script.event.eventFlags,exp.Number(0,'int'))
        self.assertEqual(script.event.params[0],exp.Number(1000,'int'))
        self.assertEqual(script.event.params[1],exp.Number(8000,'int'))
        self.assertEqual(script.event.params[2],exp.Number(8000,'int'))
        self.assertEqual(script.event.params[3],exp.Number(10000,'int'))

        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],exp.Number(71270,'int'))

        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})

        script = scripts[1]

        self.assertEqual(script.entry.value, 37127)
        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_UPDATE_OOC', 'value': 1})
        self.assertEqual(script.event.eventId,exp.Number(1,'int'))
        self.assertEqual(script.event.eventLink,exp.Number(0,'int'))
        self.assertEqual(script.event.eventChance,exp.Number(100,'int'))
        self.assertEqual(script.event.eventPhase,exp.Number(0,'int'))
        self.assertEqual(script.event.eventFlags,exp.Number(0,'int'))
        self.assertEqual(script.event.params[0],exp.Number(1000,'int'))
        self.assertEqual(script.event.params[1],exp.Number(8000,'int'))
        self.assertEqual(script.event.params[2],exp.Number(8000,'int'))
        self.assertEqual(script.event.params[3],exp.Number(10000,'int'))

        script = scripts[2]

        self.assertEqual(script.entry.value, 37127)

        self.assertEqual(script.event.eventType,{'name': 'SMART_EVENT_AGGRO', 'value': 4})
        self.assertEqual(script.event.eventId,exp.Number(2,'int'))
        self.assertEqual(script.event.eventLink,exp.Number(0,'int'))
        self.assertEqual(script.event.eventChance,exp.Number(100,'int'))
        self.assertEqual(script.event.eventPhase,exp.Number(0,'int'))
        self.assertEqual(script.event.eventFlags,exp.Number(0,'int'))
        self.assertEqual(script.event.params[0],exp.Number(0,'int'))
        self.assertEqual(script.event.params[1],exp.Number(0,'int'))
        self.assertEqual(script.event.params[2],exp.Number(0,'int'))
        self.assertEqual(script.event.params[3],exp.Number(0,'int'))

        self.assertEqual(script.action.actionType, {'name': 'SMART_ACTION_CAST', 'value': 11})
        self.assertEqual(script.action.params[0],exp.Number(71270,'int'))

        self.assertEqual(script.target.targetType, {'name': 'SMART_TARGET_SELF', 'value': 1})

unittest.main()
