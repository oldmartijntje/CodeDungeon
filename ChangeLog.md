# Version 1.2.0

What has changed between version 1.1.0 and 1.2.0:

here is the full log: https://github.com/oldmartijntje/CodeDungeon/compare/40d74571732ab822ae121d2cb455c2c64dbcfb26...main

## Map editor:

When predefining an entity, you can change the level of an enemy by using a list, and you can add a + to add the number to the base level.

You can make a lock only lock strength or only lock an item (the thing you need to open the lock)

Maps stored in a dict, so you can have different types of maps

Exits changed (look in the readme under 1.2.0+)

DefaultTiles you can use on predefined tiles

replace "NONE" with "True" for it to use default loot or entity generator

## GameData json:

added version

There is an template

defaultLevelList added under "dungeon"

"unknown" under "appSettings"

Replaymode and Logging changed (under "debug")

enemyLoopPerEnemy under "debug"

Added "defaultTiles"

"missingTile" in "tiles"

"type" has extra options under "tiles-loot-consumable"

You need to pick "levelList" under "tiles-loot-special"

complete overhaul of "movementRules" under "tiles-entity"