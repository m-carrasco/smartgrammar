# smartgrammar
Smart Grammar is an expressive way to write smart scripts for the TrinityCore emulator. A smart scripts represents an AI done writing a SQL sentence. It's not easy to give semantic to a bulk of numbers and commas. In order to understand and write a script you waste a lot of time with SQL that's not prepared for a quicky understanding of the code. The idea behind this language is to ease the comprehension and implement a language with a better semantic and syntax than SQL for AIs.

## Example
```
CREATURE SCRIPT: ENTRY=11897 
AT SMART_EVENT_UPDATE_IC 
  eventId=0 
  initialMin=5000 
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
```

The parser will generate the equivalent SQL:
```
INSERT INTO smart_scripts (entryorguid, source_type, id, link, event_type, event_phase_mask, event_chance, event_flags, event_param1, event_param2, event_param3, event_param4, action_type, action_param1, action_param2, action_param3, action_param4, action_param5,  action_param6, target_type, target_param1, target_param2, target_param3, target_x, target_y, target_z, target_o, comment)
VALUES (11897, 0, 0, 0, 0, 0, 100, 0, 5000,8000,12000, 15000, 11, 77522, 0, 0, 0, 0,0, 2, 0, 0, 0, 0, 0, 0, 0, '');

INSERT INTO smart_scripts (entryorguid, source_type, id, link, event_type, event_phase_mask, event_chance, event_flags, event_param1, event_param2, event_param3, event_param4, action_type, action_param1, action_param2, action_param3, action_param4, action_param5,  action_param6, target_type, target_param1, target_param2, target_param3, target_x, target_y, target_z, target_o, comment)
VALUES (11897, 0, 1, 0, 9, 0, 100, 0, 0,8,15000, 25000, 11, 8281, 0, 0, 0, 0,0, 1, 0, 0, 0, 0, 0, 0, 0, '');
```

The smartgrammar code is easier to understand than the SQL sentences.

## Syntax

### Header

Every script must start with: ```CREATURE SCRIPT: ENTRY=ENTRY_NUMBER``` where ENTRY_NUMBER is the creature entry (an integer).

Then the script requires the specification of event, action and target parameters. 

### Event

First you must declare the event type by writing: ```AT SMART_EVENT_XX``` where SMART_EVENT_XX is one of the labels defined in the TrinityCore wiki.

Then you must write the parameters. This is the list of the common parameters between smart events:

- eventId
- eventPhase
- eventChance
- eventFlags
- eventLink

If they are not set in the smartgrammar code the default value will be 0. For eventFlags you can use the labels defined in the TrinityCore wiki and add them together. For instance eventFlags= FLAG_1 | FLAG_5 where FLAG_1 and FLAG_5 are labels defined in the wiki.

As you can see in the first example of this documentation just eventId is set but you can set the rest if needed.

Then it's time for the parameters of the event type you choose. If it is SMART_EVENT_UPDATE_IC you should set the timers or if it is SMART_EVENT_ACCEPTED_QUEST you must specify a questId. Check the TrinityCore wiki in order to know how many paramters your event type requires.

You have two options here.

Firstly you can use the default parameters name: param1, param2, param3 and param4.

For instance SMART_EVENT_ACCEPTED_QUEST just use one parameter so you should only use param1:

```
param1=12512
```

Secondly you can define your own parameter names using the character * (asterisk).

```
*questId=12512
```

```
*whatever=12512
```
Notice that if you use custom parameter names you must not use the default parameters names for the rest of the event configuration.

If event type parameters are not set the default value will be 0.

### Action

First you must declare the action type by writing: ```DO SMART_ACTION_XX``` where SMART_ACTION_XX is one of the labels defined in the TrinityCore wiki.

Then it's time for the parameters of the action type you choose. If it is SMART_ACTION_SET_FACTION you should set the factionId or if it is SMART_ACTION_CAST you must specify a spellId, castFlags and trigger options. Check the TrinityCore wiki in order to know how many paramters your event type requires.

You have two options here.

Firstly you can use the default parameters name: param1, param2, param3, param4, param5 and param6

For instance SMART_ACTION_SET_FACTION just use one parameter so you should only use param1:

```param1=20
```

Secondly you can define your own parameter names using the character * (asterisk).

```
*factionId=12512
```

```
*whatever=12512
```

Notice that if you use custom parameter names you must not use the default parameters names for the rest of the action configuration.

If action type parameters are not set the default value will be 0.

### Target

First you must declare the target type by writing: ```DO SMART_TARGET_XX``` where SMART_TARGET_XX is one of the labels defined in the TrinityCore wiki.

Then it's time for the parameters of the target type you choose. If it is SMART_TARGET_SELF you don't need any parameter or if it is SMART_TARGET_CLOSEST_FRIENDLY you must specify a distance and if it is a player. Check the TrinityCore wiki in order to know how many paramters your event type requires.

You have two options here.

Firstly you can use the default parameters name: param1, param2, param3
Secondly you can define your own parameter names using the character * (asterisk).

Notice that if you use custom parameter names you must not use the default parameters names for the rest of the target configuration.

Also keep in mind that parameters paramX, paramY, paramZ and paramO are not customizable. You must use these names.
If action type parameters are not set the default value will be 0.

### Custom parameter names

Custom parameter names can be defined as you wish but the order is important. 

For instance:

```
*customName2=12512
*abcdefgh=156
```
The parser will consider 12512 the value for param1 and 156 for param2. The rest of the parameters will have value 0.

Also keep in mind that if you use the default parameter names you can switch the order

```
param4=12512
param3=156
```
param4 will have value 12512 and param3 will have value 156. The rest of the parameters will have value 0.

## Instructions

1. Write your smartgrammar script in a file
2. In the root directory of the repository from the console execute main.py specifying the file name. ie: python3 main.py input.in



