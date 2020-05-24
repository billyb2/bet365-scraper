from bet365 import *
from playsound import playsound
import time
import sys
import os


def removekey(d, key):
    r = d
    del r[key]
    return r

playersNotToBeepFor = []

while True:
    os.system('cls')
    data = get_odds_data("Table Tennis", True)
    newData = data
    foundInBetween = False


    if data is not None:
        #Removes players with the string SP
        for players in data:
            if data[players] == 'SP':
                newData = removekey(data, players)

        for players in newData:
            if 1.05 <= float(newData[players]) <= 1.1:
                print(players + ": " + newData[players])
                foundInBetween = True
                # Thank you to qubodup
                # https://freesound.org/people/qubodup/sounds/443026/
                if players not in playersNotToBeepFor:
                    playsound("beep.wav")
                    playersNotToBeepFor.append(players)

        if not foundInBetween:
            print("No players have odds between 1.05 and 1.1, waiting 30 seconds...")

        data = newData
        time.sleep(30)


    else:
        print('No table tennis games!')
        break


