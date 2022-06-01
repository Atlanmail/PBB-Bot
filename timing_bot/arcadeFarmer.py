from pickle import TRUE
import pyautogui
import pydirectinput
import autoit
from time import sleep

DELAY_BETWEEN_COMMANDS = 1.00

def main():
    initializePyAutoGui()
    sleep(10) # countdown before program begins
    xPos,yPos = pyautogui.position()
    xPos2,yPos2 = pyautogui.position()
    print("xPos: " + str(xPos) + " yPos: " + str(yPos))
    while (True):

        xPos2,yPos2 = pyautogui.position()

        pydirectinput.moveTo(xPos, yPos)
        pydirectinput.press('e')

        pydirectinput.moveTo(xPos2,yPos2)
        sleep(1)
        xPos2,yPos2 = pyautogui.position()

        pydirectinput.click(x = xPos, y = yPos)

        pydirectinput.moveTo(xPos2,yPos2)
        sleep(1)

        ### locate 

def initializePyAutoGui():
    pyautogui.FAILSAFE = TRUE



if __name__ == "__main__":
    main()