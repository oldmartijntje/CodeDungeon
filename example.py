import Roguelike
import random
player = Roguelike.System(442,3)
player.startGame()
# Jouw python instructies zet je vanaf hier:

print(player.distence([1,1], [1,2]))
while True: player.movePlayer(input(), False)
player.movePlayer('Down')    
player.movePlayer('Left')    
player.movePlayer('Right')    


#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()