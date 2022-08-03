import Roguelike
import random
player = Roguelike.System(random.randint(0,1000000))
player.startGame('play')
# Jouw python instructies zet je vanaf hier:


while True: player.movePlayer(input())
player.movePlayer('Down')    
player.movePlayer('Left')    
player.movePlayer('Right')   


#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()