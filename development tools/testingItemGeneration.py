import CodeDungeon
import random
player = CodeDungeon.System(random.randint(0,1000))

def addItem(dictionaaary, item, amount):
  if item in dictionaaary:
    dictionaaary[item] += amount
  else:
    dictionaaary[item] = amount
  return dictionaaary

print('calculating....')
items = {}
for x in range(1000):
  item = player.getLoot()
  if item == "NONE":
    items = addItem(items, "nothing", 1)
  else:
    items = addItem(items, item['type'], item['amount'])

print(items)
input('press space to exit')
player.exit()