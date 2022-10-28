import time
import pyautogui

"""
Colour recognition for augment rarity.
"""

def getPixelColour():
    time.sleep(4)
    pic = pyautogui.screenshot(region=(486, 375, 614, 498))
    width, height = pic.size
    augmentList = ['']
    for x in range(0,width,5):
        for y in range(0, height, 5):

            r,g,b = pic.getpixel((x,y))

            if r in range(100,114) and g in range(120,134) and b in range(146,160):
                augmentList.append('silver')
            elif r in range(209, 223) and g in range(161, 175) and b in range(14, 28):
                augmentList.append('gold')
            elif r in range(190, 240) and g in range(140, 180) and b in range(200,255):
                augmentList.append('prismatic')
    if len(augmentList) == 0:
        augmentList.append('empty!')
    return max(set(augmentList), key=augmentList.count)
#107,127,153
#216, 168, 21
#rgba(224,158,255,255)
# 486 375 614 498
