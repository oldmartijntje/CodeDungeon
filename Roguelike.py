import datetime
import json
from logging import exception
import os
import time
from tkinter import ttk
import accounts_omac
import random
import tkinter
from PIL import Image, ImageTk, ImageEnhance
import math
import copy
from tkinter.messagebox import showerror



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
    [[0, 0, 0, 0, 1, 6, 4, 1, 4, 7], [0, 1, 1, 5, 1, 0, 5, 1, 0, 0], [5, 1, 3, 0, 1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 5, 0, 0, 1, 0], [0, 0, 4, 1, 4, 0, 1, 5, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0, 6], [4, 1, 0, 0, 5, 0, 0, 1, 0, 1], [4, 1, 1, 1, 1, 1, 0, 1, 0, 0], [0, 1, 3, 0, 1, 4, 0, 1, 1, 5], [2, 1, 1, 0, 0, 0, 1, 3, 0, 0]],
    [[4, 5, 4, 0, 5, 0, 1, 4, 0, 0], [4, 4, 4, 1, 4, 5, 1, 5, 5, 4], [1, 1, 1, 1, 1, 0, 1, 4, 0, 0], [4, 0, 1, 0, 0, 0, 1, 1, 0, 1], [0, 5, 1, 0, 2, 0, 0, 0, 0, 0], [0, 4, 1, 0, 0, 4, 1, 1, 1, 5], [0, 1, 1, 1, 1, 1, 1, 0, 0, 0], [4, 0, 0, 1, 0, 0, 0, 4, 1, 0], [0, 5, 5, 0, 0, 5, 0, 0, 1, 0], [4, 0, 4, 1, 4, 0, 0, 5, 1, 3]],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 0, 0, 0, 0, 1, 4, 0, 1], [1, 1, 0, 1, 1, 0, 0, 0, 0, 1], [1, 6, 0, 4, 1, 0, 1, 5, 4, 1], [1, 4, 0, 0, 1, 5, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 4, 0, 5, 1, 0, 0, 0, 4, 1], [1, 4, 0, 0, 1, 0, 1, 5, 0, 1], [1, 0, 0, 4, 1, 3, 1, 0, 4, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    ]
    
    bugmessage = []
    _buttonsList = []
    #melee, throwables, magic
    _enemies = []
    _loot = []
    _itemRarety = {}
    _items = []
    _rarityChance= {}
    _images = {}

    defaultNPCText = ["I am the great Cackletta's most best pupil, who is named Fawful! I am here, laughing at you! If you are giving us the chase, just to get your silly princess's voice, then you are idiots of foolishness! Princess Peach's sweet voice will soon be the bread that makes the sandwich of Cackletta's desires! And this battle shall be the delicious mustard on that bread! The mustard of your doom!",
      "Fink-rat!", "Have you readiness for this?!?", "Now is when I ram you!", "O Great Cackletta, unleash the voice of Princess Peach on the Beanstar when you are wanting to!", "Now is the time where my true might shines like many angry sunbeams of rage!", "Hah! Now taste the finale, when carelessness opens the door to a comeback not expected by you! Your lives that I spit on are now but a caricature of a cartoon drawn by a kid who is stupid! You shall all fall and vanish with your precious Beanbean Kingdom as I laugh heartily at you!",
      "In the last moments of the finale of the finale, when relief leads to negligence that begets rashness... That is when the comeback that faltered comes back and beats your pathetic comeback that I scoff at!", "O Great Bowletta! The Mario Bros. who I hate are coming this way!", "Yes...Moustache...", "At last, my entrance with drama!","Stop it...such mumbling...", "ONE FELL SWOOP IS HOW I WILL DEAL WITH YOU FINK-RATS!!!",
      "Next it is the turn of you!", "You! You are the fink-rats that came with the Bowser that I hate!", "I HAVE FURY!","Ouch! Hotness! It is the overheat!", "I have boredom...Guests? Now I have... FURY!", "I say to you WELCOME! Welcome to Fawful's Bean 'n' Badge!", "In this place, beans are like precious treasure milked from a famous cow made of jewels!", "All who come with beans leave with badges so rare they make mustaches droop with disbelief!",
      "What? The story of Fawful? Your words are not beans. I am not wanting them.", "You are like brainless cats that are too dumb to know they are stupid! You have curiosity... ...But my tale is long, so long it makes babies old and hairy lips grow grey with aging. Do you dare hear?", "I am here, merchant of badges, only sometimes with fury, but I once had fury at all times.", "I drizzled rage dressing on the country next door. Rage dressing on a salad of evil!",
      "Red and green puts the fog of rage in my eyes, and my mind goes crazy.","P-Please... I will be fine. No worrying for Fawful. We talk of beans.","Beans and badges... We begin trading!","The beans hide in the dirts of this country like dirt-fish who like to eat dirt for dinner. Bean symbols like this are marking all bean spots.","You are digging in dirt, right? You are digging under symbols. And you are finding much bean!","Bean symbols have sneakiness! When the beans are gone, the symbols flee like babies!",
      "You are wanting much beans? Then you are hunting symbols. And digging and popping.","There are even places to win beans in games, maybe...","If you get many beans, you get many badges at this place, Fawful's Bean 'n' Badge!","I HAVE FURY!"]
    
    defaultSignText = ['I am probably older than you are; my friendly traveler reading this.','This text took 49 bytes to store on your computer','I was a tree', 'I was Groot','Don\'t listen to the NPCs, They only speak nonsense','I am empty, wait did i just create a paradox?','Go left and then right','Danger ahead', 'Greetings traveler, be aware of Fawful.']
      

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
        dataDict['preference'] = {'autoEquipBetter': True, 'sleepTime':0.1}
        dataDict['startingLoot'] = {'wooden_sword': {'amount': 1}}
        dataDict['equippedWeapon'] = {'weapon': 'wooden_sword', 'weight': 1}
        dataDict['playerStats'] = {'statsPerLevel':{'HP':10, 'strength':4}, 'beginStats':{'HP':5, 'strength':5}, 'startLevel': 3, 'XPneeded': {'multiplyByLevel':50, 'startingNumber':10}}
        dataDict['dungeon'] = {'startLevel': 3}
        dataDict['balancing'] = {'doStrengthDamage': True, 'strengthDevidedBy': 3, 'killMultiplierXP': 2, 'XPperDamageDevidedBy' : 1, 'entetyLootDroppingChance': 50}
        dataDict['rarities'] = {'common': {'chance': 100},'uncommon': {'chance': 50},'rare': {'chance': 15},'epic': {'chance': 8},'legendary': {'chance': 4},'impossible': {'chance': 1}}
        dataDict['chance'] = {'enemyAir' : 5, 'enemySpawn': 40, 'lootAir' : 3, 'lootSpawn' : 40}
        dataDict['appSettings'] = {'offset': 18,'size': 32, 'maxTypes': 9, 'colors': ['white','black','green', 'blue', 'pink', 'red', 'brown', 'orange', 'white', 'purple']}
        dataDict['playerImages'] = {'L': 'player left', 'R': 'player right'}
        dataDict['debug']= {'logging' : False, 'combat' : True, 'enemyAI' : True, 'sleep': True, 'enemyLoop': 2}
        dataDict['Gamma'] = {'distance': 2, 'darknessFull' : 0.2, 'darknessFade' : 0.5}
        dataDict['text'] = {'signText': defaultSignText, 'npcText': defaultNPCText}

        dataDict['tiles'] = {'rat':{'ShowOutsideAs': 'floor', 'Walkable': False, 'Image': 'rat', 'isEnemy': True, 'isInteractable': False,'isLoot': False, 'doubleAttack': False, 'statsPerLevel': {'HP':5,'ATK':2, 'deathXP' : 5},'lessATKpointsPercentage': 20, 'hitChance': 80, "movementRules": {"attackRule" : "insteadOf", "movement": 1, "attack": 1}}, 'exit':{'ShowOutsideAs': 'floor', 'Walkable': True,'Image': 'exit', 'isEnemy': False, 'isInteractable': False,'isLoot': False}, 'floor':{'ShowOutsideAs': 'floor','Walkable': True, 'Image': 'floor', 'isEnemy': False, 'isInteractable': False,'isLoot': False}, 'sign':{'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'sign', 'isEnemy': False, 'isInteractable': True,'isLoot': False, 'text': 'signText'}, 'wall':{'ShowOutsideAs': 'wall','Walkable': False, 'Image': 'wall', 'isEnemy': False, 'isInteractable': False,'isLoot': False}, 'npc':{'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'npc', 'isEnemy': False, 'isInteractable': True, 'isLoot': False, 'text': 'npcText'}, 'wooden_sword':{'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1}, "isWeapon": True,"isConsumable": False,'rarity': 'NONE', 'weapon': {'minStrenght': 17, 'attack': 8, 'type': 'stab', 'weaponWeight' : 1}}}}
        dataDict['tiles']['stone_sword'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'uncommon', 'weapon': {'minStrenght': 22, 'attack': 10, 'type': 'stab', 'weaponWeight' : 3}}}
        dataDict['tiles']['moldy_bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':3},"isWeapon": False,"isConsumable": True,'rarity': 'common', 'consumable': {'restoreHP': 5, 'restoreHPpercentage': False}}}
        dataDict['tiles']['old_bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':2},"isWeapon": False,"isConsumable": True,'rarity': 'common', 'consumable': {'restoreHP': 10, 'restoreHPpercentage': False}}}
        dataDict['tiles']['bread'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':2},"isWeapon": False,"isConsumable": True,'rarity': 'uncommon', 'consumable': {'restoreHP': 20, 'restoreHPpercentage': False}}}
        dataDict['tiles']['bandaid'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':2},"isWeapon": False,"isConsumable": True,'rarity': 'uncommon', 'consumable': {'restoreHP': 10, 'restoreHPpercentage': True}}}
        dataDict['tiles']['bronze_coin'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':10},"isWeapon": False,"isConsumable": False,'rarity': 'common'}}
        dataDict['tiles']['silver_coin'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':3},"isWeapon": False,"isConsumable": False,'rarity': 'common'}}
        dataDict['tiles']['gold_coin'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':3},"isWeapon": False,"isConsumable": False,'rarity': 'uncommon'}}
        dataDict['tiles']['iron_dagger'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'rare', 'weapon': {'minStrenght': 20, 'attack': 10, 'type': 'stab', 'weaponWeight' : 4}}}
        dataDict['tiles']['battle_axe'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'epic', 'weapon': {'minStrenght': 40, 'attack': 20, 'type': 'stab', 'weaponWeight' : 6}}}
        dataDict['tiles']['butterfly_knife'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": True,"isConsumable": False,'rarity': 'legendary', 'weapon': {'minStrenght': 30, 'attack': 5, 'type': 'slice', 'weaponWeight' : 5}}}
        dataDict['tiles']['floor_dice'] = {'ShowOutsideAs': 'floor','Walkable': False, 'Image': 'loot', 'isEnemy': False, 'isInteractable': False,'isLoot': True, 'loot': {'amount' : {'min':1, 'max':1},"isWeapon": False,"isConsumable": False,'rarity': 'legendary', 'special': {'nextFloor': True}}}
    
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
        doLogging = dataDict['debug']['logging']
        doCombat = dataDict['debug']['combat']
        doEnemyMovement = dataDict['debug']['enemyAI']
        _enemyLevel = dataDict['dungeon']['startLevel']
        defaultPlayerStats = dataDict['playerStats']
        autoEquip = dataDict['preference']['autoEquipBetter']
        hasWeaponWeight = dataDict['equippedWeapon']['weight']
        equipped = dataDict['equippedWeapon']['weapon']
    except Exception as e:
        print(e)
        print('something is wrong with the gameData/gameData.json, delete it or fix it.')
        bugmessage.append([e,'something is wrong with the gameData/gameData.json, delete it or fix it.'])

    if doLogging:
        #logging
        now = datetime.datetime.now()
        dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
        try:
            os.mkdir('logs/')
        except:
            pass
        log = open(f'logs/log{dt_string}.txt', "w")
        log.close()  
    
    


    def __init__(self, seed : int = 0):
        
        self._dungeonLevel = 0
        random.seed(seed)
        self.logging(seed,'seed')
        self.accountConfigSettings = accounts_omac.configFileTkinter()
        self.accountDataDict = accounts_omac.defaultConfigurations.defaultLoadingTkinter(self.accountConfigSettings)
        random.randint(1,10)
        self._nextStates = []
        self.newState()
        self.newState()
        self.checkStates()
        self._createdBefore = False
        self._playerX = 0
        self._playerY = 0
        self._facingDirectionTexture = 'R'
        self._facing = 'R'
        self.gameWindow = tkinter.Tk()
        self.gameWindow.configure(bg='black')
        self.gameWindow.attributes('-topmost', True)
        self.inventory = self.dataDict['startingLoot']
        self.gameWindow.protocol("WM_DELETE_WINDOW", self.exit)
        
        

        self.rarityList = []
        for rar in self.dataDict['rarities'].keys():
            self.rarityList.append(rar)

        #if no account has been logged into
        if self.accountDataDict == False:
            exit()

        if len(self.bugmessage) > 0:
            for x in range(len(self.bugmessage)):
                self.logging(self.bugmessage[x], 'function = __init__')

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
                if self.dataDict['tiles'][data]['loot']['rarity'] != 'NONE':
                    self._itemRarety[self.dataDict['tiles'][data]['loot']['rarity']].append(data)
                    self._items.append(data)
            self._images[f'darknessFull-{self.dataDict["tiles"][data]["Image"]}'.lower()] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png".lower()).convert('RGB')).enhance(self.darknessFull))
            self._images[f'darknessFade-{self.dataDict["tiles"][data]["Image"]}'.lower()] = ImageTk.PhotoImage(ImageEnhance.Brightness(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png".lower()).convert('RGB')).enhance(self.darknessFade))
            self._images[f'normal-{self.dataDict["tiles"][data]["Image"]}'.lower()] = ImageTk.PhotoImage(Image.open(f"sprites/{self.dataDict['tiles'][data]['Image']}.png".lower()))
    
    #for when something is missign from the json
    def jsonError(self,error):
        self.displayText(f'{error}\nsomething is wrong with the gameData/gameData.json, delete it or fix it.')
        self.logging([error,'something is wrong with the gameData/gameData.json, delete it or fix it.'])

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
        while len(self._nextStates) < 2:
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
    def getLoot(self, modifier: int = 0, chanceOfNothing: int = 100):
        if random.randint(1,99) < chanceOfNothing:
            while True:
                itemType = self.itemRarity(modifier)
                if len(self._itemRarety[itemType]) != 0:
                    break
            item = self._itemRarety[itemType][random.randint(0,len(self._itemRarety[itemType])-1)]
            amount = random.randint(self.dataDict['tiles'][item]['loot']['amount']['min'], self.dataDict['tiles'][item]['loot']['amount']['max'])
            if type(amount) == list:
                amount = random.randint(amount[0], amount[1])
            loot = {'type':item, 'amount':amount}
            return loot
        else:
            return 'NONE'

    #read tile of 2D erray and convert into map
    def readTile(self, tile, x, y, extra = 'NONE'):
        #all numbers are different type of tile:
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
        if tile == 0:
            entity = 'NONE'
            loot = 'NONE'
            if random.randint(1,100) <= self.chanceEnemyAir:
                entityLoot = self.getLoot(0, self.dataDict['balancing']['entetyLootDroppingChance'])
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
                entityLoot = self.getLoot(0, self.dataDict['balancing']['entetyLootDroppingChance'])
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
            #if there is an enemy, it should display enemy instead
            display = self._currentLevel[x][y]['entity']['type']
        elif self._currentLevel[x][y]['loot']!= 'NONE':
            #if there is loot, it should display loot instead
            display = self._currentLevel[x][y]['loot']['type']
        else:
            #else display the tile
            display = self._currentLevel[x][y]['tile']
        self._currentLevel[x][y]['display'] = display

    #create a level off a 2D erray
    def createLevel(self, levelDefault):
        level = copy.deepcopy(levelDefault)
        #if there isn't an entrance declared, generate random entrance
        if not any(2 in sublist for sublist in level):
            self.logging('entrance needed')
            while not any(2 in sublist for sublist in level) and (any(0 in sublist for sublist in level) or any(8 in sublist for sublist in level)):
                tryLine = random.randint(0,len(level)-1)
                if 0 in level[tryLine] or 8 in level[tryLine]:
                    whereAir = [i for i, x in enumerate(level[tryLine]) if x == 0]
                    whereNonAir = [i for i, x in enumerate(level[tryLine]) if x == 8]
                    spawnable = whereAir + whereNonAir
                    level[tryLine][spawnable[random.randint(0,len(spawnable)-1)]] = 2
        #if there isn't an exit declared, and not a bossfight, generate random exit
        if not any(3 in sublist for sublist in level) and not any(9 in sublist for sublist in level):
            self.logging('exit needed')
            while not any(3 in sublist for sublist in level) and (any(0 in sublist for sublist in level) or any(8 in sublist for sublist in level)):
                tryLine = random.randint(0,len(level)-1)
                if 0 in level[tryLine]or 8 in level[tryLine]:
                    whereAir = [i for i, x in enumerate(level[tryLine]) if x == 0]
                    whereNonAir = [i for i, x in enumerate(level[tryLine]) if x == 8]
                    spawnable = whereAir + whereNonAir
                    level[tryLine][spawnable[random.randint(0,len(spawnable)-1)]] = 3
        #make 2D erray
        self._currentLevel = []
        for x in range(len(level)):
            self._currentLevel.append([])
            for y in range(len(level[x])):
                self._currentLevel[x].append({})
                if type(level[x][y]) == list:
                    #read the tile(with extra argument, for given text to signs and npc)
                    self.readTile(level[x][y][0], x, y, level[x][y][1])
                else:
                    #read the tile(with extra argument
                    self.readTile(level[x][y], x, y)
        self.levelSize = [len(self._currentLevel), len(self._currentLevel[0])]

    #render how the dungeon looks like
    def rendering(self):
        self._canvas.delete("all")
        #make the furthest visability square (the transition)
        self._sightFurthest = [] 
        for ix in range(self._viewDistance * 2 + 1):
            for iy in range(self._viewDistance * 2 + 1):
                #add it to a list, so it remembers to shade it later
                #the math to calculate how far sight is
                self._sightFurthest.append(f'{ix + self._playerX - self._viewDistance}-{iy + self._playerY - self._viewDistance}')
        #make the normal visability square
        self._sight = [] 
        for ix in range(self._viewDistance * 2 +1 - (math.ceil(self._viewDistance/2)*2)):
            for iy in range(self._viewDistance * 2 + 1 - (math.ceil(self._viewDistance/2)*2)):
                #add it to a list, so it remembers to keep original texture
                #the math to calculate how far sight is
                self._sight.append(f'{ix + self._playerX - self._viewDistance+math.ceil(self._viewDistance/2)}-{iy + self._playerY - self._viewDistance+math.ceil(self._viewDistance/2)}')
        
        #for all tiles, display them
        for x in range(len(self._currentLevel)):
            for y in range(len(self._currentLevel[x])):
                if f"{x}-{y}" in self._sightFurthest:
                    #lookup what type of shading it needs
                    if f"{x}-{y}" in self._sight:
                        picType = 'normal-'.lower()
                    else:
                        picType = 'darknessFade-'.lower()
                else:
                    picType = 'darknessFull-'.lower()
                
                #display the tile
                if x==self._playerX and y == self._playerY:
                    self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['playerImages'][self._facingDirectionTexture.upper()]}"])
                else:
                    if picType == 'darknessFull-'.lower():
                        self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['tiles'][self._currentLevel[x][y]['display']]['ShowOutsideAs']}"])
                    else:
                        self._canvas.create_image(x*self.pixelSize+self.pixelOffset,y*self.pixelSize+self.pixelOffset, image=self._images[f"{picType}{self.dataDict['tiles'][self._currentLevel[x][y]['display']]['Image']}"])
        #for if stats changed, update those
        self.updateStats()
        #updae the window, so that it shows the new generated canvas
        self.gameWindow.update_idletasks()      
        self.gameWindow.update()

    #create the window
    def createCanvas(self):
        self._canvas = tkinter.Canvas(self.gameWindow, bg="black", height=len(self._currentLevel[0])*32, width=len(self._currentLevel)*32)
        self._canvas.grid(row=0,column=0)
        
    #for the stats like hp    
    def createStats(self):
        self._hpTextvar = tkinter.StringVar()
        self._hpTextvar.set(f'HP:')
        self._xpVar = tkinter.StringVar()
        self._xpVar.set(f'XP:')
        self._strengthVar = tkinter.StringVar()
        self._strengthVar.set(f'Strength:')
        self._levelVar = tkinter.StringVar()
        self._levelVar.set(f'Level:')
        self._hpLabel = ttk.Label(self.gameWindow, textvariable=self._hpTextvar)
        self._hpLabel.grid(row=1,column=0, sticky="EW")
        self._strengthLabel = ttk.Label(self.gameWindow, textvariable=self._strengthVar)
        self._strengthLabel.grid(row=2,column=0, sticky="EW")
        self._xpLabel = ttk.Label(self.gameWindow, textvariable=self._xpVar)
        self._xpLabel.grid(row=3,column=0, sticky="EW")
        self._levelLabel = ttk.Label(self.gameWindow, textvariable=self._levelVar)
        self._levelLabel.grid(row=4,column=0, sticky="EW")

    def updateStats(self):
        if self.playerStats["HP"]["current"] <= 0:
            showerror(title='Error',message='You died!')
            self.exit()
        while True:
            xpNeeded = self.defaultPlayerStats["XPneeded"]["multiplyByLevel"] * self.playerStats['level'] + self.defaultPlayerStats["XPneeded"]["startingNumber"]
            if self.playerStats['XP'] > xpNeeded:
                self.playerStats['XP'] -= xpNeeded
                self.playerStats['level'] += 1
                self.displayText(f'You levelled up to level {self.playerStats["level"]}!')
                self.playerStats["strength"] += self.defaultPlayerStats['statsPerLevel']['strength']
                self.playerStats["HP"]["current"] += self.defaultPlayerStats['statsPerLevel']['HP']
                self.playerStats["HP"]["max"] += self.defaultPlayerStats['statsPerLevel']['HP']
            else:
                break
        self._xpVar.set(f'XP: {self.playerStats["XP"]} / {xpNeeded}')
        self._hpTextvar.set(f'HP: {self.playerStats["HP"]["current"]} / {self.playerStats["HP"]["max"]}')
        self._levelVar.set(f'Level: {self.playerStats["level"]}')
        self._strengthVar.set(f'Strength: {self.playerStats["strength"]}')

    #startup the program
    def startGame(self, mode = 'Play', chosenLevel = 0):
        
        custom = False
        #look what mode
        if str(mode).lower() not in ['play', 'create']:
            chosenLevel = mode
            mode = 'Play'
        #look for given level
        if type(chosenLevel) == list:
            self._defaultlevels[0] = list(chosenLevel)
            chosenLevel = 0
            custom = True
        #look for 10x10 format to generate that size level
        if type(chosenLevel) == str:
            if 'x' in str(chosenLevel):
                #split it at the x, so it can read the margins
                if chosenLevel.split('x')[0].isdigit() and chosenLevel.split('x')[1].isdigit():
                    level = []
                    #generate the 2D erray of the level
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
                    #make level 0 the given level
                    self._defaultlevels[0] = level
                    #force it to play level 0
                    chosenLevel = 0
                    custom = True
        #if not given a number, it will force to play 0
        if not str(chosenLevel).isdigit():
            chosenLevel = 0
        if mode.lower() == 'create':
            #if using level editor  
            self._buttonsList = []
            #make 2D erray
            for x in range(len(self._defaultlevels[chosenLevel])):
                self._buttonsList.append([])
            #create a lot of buttons
            for x in range(len(self._defaultlevels[chosenLevel])):
                for y in range(len(self._defaultlevels[chosenLevel][x])):
                    cords = [x,y]
                    self._buttonsList[x].append(tkinter.Button(self.gameWindow, text=self._defaultlevels[chosenLevel][x][y],bg = self.colors[self._defaultlevels[chosenLevel][x][y]], command=lambda cords=cords:self.changeEditorButton(cords, chosenLevel)))
                    self._buttonsList[x][y].grid(column=x, row=y)
            tkinter.Button(self.gameWindow, text='export',command=lambda: print(self._defaultlevels[chosenLevel])).grid(column=0,row=x+1,columnspan=y+1)
        #if play mode
        if mode.lower() == 'play':
            #generate player
            hp = (self.defaultPlayerStats["statsPerLevel"]["HP"] * self.defaultPlayerStats["startLevel"]) + self.defaultPlayerStats["beginStats"]["HP"]
            strength = (self.defaultPlayerStats["statsPerLevel"]["strength"] * self.defaultPlayerStats["startLevel"]) + self.defaultPlayerStats["beginStats"]["strength"]
            self.playerStats = {'HP': {'max': hp, 'current': hp}, 'level' : self.defaultPlayerStats["startLevel"], 'XP': 0, 'strength': strength}



            #generate starting level
            self.checkStates()
            if custom == False:
                levelNumber = random.randint(0,len(self._defaultlevels)-1)
            else:
                levelNumber = chosenLevel
            print(levelNumber)
            self.createLevel(self._defaultlevels[levelNumber])
            self.createStats()
            self.createCanvas()
            self.rendering()
        

    def exit(self):
        accounts_omac.saveAccount(self.accountDataDict, self.accountConfigSettings)
        exit()

    #check if tile is being able to be walked
    def isWalkable(self, cordinates = [0,0], human = False):
        x,y = cordinates
        if x < 0 or y < 0 or y > self.levelSize[1]-1 or x > self.levelSize[0]-1:
            return False
        if x == self._playerX and y == self._playerY:
            return False
        if not human:
            if self._currentLevel[x][y]['display'] == 'exit':
                return False
        return self.dataDict['tiles'][self._currentLevel[x][y]['display']]['Walkable']

    #calculate distance between 2 cordinates
    def distence(self, cord1, cord2):
        #a^2 + b^2 == c^2
        x1,y1 =cord1
        x2,y2 =cord2
        xDis = abs(x1-x2)
        yDis = abs(y1-y2)
        distance = math.sqrt((xDis **2) + (yDis **2))
        return distance

    #check if enemy's want to move
    def enemyTurn(self):
        if self.doEnemyMovement != False:
            self.EnemyMoveRadius = [] 
            for ix in range((self._viewDistance+1) * 2 + 1):
                for iy in range((self._viewDistance+1) * 2 + 1):
                    self.EnemyMoveRadius.append([ix + self._playerX - self._viewDistance,iy + self._playerY - self._viewDistance])
            for tile in self.EnemyMoveRadius:
                
                if tile[0] < 0 or tile[1] < 0 or tile[0] > len(self._currentLevel)-1 or tile[1] > len(self._currentLevel[tile[0]])-1:
                    pass
                elif tile in self.ignore:
                    pass
                else:
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
                                pass
                            else:
                                if self.distence(cords, [self._playerX, self._playerY]) > self.distence([tile[0], tile[1]], [self._playerX, self._playerY]):
                                    if bool(random.getrandbits(1)):
                                        moveTheEnemy = True
                                    else:
                                        self.ignore.append([tile[0],tile[1]])
                                        moveTheEnemy = False
                                else:
                                    moveTheEnemy = True
                                if moveTheEnemy:
                                    if self.distence(cords, [self._playerX, self._playerY]) in bestMoves:
                                        bestMoves[self.distence(cords, [self._playerX, self._playerY])].append([move, cords, [tile[0], tile[1]]])
                                    else:
                                        bestMoves[self.distence(cords, [self._playerX, self._playerY])] = [[move, cords, [tile[0], tile[1]]]]
                                        nums.append(self.distence(cords, [self._playerX, self._playerY]))

                        #start picking a move
                        if len(bestMoves) != 0:
                            nums.sort()
                            if self.distence([tile[0], tile[1]], [self._playerX, self._playerY]) > 1.0:
                                if len(bestMoves[nums[0]]) > 1:
                                    self.moveEnemy(bestMoves[nums[0]][random.randint(0,len(bestMoves[nums[0]])-1)])
                                else:
                                    self.moveEnemy(bestMoves[nums[0]][0])

                            else:
                                ATK = self._currentLevel[tile[0]][tile[1]]['entity']['level'] * self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]['statsPerLevel']['ATK']
                                if self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]['hitChance'] > random.randint(1,99):
                                    ATK -= ATK // 100 * random.randint(0, self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]['lessATKpointsPercentage'])
                                    self.playerStats["HP"]["current"] -= ATK
                                    self.displayText(f"{self._currentLevel[tile[0]][tile[1]]['entity']['type']} hit you, You took {ATK}HP damage")
                                    if self.dataDict['tiles'][self._currentLevel[tile[0]][tile[1]]['entity']['type']]['doubleAttack'] == False:
                                        self.ignore.append([tile[0],tile[1]])



                            #delay of enemy movement
                            try:
                                if self.dataDict['debug']['sleep']:
                                    time.sleep(self.dataDict['preference']['sleepTime'])
                            except Exception as e:
                                self.jsonError(e)
                            self.rendering()






    def moveEnemy(self, moveData):
        move, NewXY, XY = moveData
        newX,newY = NewXY
        x,y = XY

        types = ['display', 'entity']
        for each in types:
            switch = []
            switch.append(self._currentLevel[x][y][each])
            switch.append(self._currentLevel[newX][newY][each])
            self._currentLevel[x][y][each] = switch[1]
            self._currentLevel[newX][newY][each] = switch[0]
            self.ignore.append([newX,newY])

    def damageMessage(self, cords, damage):
        if self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] > 0:
            self.displayText(f"You dealt {damage}HP damage to {self._currentLevel[cords[0]][cords[1]]['entity']['type']}, he has {self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current']}HP left")
            self.playerStats['XP'] += damage // self.dataDict['balancing']['XPperDamageDevidedBy']
        else:
            self.displayText(f"You dealt {damage}HP damage to {self._currentLevel[cords[0]][cords[1]]['entity']['type']}, he is ded")
            self.playerStats['XP'] += damage * self.dataDict['balancing']['killMultiplierXP'] // self.dataDict['balancing']['XPperDamageDevidedBy']
            self.playerStats['XP'] += self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['entity']['type']]['statsPerLevel']['deathXP'] * self._currentLevel[cords[0]][cords[1]]['entity']['level']


    def sliceEnemy(self, cords, damage):
        try:
            if self._currentLevel[cords[0]][cords[1]]['entity'] != 'NONE':
                if 'HP' not in self._currentLevel[cords[0]][cords[1]]['entity']:
                    hp = self._currentLevel[cords[0]][cords[1]]['entity']['level'] * self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['entity']['type']]['statsPerLevel']['HP']
                    self._currentLevel[cords[0]][cords[1]]['entity']['HP'] = {'Max': hp, 'current': hp + random.randint(-1,1)}
                self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] -= damage
                self.damageMessage(cords, damage)
        except IndexError:
            pass
        except Exception as e:
            self.logging(e, f'cords: {cords}', f'damage: {damage}', 'Function = sliceEnemy()')
            

    #interact with something
    def interact(self):
        
        match self._facing:
            case 'U':
                cords = [self._playerX, self._playerY-1]
            case 'D':
                cords = [self._playerX, self._playerY+1]
            case 'L':
                cords = [self._playerX -1, self._playerY]
            case 'R':
                cords = [self._playerX +1, self._playerY]
        
        if self._currentLevel[cords[0]][cords[1]]['loot'] != 'NONE':
            #if there is loot
            #{'type': 'Stone sword', 'amount': 1}
            self.displayText(f"You picked up {self._currentLevel[cords[0]][cords[1]]['loot']['amount']} X {self._currentLevel[cords[0]][cords[1]]['loot']['type']}")
            if self._currentLevel[cords[0]][cords[1]]['loot']['type'] in self.inventory:

                self.inventory[self._currentLevel[cords[0]][cords[1]]['loot']['type']]['amount'] += self._currentLevel[cords[0]][cords[1]]['loot']['amount']
            else:
                self.inventory[self._currentLevel[cords[0]][cords[1]]['loot']['type']] = {'amount':self._currentLevel[cords[0]][cords[1]]['loot']['amount']}
                
            if self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['loot']['type']]["loot"]['isWeapon'] == True:
                if self.autoEquip == True and self.hasWeaponWeight < self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['loot']['type']]["loot"]['weapon']['weaponWeight'] and self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['loot']['type']]["loot"]['weapon']['minStrenght'] <= self.playerStats['strength']:
                    self.equipped = self._currentLevel[cords[0]][cords[1]]['loot']['type']
                    self.hasWeaponWeight = self.dataDict['tiles'][self.equipped]["loot"]['weapon']['weaponWeight']
                    self.displayText(f"You equipped {self._currentLevel[cords[0]][cords[1]]['loot']['type']}")
            
            self._currentLevel[cords[0]][cords[1]]['loot']= 'NONE'
            self._currentLevel[cords[0]][cords[1]]['display']= 'floor'
            self.rendering()
        elif 'text' in self._currentLevel[cords[0]][cords[1]]:
            self.displayText(f"{self._currentLevel[cords[0]][cords[1]]['display']}: {self._currentLevel[cords[0]][cords[1]]['text']}")
        elif self._currentLevel[cords[0]][cords[1]]['entity'] != 'NONE':
            if 'HP' not in self._currentLevel[cords[0]][cords[1]]['entity']:
                hp = self._currentLevel[cords[0]][cords[1]]['entity']['level'] * self.dataDict['tiles'][self._currentLevel[cords[0]][cords[1]]['entity']['type']]['statsPerLevel']['HP']
                self._currentLevel[cords[0]][cords[1]]['entity']['HP'] = {'Max': hp, 'current': hp + random.randint(-1,1)}
            
            damage = self.dataDict['tiles'][self.equipped]["loot"]['weapon']['attack']
            if self.dataDict['balancing']['doStrengthDamage']:
                damage += self.playerStats['strength'] // self.dataDict['balancing']['strengthDevidedBy']
            if self.dataDict['tiles'][self.equipped]["loot"]['weapon']['minStrenght'] > self.playerStats['strength']:
                damage = random.randint(1,damage)
            if self.dataDict['tiles'][self.equipped]["loot"]['weapon']['type'] == 'stab':
                if self.dataDict['tiles'][self.equipped]["loot"]['weapon']['minStrenght'] <= self.playerStats['strength'] or bool(random.getrandbits(1)):
                    self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] -= damage
                    self.damageMessage(cords, damage)
                else:
                    self.displayText(f"You missed, The strength you need to use this weapon is {self.dataDict['tiles'][self.equipped]['loot']['weapon']['minStrenght']}")
            elif self.dataDict['tiles'][self.equipped]["loot"]['weapon']['type'] == 'slice':
                if self.dataDict['tiles'][self.equipped]["loot"]['weapon']['minStrenght'] <= self.playerStats['strength'] or bool(random.getrandbits(1)):
                    self.sliceEnemy([self._playerX, self._playerY-1],damage)
                    self.sliceEnemy([self._playerX, self._playerY+1],damage)
                    self.sliceEnemy([self._playerX-1, self._playerY],damage)
                    self.sliceEnemy([self._playerX+1, self._playerY],damage)
                else:
                    self.displayText(f"You missed, The strength you need to use this weapon is {self.dataDict['tiles'][self.equipped]['loot']['weapon']['minStrenght']}")

            if self._currentLevel[cords[0]][cords[1]]['entity']['HP']['current'] <= 0:
                if self._currentLevel[cords[0]][cords[1]]['entity']['item'] != 'NONE':
                    self._currentLevel[cords[0]][cords[1]]['loot']= {'type' : self._currentLevel[cords[0]][cords[1]]['entity']['item']['type'], 'amount': self._currentLevel[cords[0]][cords[1]]['entity']['item']['amount']}
                    self._currentLevel[cords[0]][cords[1]]['display'] = self._currentLevel[cords[0]][cords[1]]['loot']['type']
                else:
                    self._currentLevel[cords[0]][cords[1]]['display']= 'floor'
                self._currentLevel[cords[0]][cords[1]]['entity']= 'NONE'
                    

            self.enemyFullTurn()
            self.rendering()


    #checks if move is possible, and then moves
    def movePlayer(self, direction = 'Up'):
        cords = False
        match direction:
            case 'w':
                cords = [self._playerX, self._playerY-1]
                self._facing = 'U'
            case 's':
                cords = [self._playerX, self._playerY+1]
                self._facing = 'D'
            case 'a':
                cords = [self._playerX -1, self._playerY]
                self._facingDirectionTexture = 'L'
                self._facing = 'L'
            case 'd':
                cords = [self._playerX +1, self._playerY]
                self._facingDirectionTexture = 'R'
                self._facing = 'R'
            case 'wait':
                self.enemyFullTurn()
                
                return
            case 'e':
                self.interact()
                return
            case 'item':
                self.useItem(input('item>>'))
                return
            case 'inv':
                self.showInventory()
                return
            case 'weapon':
                self.equipWeapon(input('weapon>>'))
                return
                
        if cords != False:
            if self.isWalkable(cords, True):
                self._playerX, self._playerY = cords
                if self._currentLevel[self._playerX][self._playerY]['tile'] == 'exit':
                    self.newLevel()
                else:
                    self.enemyFullTurn()
            self.rendering()

    def logging(self, item,q=0, w=0, e=0,r=0 ,t=0,y=0):
        if self.doLogging:
            self.log = open(f'logs/log{self.dt_string}.txt', "a+")
            self.log.write(f'{item}')
            extra = [q,w,e,r,t,y]
            for x in extra:
                if x != 0:
                    self.log.write(f' {x} ')
            self.log.write(f'\n')
            self.log.close()       

    def enemyFullTurn(self):
        self.ignore = []
        self.enemyTurn()
        self.enemyTurn()
        self.ignore = []

    def wait(self):
        pass

    def autoSelect(self, syntax= 'show'):
        match syntax:
            case 0:
                syntax = False
            case 1:
                syntax = True
        if syntax == 'show':
            self.displayText(f'"autoSelect better weapons" is set to: {self.autoEquip}')
        elif syntax == True or syntax == False:
            self.autoEquip = syntax
            self.displayText(f'"autoSelect better weapons" has been set to: {self.autoEquip}')
        else:
            self.displayText(f'invalid syntax in autoSelect() function.\nSyntax needed: (True/False/\'show\'), syntax received: {syntax}')


    def showInventory(self):
        items = list(self.inventory.keys())
        text = 'Your inventory contains:\n'
        for item in items:
            text += f'{self.inventory[item]["amount"]} x {item}\n'
        self.displayText(text)

    def inInventory(self, item):
        if item in self.inventory:
            if self.inventory[item]['amount'] > 0:
                return True
        return False

    def useItem(self, item):
        if self.inInventory(item):
            if self.dataDict['tiles'][item]["loot"]["isConsumable"]:
                self.inventory[item]['amount'] -= 1
                if self.dataDict['tiles'][item]["loot"]["consumable"]["restoreHPpercentage"]:
                    extraHP = self.dataDict['tiles'][item]["loot"]["consumable"]["restoreHP"] * (self.playerStats["HP"]["max"] // 100)
                else:
                    extraHP = self.dataDict['tiles'][item]["loot"]["consumable"]["restoreHP"]
                self.playerStats["HP"]["current"] += extraHP
                if self.playerStats["HP"]["current"] > self.playerStats["HP"]["max"]:
                    self.playerStats["HP"]["current"] = self.playerStats["HP"]["max"]
            elif self.dataDict['tiles'][item]["loot"]["isWeapon"]:
                self.displayText(f"Item: '{item}' is defined as a weapon\nUse 'equipWeapon({item})' to equip it as weapon, or check the item information with 'itemInfo({item})'")
            elif 'special' in self.dataDict['tiles'][item]["loot"]:
                if self.dataDict['tiles'][item]["loot"]['special']['nextFloor']:
                    self.inventory[item]['amount'] -= 1
                    self.newLevel()

        else:
            self.displayText(f"You don\'t have: {item}\nUse 'showInventory()' to see the items you have")
        self.rendering()


    def itemInfo(self, item):
        if item not in self.dataDict['tiles']:
            self.displayText(f'{item} does not exist')
        elif self.dataDict['tiles'][item]['isLoot'] == False:
            self.displayText(f'{item} does not exist as item')
        else:
            self.displayText(f'-=={item}==-')
            self.displayText(f'Minimum per tile: {self.dataDict["tiles"][item]["loot"]["amount"]["min"]}\nMaximum per tile: {self.dataDict["tiles"][item]["loot"]["amount"]["max"]}')
            if self.dataDict["tiles"][item]["loot"]["isWeapon"]:
                self.displayText(f'Strenght needed to weild this weapon: {self.dataDict["tiles"][item]["loot"]["weapon"]["minStrenght"]}')
                self.displayText(f'It does {self.dataDict["tiles"][item]["loot"]["weapon"]["attack"]} attack damage\nWeapon type is {self.dataDict["tiles"][item]["loot"]["weapon"]["type"]}\nWeapon weight is {self.dataDict["tiles"][item]["loot"]["weapon"]["weaponWeight"]}')
            self.displayText(f'Item Rarity: {self.dataDict["tiles"][item]["loot"]["rarity"]}')
            if self.dataDict["tiles"][item]["loot"]["isConsumable"]:
                percentOrNot = ""
                if self.dataDict["tiles"][item]["loot"]["consumable"]["restoreHPpercentage"]:
                    percentOrNot = '%'
                self.displayText(f'It restores {self.dataDict["tiles"][item]["loot"]["consumable"]["restoreHP"]}{percentOrNot} HP when consumed')
            if "special" in self.dataDict["tiles"][item]["loot"]:
                if self.dataDict["tiles"][item]["loot"]["special"]["nextFloor"]:
                    self.displayText('It will warp you to the next floor')



            

    def equipWeapon(self,item):
        if self.inInventory(item):
            if self.dataDict['tiles'][item]["loot"]["isWeapon"]:
                self.equipped = item
                self.hasWeaponWeight = self.dataDict['tiles'][self.equipped]["loot"]['weapon']['weaponWeight']
                self.displayText(f"You equipped {item}")
            else:
                self.displayText(f"Item: '{item}' is not defined as a weapon\nUse 'useItem({item})' to use it as item, or check the item information with 'itemInfo({item})'")
        else:
            self.displayText(f"You don\'t have: {item}\nUse 'showInventory()' to see the items you have")

    def newLevel(self):
        self._dungeonLevel += 1
        self.loadState()
        levelNumber = random.randint(0,len(self._defaultlevels)-1)
        print(levelNumber)
        self._canvas.destroy()
        self.createLevel(self._defaultlevels[levelNumber])
        self.createCanvas()
        self.rendering()

    def displayText(self, text,q=0, w=0, e=0,r=0 ,t=0,y=0):
        extra = [q,w,e,r,t,y]
        for x in extra:
            if x != 0:
                text += f'\n{x}'
        print(text)
        self.rendering()