import accounts_omac
import random
class System:
    def __init__(self, levelName = ''):
        pass
    def startGame(self):
        global data, configSettings
        configSettings = accounts_omac.configFileTkinter()
        data = accounts_omac.defaultConfigurations.defaultLoadingTkinter(configSettings)
        if data == False:
            exit()

    def exit(self):
        data = accounts_omac.saveAccount(data, configSettings)
        exit()
