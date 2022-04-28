import json
import os
import string
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

maxTypes = 9
chanceEnemyAir = 5
chanceLootAir = 3
chanceEnemySpawn = 40
chanceLootSpawn = 40
pixelOffset = 18
pixelSize = 32
darkness1 = 0.5
darkness2 = 0.2

colors =['white','black','green', 'blue', 'pink', 'red', 'brown', 'orange', 'white', 'purple']
class System:

    _sightFurthest = []
    _viewDistance = 2
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
    window = tkinter.Tk()
    window.configure(bg='black')
    _blackImage=[ImageTk.PhotoImage(Image.open("sprites/black.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/black.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/black.png").convert('RGB')).enhance(darkness2))]
    _exitImage=[ImageTk.PhotoImage(Image.open("sprites/exit.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/exit.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/exit.png").convert('RGB')).enhance(darkness2))]
    _floorImage=[ImageTk.PhotoImage(Image.open("sprites/floor.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/floor.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/floor.png").convert('RGB')).enhance(darkness2))]
    _signImage=[ImageTk.PhotoImage(Image.open("sprites/sign.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/sign.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/sign.png").convert('RGB')).enhance(darkness2))]
    _wallImage=[ImageTk.PhotoImage(Image.open("sprites/wall.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/wall.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/wall.png").convert('RGB')).enhance(darkness2))]
    _playerLImage=[ImageTk.PhotoImage(Image.open("sprites/player left.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/player left.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/player left.png").convert('RGB')).enhance(darkness2))]
    _playerRImage=[ImageTk.PhotoImage(Image.open("sprites/player right.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/player right.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/player right.png").convert('RGB')).enhance(darkness2))]
    _npcImage=[ImageTk.PhotoImage(Image.open("sprites/npc.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/npc.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/npc.png").convert('RGB')).enhance(darkness2))]
    _enemyImage=[ImageTk.PhotoImage(Image.open("sprites/enemy.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/enemy.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/enemy.png").convert('RGB')).enhance(darkness2))]
    _lootImage=[ImageTk.PhotoImage(Image.open("sprites/loot.png")),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/loot.png").convert('RGB')).enhance(darkness1)),ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open("sprites/loot.png").convert('RGB')).enhance(darkness2))]
    _buttonsList = []
    #melee, throwables, magic
    _enemies = {'Rat': {'resistance': [0,0,0]}, 'Ghost': {'resistance': [2,0,0]}, 'Crab': {'resistance': [0,1,0]}, 'Goblin': {'resistance': [0,0,2]}}
    _loot = {'wooden sword': {'amount' : 1}, 'stone sword': {'amount' : 1}, 'iron sword': {'amount' : 1}, 'coin': {'amount' : [1,64]}, 'instant death': {'amount':1}, 'kings sword' : {'amount':1}, 'midas sword' : {'amount':1}, 'lego brick' : {'amount':[1,64]}}
    _itemRarety = {'common': ['wooden sword', 'coin'], 'uncommon': ['stone sword'], 'rare': ['iron sword'], 'epic': ['kings sword', 'lego brick'], 'legendary': ['midas sword'], 'impossible': ['instant death']}
    _items = {'wooden sword': {'strength' : 0}, 'stone sword': {'strength' : 11}, 'iron sword': {'strength' : 13}, 'coin': {'strength' : 0}, 'instant death': {'strength':0}, 'kings sword' : {'strength':15}, 'midas sword' : {'strength':16}, 'lego brick' : {'strength':0}}
    _rarityChance= {'common': 100, 'uncommon': 55, 'rare': 30, 'epic': 15, 'legendary': 5, 'impossible': 1}
    _npcText = ['YEET']

    _signText = ['I am a sign']
    if os.path.exists(f'gameData.json'):
        with open(f'gameData.json') as json_file:
            dataString = json.load(json_file)
            if type(dataString) != dict:
                data = json.loads(dataString)
            else:
                data= dataString
    else:
        data = {'Rat':{'ShowOutsideAs': 'floor', 'Image': 'enemy', 'isEnemy': True, 'isInteractable': False}, 'Exit':{'ShowOutsideAs': 'floor', 'Image': 'exit', 'isEnemy': False, 'isInteractable': False}, 'floor':{'ShowOutsideAs': 'floor', 'Image': 'floor', 'isEnemy': False, 'isInteractable': False}, 'sign':{'ShowOutsideAs': 'floor', 'Image': 'sign', 'isEnemy': False, 'isInteractable': True}, 'wall':{'ShowOutsideAs': 'wall', 'Image': 'wall', 'isEnemy': False, 'isInteractable': False}, 'npc':{'ShowOutsideAs': 'floor', 'Image': 'npc', 'isEnemy': False, 'isInteractable': True}, 'loot':{'ShowOutsideAs': 'floor', 'Image': 'loot', 'isEnemy': False, 'isInteractable': True}}
        json_string = json.dumps(data)
        with open(f'gameData.json', 'w') as outfile:
            json.dump(json_string, outfile)


    def __init__(self, seed : int = 0, startingDifficulty : int = 3):
        
        self._dungeonLevel = 0
        random.seed(seed)
        self.configSettings = accounts_omac.configFileTkinter()
        self.data = accounts_omac.defaultConfigurations.defaultLoadingTkinter(self.configSettings)
        random.randint(1,10)
        self._nextStates = []
        self.newState()
        self.newState()
        self.checkStates()
        self._enemyLevel = startingDifficulty
        self._createdBefore = False
        self._playerX = 0
        self._playerY = 0
        self._facingDirection = 'R'
        self._facing = 'R'
        

        if self.data == False:
            exit()

    def newState(self, modifier = 0):
        for x in range(random.randint(1,10)+ modifier):
            random.randint(1,10)
        self._nextStates.append(random.getstate())
        for x in range(random.randint(1,10)+ modifier):
            random.randint(1,10)

    def checkStates(self):
        x = 0
        while len(self._nextStates) > 2:
            self.newState()
        while self._nextStates[0] == self._nextStates[1]:
            x += 1
            self._nextStates.pop(0)
            self.newState(x)

    def loadState(self):
        random.setstate(self._nextStates[0])
        self._nextStates.pop(0)
        self.checkStates()

    def change(self,location, chosenLevel):
        x, y = location
        self._defaultlevels[chosenLevel][x][y]+= 1
        if self._defaultlevels[chosenLevel][x][y] > maxTypes:
            self._defaultlevels[chosenLevel][x][y] = 0
        self._buttonsList[x][y].configure(text=self._defaultlevels[chosenLevel][x][y], bg = colors[self._defaultlevels[chosenLevel][x][y]])

    def itemRarity(self, modifier : int = 0):
        randomNumber = random.randint(0,100)
        randomNumber -= modifier
        rarity = 'NONE'
        if randomNumber <= self._rarityChance['common']:
            rarity = 'common'
            if randomNumber <= self._rarityChance['uncommon']:
                rarity = 'uncommon'
                if randomNumber <= self._rarityChance['rare']:
                    rarity = 'rare'
                    if randomNumber <= self._rarityChance['epic']:
                        rarity = 'epic'
                        if randomNumber <= self._rarityChance['legendary']:
                            rarity = 'legendary'
                            if randomNumber <= self._rarityChance['impossible']:
                                rarity = 'impossible'
        return rarity

    def getLoot(self, modifier: int = 0):
        itemType = self.itemRarity(modifier)
        item = self._itemRarety[itemType][random.randint(0,len(self._itemRarety[itemType])-1)]
        amount = self._loot[item]['amount']
        if type(amount) == list:
            amount = random.randint(amount[0], amount[1])
        loot = {'type':item, 'amount':amount}
        return loot

    def readTile(self, tile, x, y, extra = 'NONE'):
        if tile == 0:
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= chanceEnemyAir:
                entityLoot = self.getLoot()
                entity = {'type': random.choice(list(self._enemies)), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
            if random.randint(1,100) <= chanceLootAir:
                loot = self.getLoot()
            self._currentLevel[x][y] = {'tile': 'air', 'entity': entity, 'loot': loot} 
        elif tile == 1:
            self._currentLevel[x][y] = {'tile': 'wall', 'entity': 'NONE', 'loot': 'NONE'} 
        elif tile == 2:
            self._currentLevel[x][y] = {'tile': 'air', 'entity': 'NONE', 'loot': 'NONE'} 
            self._playerX = x
            self._playerY = y
        elif tile == 3:
            self._currentLevel[x][y] = {'tile': 'exit', 'entity': 'NONE', 'loot': 'NONE'} 
        elif tile == 4:
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= chanceLootSpawn:
                loot = self.getLoot()
            self._currentLevel[x][y] = {'tile': 'air', 'entity': entity, 'loot': loot}  
        elif tile == 5:
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= chanceEnemySpawn:
                entityLoot = self.getLoot()
                entity = {'type': random.choice(list(self._enemies)), 'level': random.randint(-1,1)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
            self._currentLevel[x][y] = {'tile': 'air', 'entity': entity, 'loot': loot} 
        elif tile == 6:
            if extra != 'NONE':
                text = extra
            else:
                text = self._signText[random.randint(0,len(self._signText)-1)]
            self._currentLevel[x][y] = {'tile': 'sign', 'entity': 'NONE', 'loot': 'NONE', 'text': text} 
        elif tile == 7:
            if extra != 'NONE':
                text = extra
            else:
                text = self._npcText[random.randint(0,len(self._npcText)-1)]
            self._currentLevel[x][y] = {'tile': 'npc', 'entity': 'NONE', 'loot': 'NONE', 'text': text} 
        elif tile == 8:
            self._currentLevel[x][y] = {'tile': 'air', 'entity': 'NONE', 'loot': 'NONE'}
        elif tile == 9:
            entity = 'NONE'
            loot = self.getLoot()
            entityLoot = self.getLoot(10)
            entity = {'type': random.choice(list(self._enemies)), 'level': random.randint(1,4)+ self._enemyLevel + self._dungeonLevel, 'item': entityLoot}
            self._currentLevel[x][y] = {'tile': 'air', 'entity': entity, 'loot': loot}  


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
                        num = 0
                    else:
                        num = 1
                else:
                    num = 2
                if x==self._playerX and y == self._playerY:
                        if self._facingDirection == 'R':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._playerRImage[num])
                        else:
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._playerLImage[num])
                else:
                    notfound = False
                    if num == 2:
                        if self._currentLevel[x][y]['entity'] != 'NONE':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._floorImage[num])
                        elif self._currentLevel[x][y]['loot'] != 'NONE':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._floorImage[num])
                        elif self._currentLevel[x][y]['tile'] == 'sign':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._floorImage[num])
                        elif self._currentLevel[x][y]['tile'] == 'npc':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._floorImage[num])
                        elif self._currentLevel[x][y]['tile'] == 'exit':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._floorImage[num])
                        else:
                            notfound = True
                    else:
                        if self._currentLevel[x][y]['entity'] != 'NONE':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._enemyImage[num])
                        elif self._currentLevel[x][y]['loot'] != 'NONE':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._lootImage[num])
                        elif self._currentLevel[x][y]['tile'] == 'sign':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._signImage[num])
                        elif self._currentLevel[x][y]['tile'] == 'npc':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._npcImage[num])
                        elif self._currentLevel[x][y]['tile'] == 'exit':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._exitImage[num])
                        else:
                            notfound = True
                    if notfound:
                        if self._currentLevel[x][y]['tile'] == 'air':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._floorImage[num])
                        elif self._currentLevel[x][y]['tile'] == 'wall':
                            self._canvas.create_image(x*pixelSize+pixelOffset,y*pixelSize+pixelOffset, image=self._wallImage[num])



    def createWindow(self):
        self._canvas = tkinter.Canvas(self.window, bg="black", height=len(self._currentLevel[0])*32, width=len(self._currentLevel)*32)
        self._canvas.pack()
        

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
                    self._buttonsList[x].append(tkinter.Button(self.window, text=self._defaultlevels[chosenLevel][x][y],bg = colors[self._defaultlevels[chosenLevel][x][y]], command=lambda cords=cords:self.change(cords, chosenLevel)))
                    self._buttonsList[x][y].grid(column=x, row=y)
            tkinter.Button(self.window, text='export',command=lambda: print(self._defaultlevels[chosenLevel])).grid(column=0,row=x+1,columnspan=y+1)
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
        self.data = accounts_omac.saveAccount(self.data, self.configSettings)
        exit()


