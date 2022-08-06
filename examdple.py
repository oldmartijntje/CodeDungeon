import Roguelike
import random
player = Roguelike.System(714505)
player.startGame('play', [[[6,[4,69]],0],[0,0],[0,{'tile': 'floor', 'entity': {'type': 'rat', 'level': 4, 'item': {'type': 'bandaid', 'amount': 2}}, 'loot': {'type':'gold_coin', 'amount':1}, 'text': ['cheese','kaasblokje']}]])
# Jouw python instructies zet je vanaf hier:


while True: player.movePlayer(input())
player.movePlayer('Down')    
player.movePlayer('Left')    
player.movePlayer('Right')   


#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()