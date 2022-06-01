from pickle import TRUE
import pyautogui
import csv
from pokemon import pokemon


def main():

    scorbunny = pokemon(51, 1, 'Sassy', [31,31,31,31,31,31])

    scorbunny.writeData()



if __name__ == "__main__":
    main()