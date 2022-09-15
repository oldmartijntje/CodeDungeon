import CodeDungeon
import random
player = CodeDungeon.System(random.randint(0,1000))

print('calculating....')
results = {}
for rarity in player.rarityList:
  results[rarity] = 0
for x in range(1000):
  results[player.itemRarity()] += 1

print(results)
input('press space to exit')
player.exit()