# Mini-Roguelike
>Learning to code should be fun!

This Project is there as learning tool, a tool to teach kids the logic of programming in a fun way, By programming the movement of your character in a game.

##### Table of Contents  
[Installation](#installation)  
[How to use](#how-to-use)  

## Installation

First of all you need to <a href='https://www.python.org/downloads/'>install Python</a>, It works with <a href='https://www.python.org/downloads/release/python-3101/'>Python 3.10.1</a>, I don't know about other versions.
>Make sure that when you are installing python you enable this:
>
>![checkButton](sprites/readme/readmePython.png)

When you have python installed, install <a href="https://pillow.readthedocs.io/en/stable/installation.html">PIL</a> (Pillow),
If you have Pip installed you can do it by typing this into your console:
>pip install Pillow

<small><i><a href='https://pypi.org/project/Pillow/'>PIL on the Python Package Index.</a></i></small>

And the last step: Run <a href="https://github.com/oldmartijntje/Mini-Roguelike/blob/main/setup.py">setup.py</a> which should be installed when you downloaded the Release.

There should be code that looks like this in example.py.

![Code](sprites/readme/examplepy.png)

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

## How To Use
Open example.py, and your code should go between line 4 and 7:

![Code](sprites/readme/examplepy.png)

>How to move the player:
>
>![Code](sprites/readme/use1.png)

When you use these, the character automatically looks in the direction you last moved (even tho it might not look like it because the player only has 2 sprites)

>But if you want to look in a direction without moving, you need to use these instead:
>
>![Code](sprites/readme/use2.png)

Moving costs a turn where as looking doesn't, so you can spam looking commands without an enemy ever coming closer. 

>There are also these other easy commands:
>
>![Code](sprites/readme/use3.png)
>
>>player.wait() skips your turn
>
>>player.interact() interacts with the world, it can make you talk to a npc, read a sign, attack an enemy, or pickup loot.
>
>>player.showInventory() shows you everything you have in your inventory in the console:
>>
>>![inventory](sprites/readme/inventory.png)
>
>>player.equipWeapon('weaponName') equips a weapon, for example:
>>
>>player.equipWeapon('wooden_sword') to equip the wooden_sword, and the console will give feedback, for example when it can't equip it
>
>>player.useItem('itemNme') you use to use an item, for example:
>>
>>player.useItem('moldy_bread') to consume the moldy_bread
>
>>player.itemInfo('itemName') to get information about the item or weapon, for example:
>>
>>![code](sprites/readme/use4.png)
>>
>>would get this in the console:
>>
>>![code](sprites/readme/info.png)

>This is autoEquip, The first shows which it is, the second and third sets it to True or false.
>
>What this does is so that when you pickup a better weapon, if it automatically equips it, The default is set to True.
>
>![Code](sprites/readme/use5.png)

You can go as advanced as you want to go, by using anything python can do.

>And with these:
>
>![Code](sprites/readme/use6.png)


### Notes
This uses @oldmartijntje his account system: https://github.com/oldmartijntje/accounts-system

This is a project inspired by:

The robotarm: https://github.com/jeroenslemmer/robotarm-python-2021

Pixeldungeon: http://pixeldungeon.watabou.ru

### explenations
states are generated first, to ensure that the followup level is exactly the same, and that random choices by Program won't change it