# Version 1.3.0

What has changed between version 1.2.0 and 1.3.0:

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

## small things

readme has codeboxes

self.equipped turned into self.equippedWeapon