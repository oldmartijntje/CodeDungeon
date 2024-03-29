# Code Dungeon
>Learning to code should be fun!

This Project is there as learning tool, a tool to teach kids the logic of programming in a fun way, By programming the movement of your character in a game.

You need Python 3.10.1+

##### Table of Contents  
- [Installation](#installation)  
- [How 2 Update to this version](#update)  
- [How to use](#how-to-use)  
- [How to change content](#how-to-create)  
  + [Map Editor](#map-editor)
    - [Advanced Loading](#advanced-loading)
  + [GameData Editing](#gamedata-editing)
    - [Version](#version)
    - [Template](#template)
    - [Preference](#preference)
    - [StartingLoot](#startingLoot)
    - [equippedWeapon](#equippedweapon)
    - [playerStats](#playerstats)
    - [dungeon](#dungeon)
    - [balancing](#balancing)
    - [rarities](#rarities)
    - [chance](#chance)
    - [appSettings](#appsettings)
    - [playerImages](#playerimages)
    - [debug](#debug)
    - [Gamma](#gamma)
    - [text](#text)
    - [default Tiles](#defaulttiles)
    - [tiles](#tiles)
  + [Testing tools](#testing-tools)
- [Updating](#Updater) 
- [Trouble?](#help) 
- [Credits](#credits) 
## Installation

First of all you need to <a href='https://www.python.org/downloads/'>install Python</a>, It works with <a href='https://www.python.org/downloads/release/python-3101/'>Python 3.10.1+ </a>Earlier versions won't work.
>Make sure that when you are installing python you enable this:
>
>![checkButton](sprites/readme/readmePython.png)

When you have python installed, install <a href="https://pillow.readthedocs.io/en/stable/installation.html">PIL</a> (Pillow),
If you have Pip installed you can do it by typing this into your console:
>pip install Pillow

<small><i><a href='https://pypi.org/project/Pillow/'>PIL on the Python Package Index.</a></i></small>

Then you need to download the code, click this button:

![download](sprites/readme/install.png)

And then you need to click download zip:

![download](sprites/readme/install2.png)

Then in your file explorer, right click the zip folder:

![zip](sprites/readme/install3.png)

and then click extract all:

![extract all](sprites/readme/install4.png)

Then you put in the path where you want to save it and click extract:

![extract](sprites/readme/install5.png)

Then open the folder untill you see something like this:

![files](sprites/readme/install6.png)

>IMPORTANT: You need to run the python files from this folder, otherwise the program won't work.
>
>Because if you do it from an upper folder, The imports wont work, and the files would be written to the wrong folder.

And the last step: Run <a href="https://github.com/oldmartijntjeCodeDungeon/blob/main/setup.py">setup.py</a> which should be installed when you downloaded the Release.

There should be code that looks like this in example.py.

```python
import random
import CodeDungeon
player = CodeDungeon.System()
player.startGame()
# Your Python instructions go here:

#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()
```

You should run it first like this before you change it.

>When you run it an image like this will pop up:
>
>![Account system](sprites/readme/account1.png)

if you are using other apps using <a href="https://github.com/oldmartijntje/accounts-system">this</a> account system then it's usefull to do what it says, otherwise just click continue.

>After you clicked continue, a menu like this will show up:
>
>![Account system](sprites/readme/account2.png)

Put it to yes, and you can cange the nme if you want to, but you don't have to change the name.

>After you did that this popup should show up:
>
>![Account system](sprites/readme/account3.png)

You need to click 'Ok'

>After you did that, this should show up:
>
>![game](sprites/readme/game.png)

This is the game, you can close it, and the installation process is done.

## update

So you used an older version and want to update to this newer version.

We reccomend to only download releases.

First off: re-download everything (to another folder, not the folder of the old version)

Second: copy example.py from the old folder to the new folder.

That's all you need to do UNLESS if you changed the files.

If you added custom maps or changed the gameData.json copy those over to the new folder, make sure to check what changed in this version to see how to update those 2 files.

## How To Use

Open example.py, and your code should go between line 4 and 7:

```python
import random
import CodeDungeon
player = CodeDungeon.System()
player.startGame()
# Your Python instructions go here:

#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()
```

for different dungeons, put a number here, this is the random.seed().

![Code](sprites/readme/use7.png)

>How to move the player:
>
>![Code](sprites/readme/use1.png)
>
>A codebox for copy/paste:
>```python
>player.moveDown()
>player.moveUp()
>player.moveLeft()
>player.moveRight()
>```

When you use these, the character automatically looks in the direction you last moved (even tho it might not look like it because the player only has 2 sprites)

>But if you want to look in a direction without moving, you need to use these instead:
>
>![Code](sprites/readme/use2.png)
>
>A codebox for copy/paste:
>```python
>player.lookDown()
>player.lookUp()
>player.lookLeft()
>player.lookRight()
>```

Moving costs a turn where as looking doesn't, so you can spam looking commands without an enemy ever coming closer. 

>There are also these other easy commands:
>```python
>player.wait()
>player.interact()
>player.showInventory()
>player.equipWeapon('weaponName')
>player.useItem('itemName')
>player.itemInfo('itemName')
>player.merge('itemName')
>```
>
>>player.wait() skips your turn
>
>>player.interact() interacts with the world, it can make you talk to a npc, read a sign, attack an enemy, or pickup loot.
>
>>player.showInventory() shows you everything you have in your inventory in the console:
>>
>>![inventory](sprites/readme/inventory.png)
>
>>`player.equipWeapon('weaponName')` equips a weapon, for example:
>>
>>`player.equipWeapon('wooden_sword')` to equip the wooden_sword, and the console will give feedback, for example when it can't equip it
>
>>`player.useItem('itemNme')` you use to use an item, for example:
>>
>>`player.useItem('moldy_bread')` to consume the moldy_bread
>
>>player.itemInfo('itemName') to get information about the item or weapon, for example:
>>
>>![code](sprites/readme/use4.png)
>>
>>would get this in the console:
>>
>>![code](sprites/readme/info.png)
>
>>`player.merge('itemName')` is new since 1.3.0
>>
>>You can use this to merge multiple of the same item into something else, like a stronger version of the item.

>This is autoEquip, The first shows which it is, the second and third sets it to True or false.
>
>What this does is so that when you pickup a better weapon, if it automatically equips it, The default is set to True.
>
>![Code](sprites/readme/use5.png)
>
>A codebox for copy/paste:
>```python
>player.autoSelect()
>```

You can go as advanced as you want to go, by using anything python can do.

>And most commands have a return value:
>
>A codebox for copy/paste:
>```python
>print(player.showInventory())
>if player.inInventory('itemName'):
>    pass
>print(player.itemInfo('bread'))
>```

## How to create

This program is highly configurable so i am splitting it into multiple parts
 - [Map Editor](#map-editor)
 - [GameData](#gamedata-editing)
 - [Testing tools](#testing-tools)

## Map Editor

>The level editor is enabled by putting 'Create' (or lowercase) in between the brackets as seen on this picture:
>
>![Code](sprites/readme/level1.png)
>
>A codebox for copy/paste:
>```python
>import random
>import CodeDungeon
>player = CodeDungeon.System()
>player.startGame('Create')
># Your Python instructions go here:
>```

When enabled you will see something like this:

![editor](sprites/readme/level2.png)

When you click a square it will change number and color, here is the list of what is what:
 - 0: Air, with a chance to spawn loot or enemy (configurable in json).
 - 1: A wall.
 - 2: Entrance, if you have multiple it will spawn you at the last entrance.
 - 3: Exit, walk through this to go to the next level, a lavel can have multiple exits.
 - 4: High loot chance and normal enemy chance (configurable in json).
 - 5: High enemy chance and normal loot chance (configurable in json).
 - 6: Sign, it will have a message (configurable in multiple ways).
 - 7: Npc, it will have a message (configurable in multiple ways) (might make it be able to walk in the future, so be aware of that when putting it in a map).
 - 8: Nothing spawns here, just air.
 - 9: Bossfight, an enemy which is stronger than a normal enemy with chance of better loot, don't need to defeat it to proceed to next level.

When you are happy with the map, you can export it in 2 ways:
 - export to console:

You can copy the map from the console and easily edit it, but you need to put it in the json yourself later.
 - export to json:

It will automatically be put into the levelData.json, but it will be harder to edit the map from the json since it's one big list of numbers in the json.

This is how it looks in the json:

![level erray](sprites/readme/level3.png)

If you want to give an npc or sign specific text, you can edit the levelList:

>Change it from this:
>
>![erray](sprites/readme/level4.png)
>
>To something like this:
>
>![erray](sprites/readme/level5.png)
>
>And then the sign will display that text.

The same works with 0, 4, 5 and 9, but instead of text it takse different data:

>0, 4 and 5 have a loot modifier, the higher the number, the higher the chance of better loot (enemy loot drops too). just put it into a list and add a number:
>
>![erray](sprites/readme/level6.png)

For 9 it's a bit different since it can take 3 modifiers:

>![erray 1](sprites/readme/level7.png)
>
> - The first one is the modifier for the loot that might spawn on that tile. (put 'NONE' for default)
> - The second one is the modifier for the loot you get when you kill the enemy. (put 'NONE' for default)
> - The third one is the boss difficulty, it ranges from the first number to the last, but if you want it to always be a specific number you can do it by putting it like this:
>
>![erray 2](sprites/readme/level8.png)
>
>You can also just put only 1 modifier if you only want to change 1:
>
>![erray 3](sprites/readme/level9.png)

If you don't put the extra argument there, the sign will pick a random text out of the gameData.json, it's the same with the NPC but they have different texts they pick from.

If you want to make maps a bit more advanced, you can do that. What the game does when it encounters a map number, it creates a dictionary at the cordinate. the dictionary looks like this when empty:

```Python
{"tile": "NONE","entity": "NONE","loot": "NONE","lock": "NONE"}
```

And if you want to create loot, replace the 'NONE' with this: 

![Loot](sprites/readme/level11.png)

To give it text, put one of these:

>![text](sprites/readme/level12.png)
>
>If you put the erray, it will choose one that it always will display once u interact with it.

If you give an enemy or loot text, it will only show the text the first time you interact with it.

This is how you create an enemy:

![entity](sprites/readme/level13.png)

The item in the entity is what it drops when it dies.

>Like always you can add a list and it will randomly select:
>
>![entity](sprites/readme/level18.png)
>
>But you might not want the rat to always be level 10, so if you change it to this:
>
>![entity](sprites/readme/level19.png)
>
>It will add the number it chooses, to the base level. (the level all entitys have in that map) (v1.2+)

If you want a map where it has a chance to have a wall, and chance to have air, that's possible.

If you put on the tile a list where the first argument in the list is an '?' and the other arguments in the list are the possabillities it will work:

>![text](sprites/readme/level14.png)
>
>This wil randomly select between air or a wall.

And you can combine it with the dict method too:

>![text](sprites/readme/level15.png)
>
>This wil randomly select between air or this predefined tile.

>If you haven't put in an exit, or start, it will randomly replace an 0 or 8 for an exit and start, unless if you add this in the level list on the first position:
>
>![level erray](sprites/readme/level17.png)
>
>This is needed if you predefine an exit as dictionary, cause it won't see that as defined exit

#### v1.1.0+

>![text](sprites/readme/level16-3.png)
>
>You can lock a tile, (doesn't work on moving things, so if there is a lock on an entity only there will be a lock on air) you can lock it by minimum: HP, Strength, Level or needing a specific item
>
>This is not used by default, only when you put a tile in with dictionary
>
>If you only want to use one of the things, you can leave the others out:
>
>![text](sprites/readme/level20-2.png)

#### v1.2.0+

You can have multiple lists of maps since it's saved in a dictionary now. The default levels are defined in the gameData.json:

![text](sprites/readme/level23.png)

When you click the export button it will export to the default. The default is the one the generator chooses from when starting the game or when it's undefined on the exit.

Exits work differently from this point on, intead of looking for if it's a exit tile, it looks for if it has a 'exit' in the tile, and if it does, it checks if `['exit']['exit']` is set to True. 

![text](sprites/readme/level21.png)

`'nextLevelList'` is what level it picks from when it generates a new level. If `['exit']` has been set to false, you don't need to include this in the dictionary.

If you don't want all of your tiles to look the same even though they behave the same (or not, your choice) and you don't want to manually define everything, use `DefaultTiles` (context needed for this is in the gameData edeting part of readme). 

![text](sprites/readme/level22.png)

By putting the "|" in front it will know what to do, and pick a random one of the objects. This is always on for the tiles you can create using the built in level editor.

If you want to get an enemy or loot in a pre-defined tile but you want to use the default generator for loot or an enemy, you can now do that by replacing `"NONE"` with `"True"` (upper or lower case deosn't matter). It will have a 100% chance rate of spawning. 

![dict](sprites/readme/level24.png)

You can also define the enemy and put "true" in the entity item:

![dict](sprites/readme/level25.png)

This also works in the lock:

![dict](sprites/readme/level26.png)

## Advanced Loading

You can also load a specific level, so you don't need to be lucky to test a map.

By putting the level inside the `player.startGame()` as the second paramater, be sure to tell the app what mode you want to open, `'Play'` or `'Create'`

```python
import random
import CodeDungeon
player = CodeDungeon.System()
player.startGame('Create', [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
# Your Python instructions go here:
```
This is the default editor level.

You can also play that level by changing `'Create'` to `'Play'` in the above example, like this:
```python
player.startGame('Play', [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
```

You can also load a specific level from the levelData.json like this:
```python
player.startGame('Create', 4)
```
This will load the 5th level.

There is also a way to load a level of a specific size without putting the rows manually:

```python
player.startGame('Create', '10x15')
```
This will load a level of the sixe 15 by 10, and this works with the rotating of a level in the level editor.

And if you would want to turn everything into a wall by default:
```python
player.startGame('Create', '10x15x1')
```
Where tha last number is the same as in the editor

This is not new but has been undocumented for some reason.


## GameData Editing

Gamedata is massive so again, i'll make a quick navigation menu:
 - [Version](#version)
 - [Template](#template)
 - [Preference](#preference)
 - [StartingLoot](#startingLoot)
 - [equippedWeapon](#equippedweapon)
 - [playerStats](#playerstats)
 - [dungeon](#dungeon)
 - [balancing](#balancing)
 - [rarities](#rarities)
 - [chance](#chance)
 - [appSettings](#appsettings)
 - [playerImages](#playerimages)
 - [debug](#debug)
 - [Gamma](#gamma)
 - [text](#text)
 - [default Tiles](#defaulttiles)
 - [tiles](#tiles)

### version

This contains 2 items: `"name"` and `"number"`, this shows in which version the game was last updated or created. Don't touch this, unless you want the (future) updater app to get confused and maybe corrupt it.

`"name"` changes every update, number changes every time there changes something.

`"number"` is for the JSON versions, this number changes every time there is a change to the JSON structure

If this doesn't exist in the gamedata, it fill automatically add it. But that will make it be at the bottom of your json instead of the top like normally.

### Template

This is a template of a pre-defined tile, with everything set to `NONE`

This get's never used, this is just so you can easily start using pre-defined tiles for level editing
```JSON
"template": {
    "tile": "NONE",
    "entity": "NONE",
    "loot": "NONE",
    "lock": "NONE",
    "exit": {
      "exit": false
    }
  },
  ```

### Preference
`"preference"` is quite small, it has 2 things:

![Preference](sprites/readme/data1.png)

`"autoEquipBetter"` is something you can toggle in game: 

![AutoEquip](sprites/readme/use5.png)

`"autoEquipBetter"` means that if you pickup a better weapon than ur currently holdinng, that it will equip the new one. and sleeptime is the time it takes for an enemy to move, if set to 0 everything will happen instantly, and if set to 1, you'll be there for a while.

### StartingLoot

![StartingLoot](sprites/readme/data2.png)

`"startingLoot"` can have as many items as you want, make sure that the items also exist in the tiles tho, otherwise it will give errors.

### equippedWeapon

This contans which weapon you are using, make sure it's defined in Tiles too, otherwise bugs will happen.

![equippedWeapon](sprites/readme/data3.png)

The `"weight"` is for the automatic equip better, so that it knows which is better, put it at 0 if you want anything to replace it.

### playerStats

![playerStats](sprites/readme/data4.png)

These are self explanetory:

 - `"statsPerLevel"` is the amount of everything you'll gain for every level
 - `"beginStats"` is the stats you have at level 0
 - `"startLevel"` is the level your character has at the beginning
 - `"XPneeded"` is the amount of xp you need per level

### dungeon

```JSON
"dungeon": {
    "startLevel": 3,
    "defaultLevelList": "default",
    "startingFloor": 1
  },
```

`"startlevel"` = The starting difficulty of the dungeon, which enemys are based off, every floor you go down adds 1 to this number.

`"defaultLefelList"` = The default list in the levelData.json that it loads levels from.

`"startingFloor"` = the floor you want to start at.

### balancing

![balancing](sprites/readme/data6.png)

These are settings to balance out the game.
 - `"doStrengthDamage"`

This means that your strength adds to the attack damage, without it the damage is defined by the wepon you are using and will never get better.
 - `"strengthDevidedBy"`

This only is usefull when the doStrengthDamage is set to true, this is the amount of damage it does, if its set to 3 and you have 9 strength, it will do 3 attack damage.

### rarities

![rarities](sprites/readme/data7.png)

This is the chance of loot appearing, it's not in percentages, it's in weight, just add any rarity you want.

### chance

![chance](sprites/readme/data8.png)

These are the chances of things to spawn in maps, the chance of enemies and loot to spawn in air, and in their dedicated tiles (4/5 in the editor)

If you make it 100 or higher it will always spawn

### appSettings
These are app settings, technical stuff.

![appSettings](sprites/readme/data9-2.png)

The `"offset"` and size are for the level renderer.

`"size"` is 32 because the appTextures are 32 pixels by 32 pixels, if you want to change the size of those, change this. And if you change Size, high chance the textures aren't perfectly positioned, that's where you use offset for.

`"offset"` is offset in pixels, and size is tilesize.

`"maxTypes"` and colors is for the level editor, if you increase mextypes then also add an color, tho adding a maxtype does liturally nothing. Changing colors just changes the colors in the level editor.

The unknown is for when you changed a map using predifined of random choices, obviously you don't want to overwrite those, and you don't want the editor to crash, so these are what it shows for a predefined tile. (v1.2.0+)

### playerImages

![playerImages](sprites/readme/data10.png)

These are the textures the player has:

![file names](sprites/readme/player.png)

### debug

![debug](sprites/readme/data11.png)

These are debug settings.
 - `"logging"`, When set to true it will keep the logs, when false, it will delete the logs when closed (but will still be there if it crashes)
 - `"combat"` enables combat.
 - `"enemyai"` enables enemy AI (which is not an AI but an simple algorithm).
 - `"sleep"` means that it takes time delay between enemy movement.
 - `"EnemyLoop"` is the amount of times it checks to see if an enemy can move (for if another enemy moved out of the way).
 - `"replayMode"` writes down every movement you make and item you use/equip, so that you can get to the same place as you once were on that 1 seed. (works same as logging)
 - `"enemyLoopPerEnemy"` (since v1.2.0) will loop the enemy movement an amount of times, so that it can walk multiple tiles if it has those movement rules.

### Gamma

![Gamma](sprites/readme/data12.png)

This is about the view square:

![show](sprites/readme/view1.png)

>If you change distance to 4:
>
>![show](sprites/readme/view2.png)

>If you change darknessfull to 0.8 and darknessfade to 0.1:
>
>![show](sprites/readme/view3.png)

>If you change darkness fade and full above 1:
>
>![show](sprites/readme/view4.png)

You can create some funky things with these settings, but you probably don't need to change this like ever.

### text

![text](sprites/readme/data13.png)

This is the npc and sign text, the 2 lists it picks random text from if it's not defined in the level code. The default text is quite useless.

### defaultTiles

![defaultTiles](sprites/readme/data22.png)

These are the default walls it will place with the level editor, so if you have multiple wall variations, just add them to the list of `'wall'`

They still need to be defined in the Tiles to work, otherwise it will crash.

When using pre-defined tiles in level editing, You can also use this feature by putting | in front of the tile, like: `"|wall"`, and you can add your own custom lists of this and it will still work. 

If there is an error because of something loading an default tile, it will display missing texture, and output it into logfile (updated in v1.2.0)

### tiles

>Before i explain how this works, There is a tile: `"missingTile"` which it uses to load errors, if you delete it (you can modify `"isWalkable"` and `"Image"` and `"ShowOutsideAs"` without errors, the other things might break it even more) and it encounters an error, the game might crash without explanation and maybe no indication in the logfile. So please don't touch that 1 tile.

Tiles, this is where everything is defined, items, walls, enemies, exits, floors and signs, just everything.

Everything in here has these items:

![tiles](sprites/readme/tiles1.png)

- `"ShowOutsideAs"` means which texture it shoud show outside of the viewing area
- `"Walkable"` can you walk on it? floor yes, wall no
- `"Image"` The texture it has in the sprites/ folder
- `"isEnemy"` is it an enemy? (this enables more settings)
- `"isInteractable"` can you interact with it? like a sign? But it does nothing, you can remove it form the sign but u can still interact with it.
- `"isLoot"` is it loot? can you pick it up? (this enables more settings)

You can also add a transform dict to tiles:

>![transform](sprites/readme/data19.png)
>
>With this you can transform a closed or locked door into an opened door for example.

#### loot:

To show how to do loot i'll show 2 examples, weapon and food.

>![loot](sprites/readme/data14.png)
>
>When you enable isLoot to True, you need to add this dictionary.

- `"amount"` is self explanetory: the amount you'll find per tile.
- `"isWeapon"` is it a weapon?
- `"isConsumable"` is it consumable?
- `"rarity"` How rare is it? (pick one from the rarities you defined or `'NONE'` for not generatable loot)

If you set isWeapon to true, you need to add the "weapon" dict:

![weapon](sprites/readme/data15-2.png)
- `"minStrength"` the amount of strength you need to use the weapon (you can use it earlier but u'll miss 50% and do less damage)
- `"attack"` the attack damage
- `"type"` there are 2 types: stab and slice, stab stabs 1 enemy, slice attacks all enemies next to u
- `"weaponWeight"` the order of defined weapons (for auto equip to know which is better)

If you set `"isConsumable"` to true, you need to add the `"consumable"` dict:

```json
"consumable": {
    "HPAmount": 0,
    "type": "+",
    "strengthLevels": 1
}
```
- "type" : Set it to `"+"` or `"-"` or `"%"` or `"set"` or `"-%"` HP (this changed in v1.2.0)
- `"HPAmount"` the amount of HP

Since 1.3.0 there is a new variable you can add:
```json
"consumable": {
    "HPAmount": 0,
    "type": "+",
    "strengthLevels": 1
}
```
Where `"strengthLevels"` is the amount of strenth levels you will gain by consuming it, if you have this you will still need the `"HPAmount"`, but just set it to 0 if you don't want that.
`"type"` only effects `"HPAmount"` and not `"strengthLevels"`


>![special](sprites/readme/data17.2.png)
>
>You can also add this dictionary
> - `"nextFloor"` will instantly warp you to the next floor. Before v1.2.0 you had to set it to True, after v1.2.0 you need to put the levelList you want it to pick from

Since 1.3.2 you also have the `"mergable"` variable in the `'loot'` dict:
```json
"item": {
      "ShowOutsideAs": "floor",
      "Walkable": false,
      "Image": "loot",
      "isEnemy": false,
      "isInteractable": false,
      "isLoot": true,
      "loot": {
        "amount": {
          "min": 1,
          "max": 1
        },
        "isWeapon": false,
        "isConsumable": false,
        "rarity": "uncommon",
        "mergable": {
            "mergeAmount": 3,
            "mergeIntoAndAmount": {
            "other_item": 2,
            "yet_other_item": 1
            }
        }
      }
    },
```
Mergables work the following:
You need `"mergeAmount"` times the item to merge them into `"mergeIntoAndAmount"`. in this example merging 3 `'item'` items turns into 1 `'yet_other_item'` item + 2 `'other_item'` items.
 - note that in v1.3.0 and v1.3.1 mergables were in a different place.

#### enemy:

When you put `"isEnemy"` to true, you need to add this dictionary:

![enemy](sprites/readme/data18.png)

- `"doubleAttack"` it's true it can double attack (until v1.2)
- `"statsPerLevel"` the stats this enemy will have per level
- `"lessATKpointsPercentage"` the percentage of damage variaton, the ATK minus 0% to this% 
- `"hitChance"` the chance for the enemy to hit
- `"movementRules"` does something since v1.2:

>![movementRules](sprites/readme/data20.png)
>
>The `'insteadOf'` means that it's either 1 or the other:
>
>It either moves 1 to 3 tiles or attacks 4 times
>
>But if you set it to `'and'` it will be:
>
>![movementRules](sprites/readme/data21.png)
>
>move 1 tile and then attack twice, or attack twice and don't move.

If not set to `'and'` or `'insteadOf'` it can't attack, but can still move.

#### spawning

You can also set the spawning limits of loot and enemies (since v1.3.1):

we take for example the golden_key:
```JSON
    "golden_key": {
      "ShowOutsideAs": "floor",
      "Walkable": false,
      "Image": "loot",
      "isEnemy": false,
      "isInteractable": false,
      "isLoot": true,
      "loot": {
        "amount": {
          "min": 1,
          "max": 1
        },
        "isWeapon": false,
        "isConsumable": false,
        "rarity": "legendary"
      },
      "spawning": {
        "fromFloor": 7
      }
    }
```

`"spawning"` in tiles, only spawning from a specific moment with these attributes:
- `"toLevel"`
- `"fromLevel"`
- `"toFloor"`
- `"fromFloor"`

this only works with enemies and loot

## Testing Tools

>Want to quickly load a specific level:
>
>![level](sprites/readme/tool1.png)

>Want to load a specific level from the levelData:
>
>![level](sprites/readme/tool2.png)

>Want to load a big empty level:
>
>![big empty level](sprites/readme/tool3.png)

>Want to load a big level where everything is an exit:
>
>![big exit level](sprites/readme/tool4.png)

>Other level functions work like this too:
>
>![probably impossible level](sprites/readme/tool5.png)

>When using the dict like ths, make sure it has // instead of the x, and make sure it's a valid json string:
>
>![lot of rats](sprites/readme/tool6.png)

There is a folder called Development Tools, it has a tool called `"testingRarities.py"` where it loads your json, and tells you how many you get of each type when it picks 1000 items. `"testingItemGeneration.py"` works the same but with the items themselves and not just the rarities.

To use it, drag it into the main folder and run it.

## Updater

You have an <a href = https://github.com/oldmartijntje/CodeDungeon/blob/main/updater.py>updater.py</a>. This can be used for updating your JSON files to a newer version.

The updater only works since V1.3.2 and can updae from V1.3.0+ 

How to use:
 - Run updater.py
 - the program will do everything without input

note: 
- it needs the `"version"` dict in the json to not be tempered with.
- if there is something wrong with the version number, there is troubleshooting in place to help you.


## help

Go to the <a href = https://github.com/oldmartijntje/CodeDungeon/blob/main/troubleshooting.md>TroubleShooting.md</a> for error codes and how to solve them.

## Credits
This uses @oldmartijntje his account system: https://github.com/oldmartijntje/accounts-system

This is a project inspired by:

The robotarm: https://github.com/jeroenslemmer/robotarm-python-2021

Pixeldungeon: http://pixeldungeon.watabou.ru

