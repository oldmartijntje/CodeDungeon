# Code Dungeon

Welcome to the troubleshooting.md

[Get me back to readme](README.md)

### Error code: 0001:

There is a tile that is inpossible to create in the map generator, it's not any of the defined numbers, nor a predefined tile, turn on logging in the [gameData.json](gameData/gameData.json) to see more details.

How to fix:

Make sure your map in [levelData.json](gameData/levelData.json) are all valid, as explained in the [readme](README.md) at 'Map Editor' explenation.

### Error code: 0002:

Something is wrong with the gameData.json

How to fix:

Delete the gameData.json, or fix it using logging.

### Error code: 0003:

Something is wrong with the level you are trying to load.

How to fix:

Try to fix the map you are loading, logging can give some helpfull information, make sure that if ur loading a dictionary that u use '//' and not 'x'
