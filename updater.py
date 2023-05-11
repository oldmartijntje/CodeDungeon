import json
import os
import CodeDungeon

versionByNumber = {
    1: 'V1.3.0',
    2: 'V1.3.2',
}

if os.path.exists(f'gameData/gameData.json'):
    gameData = open("gameData/gameData.json", "r")
    gameDataText = gameData.read()
    gameData.close()
    player = CodeDungeon.System()
  
while player.dataDict['version']['number'] < 1:
    bigLoop = True
    print('Error: gameData.json doesn not have a valid version number, it\'s not possible to update this file properly.')
    while bigLoop:
        print('These are the following options: \n    1. exit the updater\n    2. fix the version number manually\n    3. set the version number to version V1.3.0 (may cause errors)\n    4. Input the corrrect version (only use this if you know the version)\n    5. delete the gameData.json file and start over.')
        options = ['1', '2', '3', '4', 'exit', '5']
        answer = input('what do you want to do? >>>')
        if answer not in options:
            print('Error: invalid option')
        elif answer == '1' or answer == 'exit':
            player.exit()
        elif answer == '2':
            input('Click on \'enter\' key once to get information on ho to do this, press it twice to exit.')
            print("""
            1. open the gameData.json file
            2. find the version number
            3. change the version number to the number corresponding to the version it is made with.
            4. save the file

            or

            1.reopen the updater.py file
            2. choose option 4 to set the version number.
            
            If you don't know what version it is, try to run player.getCurrentVersion() in the example.py file.
            This will tell you the version number and the version name of the application you are using.
            if you haven't updated the game after changing the gameData.json, this should be the number.
            
            If player.getCurrentVersion() gives you an error, you are using V1.3.0 or lower.
            That would mean that you have to set the version number to 1.""")
            input('Press enter to exit.')
            player.exit()
        elif answer == '3':
            player.dataDict['version']['number'] = 1
            player.dataDict['version']['name'] = 'Version 1.3.0'
            bigLoop = False
            print('version number set to 1 AKA V1.3.0\nDo you want to update to the newest version now? (y/n)')
            answer = input('>>>')
            if answer.lower() != 'y':
                print('exiting...')
                player.exit()
            else:
                print('updating to newest version...')
        elif answer == '4':
            loop = True
            while loop:
                number = input('Input the version number >>>')
                if number.isnumeric():
                    player.dataDict['version']['number'] = int(number)
                    if int(number) in versionByNumber:
                        player.dataDict['version']['name'] = versionByNumber[int(number)]
                    loop = False
                else:
                    print('Error: invalid input')
                    print('Input a number, as in \'1\', \'2\', \'3\', \'4\', \'5\', etc.')
            bigLoop = False
        elif answer == '5':
            deleteAnswer = input('are you sure you want to delete the gameData.json file? (y/n) >>>')
            if deleteAnswer.lower() == 'y':
                os.remove('gameData/gameData.json')
                player.exit()
            else:
                print('gameData.json not deleted')
if player.dataDict['version']['number'] == 1:
    for tile in list(player.dataDict['tiles'].keys()):
        if 'mergable' in player.dataDict['tiles'][tile]:
            if 'loot' in player.dataDict['tiles'][tile]:
                player.dataDict['tiles'][tile]['loot']['mergable'] = player.dataDict['tiles'][tile]['mergable']
            else:
                player.dataDict['tiles'][tile]['loot'] = {'mergable': player.dataDict['tiles'][tile]['mergable']}
            del player.dataDict['tiles'][tile]['mergable']
    if 'startingFloor' not in player.dataDict['dungeon']:
        player.dataDict['dungeon']['startingFloor'] = 1
    player.dataDict['version']['number'] = 2
    player.dataDict['version']['name'] = 'Version 1.3.2'
    print('updated changes to version 2 AKA V1.3.2')
        
  

player.updateGameDataDict()

print('gameData.json updated successfully')

player.exit()