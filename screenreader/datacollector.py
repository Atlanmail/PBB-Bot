from pickle import TRUE
from time import sleep
import pyautogui
import pydirectinput
import PIL
import cv2

## how this will work: open the program, create a list of coordinates to click on initially then run that loop on repeat

def main(): 
    pyautogui.FAILSAFE = TRUE
    sleep(10)
    
    x = 1
    for pos in pyautogui.locateAllOnScreen(r'C:/Users/tiep1\Documents/Programming/Python/PBBBot/PBB-Bot-1/screenreader/icons/pokemon/ditto.PNG', region=(545,219,814,696),confidence = 0.95):
        print(pos)
        print(x)
        x = x + 1


SUMMARY_XOFFSET = 140
SUMMARY_YOFFSET = -60
current_image = 0

ICONPOSITION_X = 980
ICONPOSITION_Y = 550

CLOSEPOSITION_X = 1290
CLOSEPOSITION_Y = 274

BACKPOSITION_X = 422
BACKPOSITION_Y = 528

DELAY = 3

def getData(xToClick, yToClick): # gets the data of 
    global current_image

    clickDelay(xToClick, yToClick, DELAY)
    clickDelay(xToClick + SUMMARY_XOFFSET, yToClick + SUMMARY_YOFFSET, DELAY)

    
    im1 = pyautogui.screenshot(r'C:/Users/tiep1/Documents/Programming/Python/PBBBot/PBB-Bot-1/screenreader/data/HAs/' + str(current_image) +  '.png')

    

    clickDelay(ICONPOSITION_X, ICONPOSITION_Y, DELAY)

    im2 = pyautogui.screenshot(r'C:/Users/tiep1/Documents/Programming/Python/PBBBot/PBB-Bot-1/screenreader/data/IVs/' + str(current_image) +  '.png')

    clickDelay(CLOSEPOSITION_X, CLOSEPOSITION_Y, DELAY)

    sleep(1)

    clickDelay(BACKPOSITION_X,BACKPOSITION_Y, DELAY)

    current_image = current_image + 1

def clickDelay(x,y, delay):
    pydirectinput.click(x,y)
    sleep(.2)
    pydirectinput.click(x,y)
    sleep(delay)
    

if __name__ == "__main__":
    main()