import context
import src.parser as parser

import unittest

# Theses are lexer test. They don't necessary have a correct semantic
class TestParser(unittest.TestCase):

    def test_1(self):
        script = ''' 
                CREATURE SCRIPT: ENTRY=25
                AT SMART_EVENT_UPDATE_OOC
                    eventId=0
                    eventLink=0
                    eventChance=100
                    eventPhaseMask=0
                    eventFlags=0
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
        src.parse(script)

if __name__ == '__main__':
    unittest.main()