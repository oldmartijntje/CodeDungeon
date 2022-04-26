import Roguelike
import random
player = Roguelike.System(random.randint(1,1000),3)
player.startGame()
# Jouw python instructies zet je vanaf hier:

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



# exit the program
player.exit()