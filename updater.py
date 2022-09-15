import json
import os
import CodeDungeon

if os.path.exists(f'gameData/gameData.json'):
  gameData = open("gameData/gameData.json", "r")
  gameDataText = gameData.read()
  gameData.close()
  gameDataTextSplitted = gameDataText.split('trenght')
  gameDataNewText = 'trength'.join(gameDataTextSplitted)
  player = CodeDungeon.System()
  player.dataDict = json.loads(gameDataNewText)
  player.updateGameDataDict()
  player.exit(True, True)
  player = ''
  
player = CodeDungeon.System()
if 'version' not in player.dataDict:
  player.dataDict['version'] = dict(player.version)
if 'dungeon' not in player.dataDict:
  player.dataDict['dungeon'] = {'startLevel': 3, "defaultLevelList": "default"}
elif 'defaultLevelList' not in player.dataDict['dungeon']:
  player.dataDict['dungeon']["defaultLevelList"] = "default"
if 'defaultTiles' not in player.dataDict:
  player.dataDict['defaultTiles'] = {'floor': ['floor'], 'wall': ['wall'], 'exit': ['exit'], 'sign': ['sign'], 'npc': ['npc']}
if 'enemyLoopPerEnemy' not in player.dataDict['debug']:
  player.dataDict['debug']['enemyLoopPerEnemy'] = 2
for tile in player.dataDict['tiles']:
  if "enemy" in player.dataDict['tiles'][tile]:
    if 'doubleAttack' in player.dataDict['tiles'][tile]["enemy"]:
      del player.dataDict['tiles'][tile]["enemy"]['doubleAttack']
if "missingTile" not in player.dataDict['tiles']:
  player.dataDict['tiles']['missingTile'] = {'ShowOutsideAs': 'missingTile', 'Walkable': True,'Image': 'textureMissing', 'isEnemy': False, 'isInteractable': False,'isLoot': False}

player.updateGameDataDict()

if type(player._defaultlevels) == list:
  defaultLevelsDict = {}
  defaultLevelsDict[player.dataDict['dungeon']["defaultLevelList"]] = player._defaultlevels
  player._defaultlevels = defaultLevelsDict

player.updateLevelDataDict()

player.exit()