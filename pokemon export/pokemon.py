from pickle import FALSE
import numpy as np
import csv


class pokemon:

    data = 'D:\Programming\Roblox\PBB Bot\pokemon export\data.csv'

    def __init__(self, id,isHA, nature, IV): # IV is an array
        self.isHA = isHA # 1 if is HA, 0 if not
        self.nature = nature
        self.IV = IV
        self.position = ["party", 2, 1] # x, y (1,1 is top left)
        self.id = id

    def writeData(self):
        with open('D:\Programming\Roblox\PBB Bot\pokemon export\data.csv', 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([self.id, self.isHA, self.nature, self.IV, self.position])

            
