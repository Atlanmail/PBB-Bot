from pickle import TRUE
import pyautogui
import pydirectinput
import autoit
from time import sleep

DELAY_BETWEEN_COMMANDS = 1.00

def main():
    pyautogui.FAILSAFE = TRUE

    sleep(5)
    pydirectinput.keyDown('w')
    sleep(.1)
    pydirectinput.keyDown('d')

def initializePyAutoGui():
    pyautogui.FAILSAFE = TRUE



if __name__ == "__main__":
    main()
