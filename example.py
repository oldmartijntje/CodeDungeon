import Roguelike
import random
player = Roguelike.System(random.randint(1,1000),3)
player.startGame()
# Jouw python instructies zet je vanaf hier:

player.distence([1,1], [1,100])
player.move()
player.move('Down')    
player.move('Left')    
player.move('Right')    


#launch program
#player.gameWindow.mainloop()
# exit the program
player.exit()