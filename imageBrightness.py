from PIL import Image, ImageTk, ImageEnhance
e = ['black','exit','floor','sign','wall','player left','player right','npc','enemy','loot']
for x in range(len(e)):
    im = Image.open(f'sprites/{e[x]}.png')
    enhancer = ImageEnhance.Brightness(im.convert('RGB'))
    enhanced_im = enhancer.enhance(0.5)
    enhanced_im.save(f'sprites/{e[x]}_dark.png')