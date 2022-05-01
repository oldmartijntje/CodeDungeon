
version = '2.8.0'
#code made by OldMartijntje

#functions u don't need, bacause it's just to make the system work
class systemFunctions:
    def userID(name):
        '''Create UserID'''
        from datetime import datetime
        now = datetime.now()
        UID = f'{easy.stringToAscii(now.strftime("%H:%M:%S"))}x{(easy.stringToAscii(f"{name}")+1)//2 +easy.stringToAscii(now.strftime("%m/%d/%Y"))}'
        return UID

    def on_closing():
        '''What happens when you close an account system tkinter window, this will not save your account data'''
        import tkinter.messagebox
        if tkinter.messagebox.askyesno('Accounts_omac_lib', f"Your program will be terminated\nShould we proceed?", icon ='warning'):
            exit()

    def updateRequest(message, tkinterOrConsole = 'Console', configSettings = ['accounts/', 'False', 'testaccount', '_omac'], removeAutoLoginOnUpdate =True):
        '''Asks user for confirmation to update their account, the system only asks you when something new is added to the account itself and not the system'''
        import tkinter.messagebox
        if tkinterOrConsole == 'Tkinter':
            return tkinter.messagebox.askyesno('Accounts_omac_lib', f"Your account is outdated, Do you want us to update your account?\nIf you don\'t update {message} You will keep getting this message if you load newer apps", icon ='warning')
        else:
            yesorno = ''
            while yesorno.lower() not in ['y', 'n']:
                yesorno = input( f"Your account is outdated, Do you want us to update your account?\nIf you don\'t update {message} You will keep getting this message if you load newer apps (Y/N)")
            if yesorno.lower() == 'y':
                if removeAutoLoginOnUpdate:
                    changeConfigFile([configSettings[0], 'False', configSettings[2], configSettings[3]])
                return True
            else: 
                return False

    def CAFU(accountData, tkinterOrConsole = 'Console', configSettings = ['accounts/', 'False', 'testaccount', '_omac'], removeAutoLoginOnUpdate = True):
        '''Check Account For Update, and if there is an update, it will ask you to update'''
        message = ''
        updateNeeded = False
        if 'TempData' not in accountData: #force-add since it's always empty anyways
            accountData['TempData'] = []    
        if 'UserID' not in accountData:#2.6.0
            message += 'You won\'t be able to reconnect to online lobbies if you accidentally disconnect and'
            updateNeeded = True
        if updateNeeded:
            if systemFunctions.updateRequest(message, tkinterOrConsole, configSettings, removeAutoLoginOnUpdate):
                if 'UserID' not in accountData:
                    UID = systemFunctions.userID(accountData['name'])
                    accountData['UserID'] = UID
            else:
                if 'UserID' not in accountData:
                    accountData['TempData'].append('UserID')
                    UID = systemFunctions.userID(accountData['name'])
                    accountData['UserID'] = UID
                    accountData['versionHistory'].remove(version)
                
        return accountData

    def checkVersion(account_version, system_version = version):
        '''Check if version is lower'''
        splittedAccountVersion = account_version.split('.')
        splittedSystemVersion = system_version.split('.')
        biggerOrSmaller = False
        bigger = False
        for x in range(min([len(splittedAccountVersion),len(splittedSystemVersion)])):
            if biggerOrSmaller == False:
                if splittedAccountVersion[x] != splittedSystemVersion[x]:
                    biggerOrSmaller = True
                    if int(splittedAccountVersion[x]) > int(splittedSystemVersion[x]):
                        bigger = True
        if biggerOrSmaller == False or bigger == True:
            return False
        else:
            return True

def changeConfigFile(configGiven):
    '''re-creates the systemConfig.ini based on the files given'''
    import configparser
    import os
    with open('systemConfig.ini', 'w') as configfile:
        config = configparser.ConfigParser(allow_no_value=True)
        config['DEFAULT'] = {'#don\'t change the file-extention if you are not sure of what it is' : None,
                'fileExtention' : f'{configGiven[3]}'}
        folder = configGiven[0]
        if os.path.isdir(folder):#check if the inputted folder exists
            if folder[len(folder)-1] != '/' and folder[len(folder)-1] != '\\':
                folder += '\\'
            config['User'] = {'SaveFileFolder' : folder,'AutoLogin' : configGiven[1], 'AccountName' : configGiven[2]}
        else:
            config['User'] = {'SaveFileFolder' : 'accounts/','AutoLogin' : configGiven[1], 'AccountName' : configGiven[2]}
            try:
                os.mkdir('accounts/')
            except:
                pass
        config.write(configfile)

def configFileConsole(pathLocation = False):
    '''creates or reads config file (consoleApp) 
    the argument is the path to where accounts are stored.
    if False or not given, the program will ask for you'''
    import configparser
    import string
    import os
    if os.path.isfile("systemConfig.ini"):#read config if it exists
        config = configparser.ConfigParser()
        config.read('systemConfig.ini')
    else:#create config
        with open('systemConfig.ini', 'w') as configfile:
            config = configparser.ConfigParser(allow_no_value=True)
            config['DEFAULT'] = {'#don\'t change the file-extention if you are not sure of what it is' : None,
                'fileExtention' : '_omac'}
            if pathLocation == False:
                folder = input('do you have a specific folder where you want to store accounts?\ntype the path, or not\n>')
            else: folder = 'accounts/'
            if os.path.isdir(folder):#check if the inputted folder exists
                if folder[len(folder)-1] != '/' and folder[len(folder)-1] != '\\':
                    folder += '\\'
                config['User'] = {'SaveFileFolder' : folder,'AutoLogin' : 'False', 'AccountName' : 'testaccount'}
            else:
                config['User'] = {'SaveFileFolder' : 'accounts/','AutoLogin' : 'False', 'AccountName' : 'testaccount'}
                try:
                    os.mkdir('accounts/')
                except:
                    pass
            config.write(configfile)
            print('we created systemConfig.ini, this contains configurations for the account system, change the [User] section at any time')
    try:
        fileExtention = config['DEFAULT']['fileExtention']
        path = config['User']['SaveFileFolder']
        autoLogin = config['User']['AutoLogin']
        autoLoginName = config['User']['AccountName']
        try:
            os.mkdir(path)
        except:
            pass
    except:
        delete = input('The configfile is not readable, either fix it or delete it.\nWe will close this program after you press enter. \nDo you want us to delete systemConfig.ini for you? (Y/N)\n>>')
        if delete.lower() == 'y':
            os.remove("systemConfig.ini")
        exit()

    autoLoginName = autoLoginName.replace(" ", "")
    for character in string.punctuation:
        autoLoginName = autoLoginName.replace(character, '')
    if autoLoginName == '':
        autoLogin = 'False'
    return path, autoLogin, autoLoginName, fileExtention

def configFileTkinter(pathLocation = False):
    '''creates or reads config file (consoleApp) 
    the argument is the path to where accounts are stored.
    if False or not given, the program will ask for you'''
    import configparser
    import string
    import tkinter
    from tkinter import ttk
    import os
    if os.path.isfile("systemConfig.ini"):#read config if it exists
        config = configparser.ConfigParser()
        config.read('systemConfig.ini')
    else:#create config
        with open('systemConfig.ini', 'w') as configfile:
            config = configparser.ConfigParser(allow_no_value=True)
            config['DEFAULT'] = {'#don\'t change the file-extention if you are not sure of what it is' : None,
                'fileExtention' : '_omac'}
            def chosenPath(*args):
                global folderr
                window.destroy()
                folderr = path_var.get()
            if pathLocation == False:
                window = tkinter.Tk()
                ttk.Label(window,text='do you have a specific folder where you want to store accounts, then type it in here or not.\nIf you don\'t it will get recommended path for you').grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW")
                path_var = tkinter.StringVar()
                path_entry = tkinter.Entry(window, textvariable= path_var)
                path_entry.grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW")
                ttk.Button(window,text='Continue',command=chosenPath).grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW")
                window.protocol("WM_DELETE_WINDOW", systemFunctions.on_closing)
                window.mainloop()
                folder = folderr


            else: folder = 'accounts/'
            if os.path.isdir(folder):#check if the inputted folder exists
                if folder[len(folder)-1] != '/' and folder[len(folder)-1] != '\\':
                    folder += '\\'
                config['User'] = {'SaveFileFolder' : folder,'AutoLogin' : 'False', 'AccountName' : 'testaccount'}
            else:
                config['User'] = {'SaveFileFolder' : 'accounts/','AutoLogin' : 'False', 'AccountName' : 'testaccount'}
                try:
                    os.mkdir('accounts/')
                except:
                    pass
            config.write(configfile)
            print('we created systemConfig.ini, this contains configurations for the account system, change the [User] section at any time')
    try:
        fileExtention = config['DEFAULT']['fileExtention']
        path = config['User']['SaveFileFolder']
        autoLogin = config['User']['AutoLogin']
        autoLoginName = config['User']['AccountName']
        try:
            os.mkdir(path)
        except:
            pass
    except:
        import tkinter.messagebox
        if tkinter.messagebox.askyesno('Config Error!', 'There is a problem when we try to open your settings\nWe will close the program after you click this message away\n\nDo you want us to delete the configfile (systemConfig.ini) for you,\notherwise you will have to fix it yourself', icon ='error'):
            os.remove("systemConfig.ini")
        exit()
    autoLoginName = autoLoginName.replace(" ", "")
    for character in string.punctuation:
        autoLoginName = autoLoginName.replace(character, '')
    if autoLoginName == '':
        autoLogin = 'False'
    return path, autoLogin, autoLoginName, fileExtention

def loadAccount(accountName = 'testaccount', configSettings = ['accounts/', 'False', 'testaccount', '_omac'], tkinterOrConsole = 'Console', removeAutoLoginOnUpdate = True):
    '''load existing acount'''
    import json
    import datetime
    path = configSettings[0]
    fileExtention = configSettings[3]
    #just loading the json
    with open(f'{path}{accountName.lower()}{fileExtention}.json') as json_file:
        dataString = json.load(json_file)
        if type(dataString) != dict:
            data = json.loads(dataString)
        else:
            data= dataString
        data['loadTime'] = datetime.datetime.now()
    if systemFunctions.checkVersion(data['versionHistory'][len(data['versionHistory']) -1]):
        data['versionHistory'].append(version)
    data = systemFunctions.CAFU(data, tkinterOrConsole, configSettings, removeAutoLoginOnUpdate)
    
    return data

def createAccount(accountName = 'testaccount', configSettings = ['accounts/', 'False', 'testaccount', '_omac'], tkinterOrConsole = 'Console'):
    '''create the account (will wipe existing data!!!)'''
    import json
    import datetime
    path = configSettings[0]
    fileExtention = configSettings[3]
    today = datetime.datetime.today()
    UID = systemFunctions.userID(accountName)
    data = {'name': accountName, 'nickname': accountName, 'time': [0,'0'], 'versionHistory':[version], 'appData':{}, 'collectables':{}, 'achievements':{}, 'loadTime':0, 'UserID':UID, 'TempData' : []}
    

    #creating the json
    json_string = json.dumps(data)
    try:
        with open(f'{path}{accountName.lower()}{fileExtention}.json', 'w') as outfile:
            json.dump(json_string, outfile)
            data['loadTime'] = datetime.datetime.now()
    except:
        import os
        if tkinterOrConsole == 'Console':
            delete = input('The configfile is not readable, either fix it or delete it.\nWe will close this program after you press enter. \nDo you want us to delete systemConfig.ini for you? (Y/N)\n>>')
            if delete.lower() == 'y':
                os.remove("systemConfig.ini")
        elif tkinterOrConsole == 'Tkinter':
            import tkinter.messagebox
            if tkinter.messagebox.askyesno('Config Error!', 'There is a problem when we try to open your settings\nWe will close the program after you click this message away\n\nDo you want us to delete the configfile (systemConfig.ini) for you,\notherwise you will have to fix it yourself', icon ='error'):
                os.remove("systemConfig.ini")
        exit()
    return data

def saveAccount(data, configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''saves the account back to the json, will return data for when you want to keep using the data'''
    tempdataOptions = ['UserID']
    import json
    import datetime
    path = configSettings[0]
    fileExtention = configSettings[3]
    now = datetime.datetime.now()
    timePlayed = ((now - data['loadTime']).total_seconds()) // 1
    data['loadTime'] = 0
    data['time'][0] += timePlayed
    data['time'][1] = str(datetime.timedelta(seconds=data['time'][0]))
    saveData = dict(data)
    for x in saveData['TempData']:
        if x in tempdataOptions:
            del saveData[x]
    del saveData['TempData']
    json_string = json.dumps(saveData)
    with open(f'{path}{data["name"].lower()}{fileExtention}.json', 'w') as outfile:
        json.dump(json_string, outfile)
        data['loadTime'] = datetime.datetime.now()
    return data

def checkForAccount(accountName = 'testaccount', configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
    '''check if the account exists'''
    import os
    path = configSettings[0]
    fileExtention = configSettings[3]
    if os.path.exists(f'{path}{accountName.lower()}{fileExtention}.json'):#check if account exists
        return True
    else:
        return False

def removeCharacters(name, removeCharacters = []):
    '''this only keeps numbers and letters in the string you provide, unless you give a list of characters, then it removes those characters instead'''
    import string
    name = name.replace(" ", "")
    if removeCharacters == '' or removeCharacters == []:
        for character in string.punctuation:
            name = name.replace(character, '')
    else:
        for character in removeCharacters:
            name = name.replace(str(character), '')
    return name

def askAccountNameConsole(configSettings = ['accounts/', 'False', 'testaccount', '_omac'], text = 'please give username\n>', text2 = 'Automatically login to this account? (Y/N)'):
    '''simply asks input for an account name (console app), returns account name and if autologin is enabled'''
    autoLogin = configSettings[1]
    autoLoginName = configSettings[2]
    #for the autologin
    if autoLogin.lower() == 'true':
        username = autoLoginName
        remember = True
    else:
        username = ''
        while username == '':  
            username = input(text)
            username = removeCharacters(username)
        remember = input(text2).lower()
    
    return username, remember

def askAccountNameTkinter(configSettings = ['accounts/', 'False', 'testaccount', '_omac'], buttonText = 'click me when you chose your name',
                            labelText = 'input your name here', exampleName = 'exampleName', text2 = 'Automatically login to this account?'):
    '''input the account name (tkinter), returns account name and if autologin is enabled'''
    import tkinter
    from tkinter import ttk
    def click():
        username = removeCharacters(nameVar.get())
        if username != '':
            window.destroy()
    autoLogin = configSettings[1]
    autoLoginName = configSettings[2]
    if autoLogin.lower() == 'true':
        username = autoLoginName
        return username, True
    else:
        window = tkinter.Tk()
        nameVar=tkinter.StringVar()
        nameVar.set(exampleName)
        tkinter.Label(window,text = labelText).grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW",columnspan=2)
        nameEntry = tkinter.Entry(window,textvariable = nameVar, font=('calibre',10,'normal'))
        nameEntry.grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW",columnspan=2)
        tkinter.Button(window, text = buttonText, command = lambda: click()).grid(column=0, row=4, ipadx=20, ipady=10, sticky="EW",columnspan=2)
        autoLoginVar=tkinter.BooleanVar()
        autoLoginVar.set(False)
        tkinter.Label(window,text = text2).grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW",columnspan=2)
        ttk.Radiobutton(window, text='Yes', value=True, variable=autoLoginVar).grid(column=0, row=3, ipadx=20, ipady=10, sticky="EW")
        ttk.Radiobutton(window, text='No', value=False, variable=autoLoginVar).grid(column=1, row=3, ipadx=20, ipady=10, sticky="EW")
        window.protocol("WM_DELETE_WINDOW", systemFunctions.on_closing)
        window.mainloop()
        username = removeCharacters(nameVar.get())
        return username, autoLoginVar.get()

def questionConsole(question = 'account doesn\'t exist, should i create it? \nIf it does exist, change the path in the systemConfig.ini'):
    '''simply asks user (console app) a question, returns True or False'''
    answer = 0
    print(f'{question} (Y/N)')
    while answer != 'y' and answer != 'n':
        answer = input().lower()
    if answer == 'y':
        return True
    else:
        return False

def questionTkinter(question = 'account doesn\'t exist, should i create it? \nIf it does exist, change the path in the systemConfig.ini', title = 'POPUP'):
    '''simply asks user (Tkinter) a question, returns True or False'''
    import tkinter
    import tkinter.messagebox
    if tkinter.messagebox.askokcancel(title, question):
        return True
    else:
        return False

def createAppData(data, appID):
    '''creates empty errays for you to use in the dicts'''
    if appID not in data['appData']:
        data['appData'][appID] = []
    if appID not in data['collectables']:
        data['collectables'][appID] = []
    if appID not in data['achievements']:
        data['achievements'][appID] = []
    return data

class defaultConfigurations:
    def defaultLoadingConsole(configSettings = ['accounts/', 'False', 'testaccount', '_omac']):
        '''The default loading system without your configuration, in the console app'''
        account, autologin = askAccountNameConsole(configSettings)
        if autologin != bool(configSettings[1]):
            configSettings = list(configSettings)
            configSettings[1] = str(autologin)
            configSettings[2] = account
            changeConfigFile(configSettings)
        if checkForAccount(account, configSettings):
            return loadAccount(account, configSettings, 'Console')
        else:
            if questionConsole():
                return createAccount(account, configSettings, 'Console')
            else:
                return False

    def defaultLoadingTkinter(configSettings : list= ['accounts/', 'False', 'testaccount', '_omac']):
        '''The default loading system without your configuration, using tkinter'''
        account, autologin = askAccountNameTkinter(configSettings)
        if str(autologin) != configSettings[1]:
            configSettings = list(configSettings)
            configSettings[1] = str(autologin)
            configSettings[2] = account
            changeConfigFile(configSettings)
        if checkForAccount(account, configSettings):
            return loadAccount(account, configSettings, 'Tkinter')
        else:
            if questionTkinter():
                return createAccount(account, configSettings, 'Tkinter')
            else:
                return False

class easy:
    def createPathIfNotThere(path):
        '''Creates the path if it doesn't exists and returns true or false'''
        import os
        if os.path.isdir(path):
            return True
        else:   
            os.mkdir(path)
            return False
    
    def addRandomNoDuplicates(list_all_items, amount_to_return : int = 1, beginList = [], ignoreExisting = True, avoidError = True):
        '''first list is a list of all items, second argument is the amount of items, third argument is the list the items get added to. 
        fourth argument ignores already existing items if True, if False, it will remove duplicates, last argument will avoid errors if nothing is left'''
        import random
        if ignoreExisting == False:
            num = 0
            while num < len(beginList):
                counter = beginList.count(beginList[num])
                if counter > 1:
                    beginList.pop(num)
                else:
                    num += 1
        num = 0
        while num < len(list_all_items):
            counter = list_all_items.count(list_all_items[num])
            if list_all_items[num] in beginList:
                list_all_items.pop(num)
            elif counter > 1:
                list_all_items.pop(num)
            else:
                num += 1
        for x in range(amount_to_return):
            if len(list_all_items) == 0 and avoidError == True:
                return beginList
            randomNumber = random.randint(0, len(list_all_items)-1)
            beginList.append(list_all_items[randomNumber])
            list_all_items.pop(randomNumber)
        return beginList
    
    def stringToAscii(seedString:str): #turns everything into ther ASCII value
        seedList = []
        for x in seedString:
            seedList.append(ord(x))#change every character into its ASCII value
        seedString = ''.join([str(elem) for elem in seedList])#add list together into string
        seed = int(seedString)
        return seed
