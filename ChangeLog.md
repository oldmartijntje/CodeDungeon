# Version 1.3.0

What has changed between version 1.2 and 1.3.1:

## consumable changes

You can now add a strength level modifier to a consumable, you can't remove the hp from a consumable, you'll have to set the HPAmount to 0

## mergables

You can run the 

```
player.merge()
``` 
to merge for example: 5 moldy_bread into 3 old_bread

## logger and replayFiles

they didn't listen to the json settings before, now thwy do 

atleast kinda, they still make empty files ¯\\_(ツ)_/¯

replay files now save a more readable\usable format

## returns

most functions show what value they will return and now return things

## spawning 

`"spawning"` in tiles, only spawning from a specific moment with these attributes:
- `"toLevel"`
- `"fromLevel"`
- `"toFloor"`
- `"fromFloor"`

## small things

readme has codeboxes

self.equipped turned into self.equippedWeapon

## customizable settings

`"startingFloor"` in the gameData.json

`movementRules` has a new feature.
You can now add floats to the movement and attack of an enemy, upon first movement it will do a random float between 0 and 1, if it's smaller than the float defined in the stats, it will get 1 extra every time.
```json
"movementRules": {
    "attackRule": "insteadOf",
    "movement": 1.9,
    "attack": 1.5
}
```

## updater

will be discontinued from older versions, it will only update from 1.3.1 upwards

## content:

- more weapons
- mimics! - an enemy
- strength potion