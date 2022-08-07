import os
value = 0
tested = 0
exampleMade = False
def endText():
    print(f'Setup complete\n{value}/{tested} items installed')
    input('Press [ENTER] to close')
exampleName = 'example'


tested += 1
if not os.path.exists(f'{exampleName}.py'):
    examplePy = open(f"{exampleName}.py", "w")
    value += 1
    exampleMade = True
    examplePy.close()
examplePy = open(f"{exampleName}.py", "r")
tested += 1
if exampleMade == True or examplePy.read() == '':
    examplePy.close()
    examplePy = open(f"{exampleName}.py", "w")
    examplePy.write("""import CodeDungeon
player = CodeDungeon.System()
player.startGame()
# Your Python instructions go here:


#launch program
player.gameWindow.mainloop()
# exit the program
player.exit()""")
    examplePy.close()
    value += 1

endText()