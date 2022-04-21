import accounts_omac
import random
import tkinter
from tkinter import ttk

    #0 air
    #1 wall
    #2 start
    #3 next level
    #4 high chance of loot
    #5 high chance of enemy
    #6 sign

class System:

    
    _defaultlevels = [
    [[1,1,1,1,1,1,1,1,1,1], [1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]]
    buttons = []




    def __init__(self, seed : int = 0):
        global data, configSettings
        self.seed = seed
        random.seed = seed
        configSettings = accounts_omac.configFileTkinter()
        data = accounts_omac.defaultConfigurations.defaultLoadingTkinter(configSettings)
        if data == False:
            exit()

    def change(self,location):
        x, y = location
        self._defaultlevels[0][x][y]+= 1
        if self._defaultlevels[0][x][y] > 6:
            self._defaultlevels[0][x][y] = 0

        exec(f'{location}.configure(text = defaultlevels[0][{x}][{y}])')

    def startGame(self, mode = 'Play'):
        global window
        window = tkinter.Tk()
        self.buttons = []
        if mode == 'Create':
            for x in range(len(self._defaultlevels[0])):
                self.buttons.append([])
            for x in range(len(self._defaultlevels[0])):
                for y in range(len(self._defaultlevels[0][x])):
                    cords = [x,y]
                    self.buttons.append(ttk.Button(self, text=self._defaultlevels[0][x][y], command=lambda cords=cords:self.change(cords)))
        window.mainloop()

    def exit(self):
        global data
        data = accounts_omac.saveAccount(data, configSettings)
        exit()


