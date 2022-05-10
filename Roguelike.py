import json
import os
import string
import time
import accounts_omac
import random
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk, ImageEnhance
import math
    #0 air
    #1 wall
    #2 start
    #3 next level
    #4 high chance of loot
    #5 high chance of enemy
    #6 sign
    #7 npc
    #8 nothing able to spawn
    #9 bossfight




class System:

    _sightFurthest = []

    #some default levels
    _defaultlevels = [
    [[1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 1, 0, 4, 5, 1, 4, 1, 2], [4, 0, 0, 4, 0, 0, 0, 0, 1, 0], [5, 4, 1, 0, 5, 4, 1, 0, 1, 0], [4, 0, 1, 0, 4, 0, 1, 0, 1, 0], [1, 0, 1, 5, 0, 4, 1, 3, 1, 0], [0, 5, 4, 1, 1, 1, 1, 1, 1, 0], [4, 0, 0, 1, 4, 0, 0, 4, 0, 0], [0, 0, 4, 1, 0, 4, 5, 0, 0, 0], [5, 0, 0, 0, 0, 5, 0, 5, 1, 0], [4, 0, 0, 1, 4, 0, 0, 4, 1, 3]],
    [[4, 0, 4, 0, 1, 2, 1, 4, 5, 4], [4, 5, 0, 4, 1, 0, 1, 0, 4, 0], [0, 4, 0, 0, 0, 0, 1, 4, 5, 4], [0, 0, 4, 0, 1, 0, 1, 0, 4, 0], [4, 0, 5, 4, 1, 0, 0, 4, 5, 4], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 4, 0, 4, 1, 0, 1, 4, 0, 4], [4, 5, 4, 0, 1, 0, 1, 0, 5, 0], [0, 4, 0, 4, 0, 0, 1, 0, 4, 4], [4, 5, 4, 0, 1, 3, 1, 5, 0, 0]],
    [[4, 0, 4, 1, 0, 2, 1, 4, 5, 4], [4, 5, 0, 1, 7, 0, 1, 0, 4, 0], [0, 4, 0, 0, 1, 0, 1, 4, 5, 4], [0, 0, 4, 0, 0, 0, 1, 0, 4, 0], [4, 0, 5, 0, 1, 0, 0, 4, 5, 4], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0], [0, 4, 0, 4, 1, 0, 1, 4, 0, 4], [4, 5, 4, 0, 1, 0, 1, 0, 5, 0], [0, 4, 0, 4, 0, 0, 1, 0, 4, 4], [4, 5, 4, 0, 1, 3, 1, 5, 0, 7]],
    [[1, 4, 0, 0, 5, 0, 4, 1, 0, 3], [0, 1, 1, 1, 0, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 5, 0, 0], [2, 0, 1, 5, 0, 1, 0, 0, 1, 0], [0, 0, 4, 1, 0, 5, 1, 1, 4, 1], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 5, 1, 4, 1, 5, 1, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 1, 0, 5, 0, 0, 1, 1, 0, 1], [4, 0, 0, 1, 4, 0, 5, 0, 0, 5]],
    [[8, 8, 8, 8, 8, 8, 1, 2, 0, 0], [8, 8, 8, 8, 8, 8, 1, 0, 0, 0], [8, 8, 8, 8, 8, 8, 1, 0, 0, 0], [8, 8, 8, 8, 8, 8, 1, 0, 0, 0], [8, 8, 8, 8, 8, 8, 1, [6, 'Goodluck with the bossfight\nBeat him to spanw exit.'], 0, 0], [8, 8, 9, 8, 8, 8, 0, 0, 0, 0], [8, 8, 8, 8, 8, 8, 1, 0, 0, 0], [8, 8, 8, 8, 8, 8, 1, 0, 0, 0], [8, 8, 8, 8, 8, 8, 1, 0, 0, 4], [8, 8, 8, 8, 8, 8, 1, 4, 4, 4]],
    [[0, 0, 0, 0, 1, 6, 4, 1, 4, 7], [0, 1, 1, 5, 1, 0, 5, 1, 0, 0], [5, 1, 3, 0, 1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 5, 0, 0, 1, 0], [0, 0, 4, 1, 4, 0, 1, 5, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0, 6], [4, 1, 0, 0, 5, 0, 0, 1, 0, 1], [4, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 3, 0, 1, 4, 0, 1, 1, 5], [2, 1, 1, 0, 0, 0, 1, 3, 0, 0]],
    [[4, 5, 4, 0, 5, 0, 1, 4, 0, 0], [4, 4, 4, 1, 4, 5, 1, 5, 5, 4], [1, 1, 1, 1, 1, 0, 1, 4, 0, 0], [4, 0, 1, 0, 0, 0, 1, 1, 0, 1], [0, 5, 1, 0, 2, 0, 0, 0, 0, 0], [0, 4, 1, 0, 0, 4, 1, 1, 1, 5], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0], [4, 0, 0, 1, 0, 0, 0, 4, 1, 0], [0, 5, 5, 0, 0, 5, 0, 0, 1, 0], [4, 0, 4, 1, 4, 0, 0, 5, 1, 3]],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 0, 0, 0, 0, 1, 4, 0, 1], [1, 1, 0, 1, 1, 0, 0, 0, 0, 1], [1, 6, 0, 4, 1, 0, 1, 5, 4, 1], [1, 4, 0, 0, 1, 5, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 4, 0, 5, 1, 0, 0, 0, 4, 1], [1, 4, 0, 0, 1, 0, 1, 5, 0, 1], [1, 0, 0, 4, 1, 3, 1, 0, 4, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    ]
    
    
    _buttonsList = []
    #melee, throwables, magic
    _enemies = []
    _loot = []
    _itemRarety = {}
    _items = []
    _rarityChance= {}
    _images = {}

    #load Json
    try:
        os.mkdir('gameData/')
    except:
        pass
    if os.path.exists(f'gameData/gameData.json'):
        with open(f'gameData/gameData.json') as json_file:
            dataString = json.load(json_file)
            if type(dataString) != dict:
                dataDict = json.loads(dataString)
            else:
                dataDict= dataString
    else:
        dataDict = {}
        dataDict['playerImages'] = {'L': 'player left', 'R': 'player right'}
        dataDict['chance'] = {'enemyAir' : 5, 'enemySpawn': 40, 'lootAir' : 3, 'lootSpawn' : 40}
        dataDict['tiles'] = {'rat':{'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'rat', 'isEnemy': True, 'isInteractable': False,'isLoot': False}, 'exit':{'ShowOutsideAs': 'floor', 'Walkable': True,'Image': 'exit', 'isEnemy': False, 'isInteractable': False,'isLoot': False}, 'floor':{'ShowOutsideAs': 'floor','Walkable': True, 'Image': 'floor', 'isEnemy': False, 'isInteractable': False,'isLoot': False}, 'sign':{'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'sign', 'isEnemy': False, 'isInteractable': True,'isLoot': False, 'text': 'signText'}, 'wall':{'ShowOutsideAs': 'wall','Walkable': False, 'Image': 'wall', 'isEnemy': False, 'isInteractable': False,'isLoot': False}, 'npc':{'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'npc', 'isEnemy': False, 'isInteractable': True, 'isLoot': False, 'text': 'npcText'}, 'wooden sword':{'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': False, 'loot': {'amount' : 1,'rarity': 'common', 'weapon': True, 'weapon': {'minStrenght': 8, 'attack': 4, 'type': 'stab'}}}}
        dataDict['tiles']['Stone sword'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : 1,'rarity': 'uncommon', 'weapon': True, 'weapon': {'minStrenght': 10, 'attack': 5, 'type': 'stab'}}}
        dataDict['rarities'] = {'common': {'chance': 100},'uncommon': {'chance': 55},'rare': {'chance': 30},'epic': {'chance': 15},'legendary': {'chance': 5},'impossible': {'chance': 1}}
        dataDict['Gamma'] = {'distance': 2, 'darknessFull' : 0.2, 'darknessFade' : 0.5}
        dataDict['text'] = {'signText': ['YEET'], 'npcText': ['I am a sign']}
        dataDict['appSettings'] = {'offset': 18,'size': 32, 'maxTypes': 9, 'colors': ['white','black','green', 'blue', 'pink', 'red', 'brown', 'orange', 'white', 'purple']}
        json_string = json.dumps(dataDict)
        with open(f'gameData/gameData.json', 'w') as outfile:
            json.dump(json_string, outfile)
    
    #change json into usable data part1
    try:
        colors =dataDict['appSettings']['colors']
        _viewDistance = dataDict['Gamma']['distance']
        maxTypes = dataDict['appSettings']['maxTypes']
        chanceEnemyAir = dataDict['chance']['enemyAir']
        chanceLootAir = dataDict['chance']['lootAir']
        chanceEnemySpawn = dataDict['chance']['enemySpawn']
        chanceLootSpawn = dataDict['chance']['lootSpawn']
        pixelOffset = dataDict['appSettings']['offset']
        pixelSize = dataDict['appSettings']['size']
        darknessFull = dataDict['Gamma']['darknessFull']
        darknessFade = dataDict['Gamma']['darknessFade']
    except Exception as e:
        print(e)
        print('something is wrong with the gameData/gameData.json, delete it or fix it.')


    
    


    def __init__(self, seed : int = 0, startingDifficulty : int = 3):
        
        self._dungeonLevel = 0
        random.seed(seed)
        self.accountConfigSettings = accounts_omac.configFileTkinter()
        self.accountDataDict = accounts_omac.defaultConfigurations.defaultLoadingTkinter(self.accountConfigSettings)
        random.randint(1,10)
        self._nextStates = []
        self.newState()
        self.newState()
        self.checkStates()
        self._enemyLevel = startingDifficulty
        self._createdBefore = False
        self._playerX = 0
        self._playerY = 0
        self._facingDirectionTexture = 'R'
        self._facing = 'R'
        self.gameWindow = tkinter.Tk()
        self.gameWindow.configure(bg='black')


        self.rarityList = []
        for rar in self.dataDict['rarities'].keys():
            self.rarityList.append(rar)

        #if no account has been logged into
        if self.accountDataDict == False:
            exit()

        #change json into usable data part2
        for player in self.dataDict['playerImages'].keys():
            self._images[f'darknessFull-{self.dataDict["playerImages"][player]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['playerImages'][player]}.png").convert('RGB')).enhance(self.darknessFull))
            self._images[f'darknessFade-{self.dataDict["playerImages"][player]}'] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['playerImages'][player]}.png").convert('RGB')).enhance(self.darknessFade))
            self._images[f'normal-{self.dataDict["playerImages"][player]}'] = ImageTk.PhotoImage(Image.open(f"sprites/{self.dataDict['playerImages'][player]}.png"))
        for rarety in self.dataDict['rarities'].keys():
            self._itemRarety[rarety] = []
            self._rarityChance[rarety] = self.dataDict['rarities'][rarety]['chance']
        for data in self.dataDict['tiles'].keys():
            if self.dataDict['tiles'][data]['isEnemy']:
                self._enemies.append(data)
            if self.dataDict['tiles'][data]['isLoot']:
                self._itemRarety[self.dataDict['tiles'][data]['loot']['rarity']].append(data)
                self._items.append(data)
            self._images[f'darknessFull-{self.dataDict["tiles"][data]["Image"]}'.lower()] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png".lower()).convert('RGB')).enhance(self.darknessFull))
            self._images[f'darknessFade-{self.dataDict["tiles"][data]["Image"]}'.lower()] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png".lower()).convert('RGB')).enhance(self.darknessFade))
            self._images[f'normal-{self.dataDict["tiles"][data]["Image"]}'.lower()] = ImageTk.PhotoImage(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png".lower()))

    #generate a new state
    def newState(self, modifier = 0):
        for x in range(random.randint(1,10)+ modifier):
            random.randint(1,10)
        self._nextStates.append(random.getstate())
        for x in range(random.randint(1,10)+ modifier):
            random.randint(1,10)

    #check if states are valid
    def checkStates(self):
        x = 0
        while len(self._nextStates) > 2:
            self.newState()
        while self._nextStates[0] == self._nextStates[1]:
            x += 1
            self._nextStates.pop(0)
            self.newState(x)

    #load a state for the dungeon generation
    def loadState(self):
        random.setstate(self._nextStates[0])
        self._nextStates.pop(0)
        self.checkStates()

    #change tile type in the creator app
    def changeEditorButton(self,location, chosenLevel):
        x, y = location
        self._defaultlevels[chosenLevel][x][y]+= 1
        if self._defaultlevels[chosenLevel][x][y] > self.maxTypes:
            self._defaultlevels[chosenLevel][x][y] = 0
        self._buttonsList[x][y].configure(text=self._defaultlevels[chosenLevel][x][y], bg = self.colors[self._defaultlevels[chosenLevel][x][y]])

    #get a random rarity
    def itemRarity(self, modifier : int = 0):
        randomNumber = random.randint(0,100)
        randomNumber -= modifier
        chanceList = []

        for rarety in self.rarityList:
            chanceList.append(self._rarityChance[rarety] + modifier)
        return random.choices(self.rarityList, weights = chanceList, k = 1)[0]

    #generate loot
    def getLoot(self, modifier: int = 0):
        while True:
            itemType = self.itemRarity(modifier)
            if len(self._itemRarety[itemType]) != 0:
                break
        item = self._itemRarety[itemType][random.randint(0,len(self._itemRarety[itemType])-1)]
        amount = self.dataDict['tiles'][item]['loot']['amount']
        if type(amount) == list:
            amount = random.randint(amount[0], amount[1])
        loot = {'type':item, 'amount':amount}
        return loot

    #read tile of 2D erray and convert into map
    def readTile(self, tile, x, y, extra = 'NONE'):
        if tile == 0:
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= self.chanceEnemyAir:
                entityLoot = self.getLoot()
                entity = {'type': random.choice(list(self._enemies)), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
            if random.randint(1,100) <= self.chanceLootAir:
                loot = self.getLoot()
            self._currentLevel[x][y] = {'tile': 'floor', 'entity': entity, 'loot': loot} 
        elif tile == 1:
            self._currentLevel[x][y] = {'tile': 'wall', 'entity': 'NONE', 'loot': 'NONE'} 
        elif tile == 2:
            self._currentLevel[x][y] = {'tile': 'floor', 'entity': 'NONE', 'loot': 'NONE'} 
            self._playerX = x
            self._playerY = y
        elif tile == 3:
            self._currentLevel[x][y] = {'tile': 'exit', 'entity': 'NONE', 'loot': 'NONE'} 
        elif tile == 4:
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= self.chanceLootSpawn:
                loot = self.getLoot()
            self._currentLevel[x][y] = {'tile': 'floor', 'entity': entity, 'loot': loot}  
        elif tile == 5:
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= self.chanceEnemySpawn:
                entityLoot = self.getLoot()
                entity = {'type': random.choice(list(self._enemies)), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
            self._currentLevel[x][y] = {'tile': 'floor', 'entity': entity, 'loot': loot} 
        elif tile == 6:
            if extra != 'NONE':
                text = extra
            else:
                text = self.dataDict['text']['signText'][random.randint(0,len(self.dataDict['text']['signText'])-1)]
            self._currentLevel[x][y] = {'tile': 'sign', 'entity': 'NONE', 'loot': 'NONE', 'text': text} 
        elif tile == 7:
            if extra != 'NONE':
                text = extra
            else:
                text = self.dataDict['text']['npcText'][random.randint(0,len(self.dataDict['text']['npcText'])-1)]
            self._currentLevel[x][y] = {'tile': 'npc', 'entity': 'NONE', 'loot': 'NONE', 'text': text} 
        elif tile == 8:
            self._currentLevel[x][y] = {'tile': 'floor', 'entity': 'NONE', 'loot': 'NONE'}
        elif tile == 9:
            entity = 'NONE'
            loot = self.getLoot()
            entityLoot = self.getLoot(10)
            entity = {'type': random.choice(list(self._enemies)), 'level': random.randint(1,4)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
            self._currentLevel[x][y] = {'tile': 'floor', 'entity': entity, 'loot': loot}  
        if self._currentLevel[x][y]['entity']!= 'NONE':
            display = self._currentLevel[x][y]['entity']['type']
        elif self._currentLevel[x][y]['loot']!= 'NONE':
            display = self._currentLevel[x][y]['loot']['type']
        else:
            display = self._currentLevel[x][y]['tile']
        self._currentLevel[x][y]['display'] = display

    #create a level off a 2D erray
    def createLevel(self, level):
        if not any(2 in sublist for sublist in level):
            while not any(2 in sublist for sublist in level) and (any(0 in sublist for sublist in level) or any(8 in sublist for sublist in level)):
                tryLine = random.randint(0,len(level)-1)
                if 0 in level[tryLine] or 8 in level[tryLine]:
                    whereAir = [i for i, x in enumerate(level[tryLine]) if x == 0]
                    whereNonAir = [i for i, x in enumerate(level[tryLine]) if x == 8]
                    spawnable = whereAir + whereNonAir
                    level[tryLine][spawnable[random.randint(0,len(spawnable)-1)]] = 2
        if not any(3 in sublist for sublist in level) and not any(9 in sublist for sublist in level):
            while not any(3 in sublist for sublist in level) and (any(0 in sublist for sublist in level) or any(8 in sublist for sublist in level)):
                tryLine = random.randint(0,len(level)-1)
                if 0 in level[tryLine]or 8 in level[tryLine]:
                    whereAir = [i for i, x in enumerate(level[tryLine]) if x == 0]
                    whereNonAir = [i for i, x in enumerate(level[tryLine]) if x == 8]
                    spawnable = whereAir + whereNonAir
                    level[tryLine][spawnable[random.randint(0,len(spawnable)-1)]] = 3
        self._currentLevel = []
        for x in range(len(level)):
            self._currentLevel.append([])
            for y in range(len(level[x])):
                self._currentLevel[x].append({})
                if type(level[x][y]) == list:
                    self.readTile(level[x][y][0], x, y, level[x][y][1])
                else:
                    self.readTile(level[x][y], x, y)
        self.levelSize = [len(self._currentLevel), len(self._currentLevel[0])]

    #render how the dungeon looks like
    def rendering(self):
        self._sightFurthest = [] 
        for ix in range(self._viewDistance * 2 + 1):
            for iy in range(self._viewDistance * 2 + 1):
                self._sightFurthest.append(f'{ix + self._playerX - self._viewDistance}-{iy + self._playerY - self._viewDistance}')
        self._sight = [] 
        for ix in range(self._viewDistance * 2 +1 - (math.ceil(self._viewDistance/2)*2)):
            for iy in range(self._viewDistance * 2 + 1 - (math.ceil(self._viewDistance/2)*2)):
                self._sight.append(f'{ix + self._playerX - self._viewDistance+math.ceil(self._viewDistance/2)}-{iy + self._playerY - self._viewDistance+math.ceil(self._viewDistance/2)}')
        for x in range(len(self._currentLevel)):
            for y in range(len(self._currentLevel[x])):
                if f"{x}-{y}" in self._sightFurthest:
                    if f"{x}-{y}" in self._sight:
                        picType = 'normal-'.lower()
                    else:
                        picType = 'darknessFade-'.lower()
                else:
                    picType = 'darknessFull-'.lower()
                
                if x==self._playerX and y == self._playerY:
                    self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['playerImages'][self._facingDirectionTexture.upper()]}"])
                else:
                    if picType == 'darknessFull-'.lower():
                        self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['tiles'][self._currentLevel[x][y]['display']]['ShowOutsideAs']}"])
                    else:
                        self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['tiles'][self._currentLevel[x][y]['display']]['Image']}"])
        self.gameWindow.update_idletasks()      
        self.gameWindow.update()

    #create the window
    def createWindow(self):
        self._canvas = tkinter.Canvas(self.gameWindow, bg="black", height=len(self._currentLevel[0])*32, width=len(self._currentLevel)*32)
        self._canvas.pack()
        
    #startup the program
    def startGame(self, mode = 'Play', chosenLevel = 0):
        
        custom = False
        if str(mode).lower() not in ['play', 'create']:
            chosenLevel = mode
            mode = 'Play'
        if type(chosenLevel) == list:
            self._defaultlevels[0] = list(chosenLevel)
            chosenLevel = 0
            custom = True
        if type(chosenLevel) == str:
            if 'x' in str(chosenLevel):
                if chosenLevel.split('x')[0].isdigit() and chosenLevel.split('x')[1].isdigit():
                    level = []
                    for x in range(int(chosenLevel.split('x')[0])):
                        level.append([])
                        for y in range(int(chosenLevel.split('x')[1])):
                            if len(chosenLevel.split('x')) > 2:
                                if chosenLevel.split('x')[2].isdigit():
                                    level[x].append(int(chosenLevel.split('x')[2]))
                                else:
                                    level[x].append(0)
                            else:
                                level[x].append(0)
                    self._defaultlevels[0] = level
                    chosenLevel = 0
                    custom = True
        if not str(chosenLevel).isdigit():
            chosenLevel = 0
        self._buttonsList = []
        if mode.lower() == 'create':
            for x in range(len(self._defaultlevels[chosenLevel])):
                self._buttonsList.append([])
            for x in range(len(self._defaultlevels[chosenLevel])):
                for y in range(len(self._defaultlevels[chosenLevel][x])):
                    cords = [x,y]
                    self._buttonsList[x].append(tkinter.Button(self.gameWindow, text=self._defaultlevels[chosenLevel][x][y],bg = self.colors[self._defaultlevels[chosenLevel][x][y]], command=lambda cords=cords:self.changeEditorButton(cords, chosenLevel)))
                    self._buttonsList[x][y].grid(column=x, row=y)
            tkinter.Button(self.gameWindow, text='export',command=lambda: print(self._defaultlevels[chosenLevel])).grid(column=0,row=x+1,columnspan=y+1)
        if mode.lower() == 'play':
            self.checkStates()
            if custom == False:
                levelNumber = random.randint(0,len(self._defaultlevels)-1)
            else:
                levelNumber = chosenLevel
            print(levelNumber)
            self.createLevel(self._defaultlevels[levelNumber])
            self.createWindow()
            self.rendering()
        

    def exit(self):
        self.dataDict = accounts_omac.saveAccount(self.accountDataDict, self.accountConfigSettings)
        exit()

    #interact with something
    def interact(self):
        pass

    #check if tile is being able to be walked
    def isWalkable(self, cordinates = [0,0]):
        x,y = cordinates
        if x < 0 or y < 0 or y > self.levelSize[1]-1 or x > self.levelSize[0]-1:
            return False
        if x == self._playerX and y == self._playerY:
            return False
        return self.dataDict['tiles'][self._currentLevel[x][y]['display']]['Walkable']

    #calculate distance between 2 cordinates
    def distence(self, cord1, cord2):
        x1,y1 =cord1
        x2,y2 =cord2
        xDis = abs(x1-x2)
        yDis = abs(y1-y2)
        distance = math.sqrt((xDis **2) + (yDis **2))
        return distance

    #check if enemy's want to move
    def enemyTurn(self):
        self.EnemyMoveRadius = [] 
        for ix in range(self._viewDistance+1 * 2 + 1):
            for iy in range(self._viewDistance+1 * 2 + 1):
                self.EnemyMoveRadius.append([ix + self._playerX - self._viewDistance,iy + self._playerY - self._viewDistance])
        for tile in self.EnemyMoveRadius:
            if self._currentLevel[tile[0]][tile[1]]['entity'] != 'NONE':
                moves = ['Up', 'Down', 'Left', 'Right']
                bestMoves = {}
                nums = []
                for move in moves:
                    match move:
                        case 'Up':
                            cords = [tile[0], tile[1]-1]
                        case 'Down':
                            cords = [tile[0], tile[1]+1]
                        case 'Left':
                            cords = [tile[0]-1, tile[1]]
                        case 'Right':
                            cords = [tile[0]+1, tile[1]]
                    if not self.isWalkable(cords):
                        moves.remove(move)
                    else:
                        bestMoves[self.distence(cords, [self._playerX, self._playerY])] = move
                        nums.append(self.distence(cords, [self._playerX, self._playerY]))
                bestMoves[self.distence([tile[0], tile[1]], [self._playerX, self._playerY])] = 'NONE'
                nums.append(self.distence([tile[0], tile[1]], [self._playerX, self._playerY]))

        
    #checks if move is possible, and then moves
    def move(self, direction = 'Up', wait = True):
        cords = [False]
        match direction:
            case 'Up':
                cords = [self._playerX, self._playerY-1]
                self._facing = 'U'
            case 'Down':
                cords = [self._playerX, self._playerY+1]
                self._facing = 'D'
            case 'Left':
                cords = [self._playerX -1, self._playerY]
                self._facingDirectionTexture = 'L'
                self._facing = 'L'
            case 'Right':
                cords = [self._playerX +1, self._playerY]
                self._facingDirectionTexture = 'R'
                self._facing = 'R'
        if cords != [False]:
            if self.isWalkable(cords):
                self._playerX, self._playerY = cords
                if wait:
                    time.sleep(1)
            self.rendering()

            

        

    def wait(self):
        pass

    def switchInventory(self, slot1, slot2):
        pass

    def inInventory(self):
        pass

    def useItem(self,slot):
        pass

