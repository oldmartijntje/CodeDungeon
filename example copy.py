import CodeDungeon
player = CodeDungeon.System()
player.startGame()
# Your Python instructions go here:

while True:
    player.movePlayer(input())

#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()