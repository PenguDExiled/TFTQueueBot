import time
import pyautogui
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller
import augmentGrabber
import getColour
import postRequest
import gameID
import tkinter as tk
import pydirectinput


def click(x,y):
    pydirectinput.moveTo(int(x), int(y))
    time.sleep(0.5)
    pydirectinput.mouseDown()
    time.sleep(0.5)
    pydirectinput.mouseUp()
    time.sleep(0.5)

def queueGame():
    print('Queueing up..')
    clicked = False
    while not clicked:
        if pyautogui.locateOnScreen('FindMatch.png', confidence =0.95) != None:
            queue = pyautogui.locateOnScreen('FindMatch.png', confidence =0.95)
            print('found it here: ' + str(queue))
            click(queue[0] + (queue[2]/2), queue[1] + (queue[3]/2))
            clicked = True
            time.sleep(0.5)
        else:
            print('cant see Find Match')
            time.sleep(0.5)


def acceptGame():
    print('Accepting...')
    clicked = False
    while not clicked:
        if pyautogui.locateOnScreen('Accept.png', confidence=0.95) != None:
            accept = pyautogui.locateOnScreen('Accept.png', confidence =0.95)
            print('found it here: ' + str(accept))
            click(accept[0] + (accept[2] / 2), accept[1] + (accept[3] / 2))
            clicked = True
            time.sleep(0.5)
        else:
            print('cant see Accept button')
            time.sleep(0.5)


def forfeitGame():
    time.sleep(3)
    print('surrendering...')
    keyboard = KeyboardController()
    clicked = False
    while not clicked:
        pydirectinput.press('esc')
        if pyautogui.locateOnScreen('forfeit.png', confidence=0.95) != None:
            surrender = pyautogui.locateOnScreen('forfeit.png', confidence=0.95)
            click(surrender[0] + (surrender[2] / 2), surrender[1] + (surrender[3] / 2))
            time.sleep(0.5)

        if pyautogui.locateOnScreen('ffbutton.png', confidence=0.95) != None:
            surrenderbutton = pyautogui.locateOnScreen('ffbutton.png', confidence=0.95)
            click(surrenderbutton[0] + (surrenderbutton[2] / 2), surrenderbutton[1] + (surrenderbutton[3] / 2))
            time.sleep(0.5)

        if pyautogui.locateOnScreen('playagain.png', confidence=0.95) != None:
            playagain = pyautogui.locateOnScreen('playagain.png', confidence=0.95)
            click(playagain[0] + (playagain[2] / 2), playagain[1] + (playagain[3] / 2))
            time.sleep(2)

        if pyautogui.locateOnScreen('FindMatch.png', confidence=0.95) != None:
            clicked = True
        else:
            time.sleep(1)
            pyautogui.moveTo(10,10)


def sellUnit(x,y):
    time.sleep(0.5)
    print('sells unit...')
    click(x,y)
    time.sleep(0.3)
    pydirectinput.keyDown('e')
    time.sleep(0.3)
    pydirectinput.keyUp('e')
    time.sleep(0.3)
    pydirectinput.moveTo(10,10)

def takeAugment(x,y):
    time.sleep(1)
    print('takes the left augment')
    click(x,y)



def gameProcessing(username):
    print('game in progress...')
    pyautogui.FAILSAFE = False
    game = gameID.random_string(6,6)
    stagecount = 1
    unitsold1 = False
    unitsold2 = False
    unitsold3 = False
    ff = False
    while stagecount < 4:
        if pyautogui.locateOnScreen('1-3.png', confidence=0.95) != None and unitsold1 == False:
            sellUnit(957,667)
            unitsold1 = True
        if pyautogui.locateOnScreen('2-5.png', confidence=0.95) != None and unitsold2 == False:
            # 415 770, 538 759, 659, 776
            sellUnit(440,776)
            sellUnit(538,759)
            sellUnit(659,776)
            unitsold2 = True
        if pyautogui.locateOnScreen('3-5.png', confidence=0.95) != None and unitsold3 == False:
            sellUnit(440,776)
            unitsold3 = True

        if pyautogui.locateOnScreen('2-1.png', confidence=0.95) != None and stagecount == 1:
            stage = '2-1'
            stagecount = stagecount + 1
            augments = augmentGrabber.imageToString()
            rarity = getColour.getPixelColour()
            time.sleep(0.5)
            print((augments, rarity, stage, username, game))
            postRequest.addData(augments[0]+', '+augments[1]+', '+augments[2], rarity, stage, username,game)
            takeAugment(546,621)
        elif pyautogui.locateOnScreen('3-2.png', confidence=0.95) != None and stagecount == 2:
            stage = '3-2'
            stagecount = stagecount + 1
            augments = augmentGrabber.imageToString()
            rarity = getColour.getPixelColour()
            time.sleep(0.5)
            print((augments, rarity, stage, username, game))
            postRequest.addData(augments[0] + ', ' + augments[1] + ', ' + augments[2], rarity, stage, username, game)
            takeAugment(546,621)
        elif pyautogui.locateOnScreen('4-2.png', confidence=0.95) != None and stagecount == 3:
            stage = '4-2'
            stagecount = stagecount + 1
            augments = augmentGrabber.imageToString()
            rarity = getColour.getPixelColour()
            time.sleep(0.5)
            print((augments, rarity, stage, username, game))
            postRequest.addData(augments[0] + ', ' + augments[1] + ', ' + augments[2], rarity, stage, username, game)
            takeAugment(546,621)
    while not ff:
        if pyautogui.locateOnScreen('4-3.png', confidence=0.95) != None:
            forfeitGame()
            ff = True


def runAll(username):
    p_username = username
    run = True
    counter = 0
    while run is True:
        counter = counter + 1
        print('New Game! Game number: ' + str(counter))
        queueGame()
        time.sleep(1)
        acceptGame()
        time.sleep(1)
        gameProcessing(p_username)
    print(counter)


def main():
    root = tk.Tk()
    apps = []
    root.title("Augment Reader")

    def b_run():
        runAll(username.get())



    canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="black")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    UItext = tk.Label(frame, text=
    """READ ME!
    What does it do?:
    It queues up, sells all carousel units, recognizes when augments are on screen
    --> reads them and sends them to a database. --> repeat
    
    Step 1: Choose a normal Map - with no animations or anything else!
    Step 2: Make sure your settings are:
    Fullscreen mode (Windowed-Fullscreen should work too)
    resolution: 1920x1080 (other might not work!)
    Also: Put the game on your main screen.
    Step 3: Go up on PBE and click on TFT -> 1v0 Mode -> confirm.
    From now on the Bot should do all on 
    itself. It just has to see the "Find Game" Button.
    
    Reminder: Please do not interrupt with the Bot... 
    I tried to make sure that you can use your Pc most of the time,
    but it may cause errors
    or it could be stuck in a loop and won't continue. So best case -
    use it if you don't use your Mouse or PC at all.
    If the program has no respone - don't worry, it still works!!
    To close it, just close the CMD.
    
    PS: Start as admin!!!
    
    Last Step: Please enter your username below,
    for database purposes. 
    
    
    
    
    
    Username:
    """)
    UItext.pack()
    username = tk.Entry(frame, width=50)
    username.pack()

    run = tk.Button(root, text="Run", padx=10, pady=5, fg="white", bg="#263D42", command=b_run)

    run.pack()

    root.mainloop()


if __name__ == '__main__':
    print("Running...")
    main()