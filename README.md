# smartgrammar
Smart Grammar is an expressive way to write smart scripts for the TrinityCore emulator. A smart scripts represents an AI done writing a SQL sentence. It's not easy to give semantic to a bulk of numbers and commas. In order to understand and write a script you waste a lot of time with SQL that's not prepared for a quicky understanding of the code. The idea behind this language is to ease the comprehension and implement a language with a better semantic and syntax than SQL for AIs.

## Example
```
TYPE CREATURE ENTRY 37127 // Ymirjar Frostbinder
PHASE(0)
CHANCE(100)
FLAGS(30) // normal dungeon, heroic dungeon, normal raid, heroic raid
SMART_EVENT_UPDATE_IC(*initialMin=1000, *initialMax=8000, *repeatMin=8000, *repeatMax=10000) 
SMART_ACTION_CAST(*spellId=71270) // Arctic Chill
SMART_TARGET_SELF()

```

The parser will generate the equivalent SQL:
```
INSERT INTO smart_scripts (entryorguid, source_type, id, link, event_type, event_phase_mask, event_chance, event_flags, event_param1, event_param2, event_param3, event_param4, action_type, action_param1, action_param2, action_param3, action_param4, action_param5,  action_param6, target_type, target_param1, target_param2, target_param3, target_x, target_y, target_z, target_o, comment)
VALUES (37127, 0, 0, 0, 0, 0, 100, 30, 1000,8000,8000, 10000, 11, 71270, 0, 0, 0, 0,0, 1, 0, 0, 0, 0, 0, 0, 0, '');
```

The smartgrammar code is easier to understand than the SQL sentences.

## Syntax

### Header

Every script must start with: ```TYPE SOURCE_TYPE ENTRYORGUID NUMBER ``` where:
- SOURCE_TYPE is any of the following strings: CREATURE, GAMEOBJECT, AREATRIGGER, EVENT, GOSSIP, QUEST, SPELL, TRANSPORT, INSTANCE, TIMED_ACTIONLIST
- ENTRYORGUID is the string ENTRY or GUID.
- NUMBER is the source entry or guid (both as positive integers).

Then the script requires the specification of event, action and target parameters (in that order).

### Event

Before specifying the event type you can define the following event attributes:

- Link (default: 0)
- Phase (default: 0)
- Flags (default: 0)
- Chance (default: 100)

You must use the following keywords (see first example):

- LINK
- PHASE
- FLAGS
- CHANCE

The order between this attributes doesn't matter. It is mandatory that they are before the event type.

Then you must set the event type. Currently the event's are named in the same way as in the TC source. For example: SMART_EVENT_UPDATE_OOC

In order to set the parameters of the event you must do the following:

```
SMART_EVENT_TYPE(NUMBER, ..., NUMBER)
```
The parameter list can have up to 4 numbers. Any parameter that's not set will have value 0 as default.

An alternative is to use custom parameters names. Read the custom parameters section or see the first example (above).
### Action

The action is set using the TC naming for actions. It is done like this:

```
SMART_ACTION_TYPE(NUMBER, ..., NUMBER)
```
The parameter list can have up to 6 numbers. Any parameter that's not set will have value 0 as default.

An alternative is to use custom parameters names. Read the custom parameters section or see the first example (above).

### Target

Target type follows the same convention as the TC source code. The parameters are set like this:

```
SMART_TARGET_TYPE(NUMBER, ..., NUMBER)
```

The first 3 numbers are for param1, param2, param3 (described in the tc wiki).
The latters are for paramX, paramY, paramZ, paramO.

If you only want to set the value of paramX, ..., param0 you must set the default values for param1,param2,param3.

Example: You just want to set paramX

```
SMART_TARGET_TYPE(0,0,0,15.5)
```

An alternative is to use custom parameters names. Read the custom parameters section or see the first example (above).

### Custom parameter names

Custom parameter names can be defined as you wish but the order is important. 

For instance (they can be used for ACTION and TARGET types):

```
SMART_EVENT_TYPE(*dsagfas=12512, *param4=51)
```
The parser will consider 12512 the value for param1 and 51 for param2. The rest of the parameters will have value 0.

## Instructions

1. Write your smartgrammar script in a file
2. In the root directory of the repository from the console execute main.py specifying the file name. ie: python3 main.py input.in
