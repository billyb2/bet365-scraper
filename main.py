from scrape import *
import time
import sys
import os


def removekey(d, key):
    r = d
    del r[key]
    return r


while True:
    os.system('cls')
    data = get_data("Table Tennis", False)
    newData = data
    foundInBetween = False

    if data is not None:
        #Removes players with the string SP
        for players in data:
            if data[players] == 'SP':
                print(data)
                newData = removekey(data, players)

        for players in newData:
            if 1.05 <= float(newData[players]) <= 1.1:
                print(players + ": " + newData[players])
                foundInBetween = True

        if not foundInBetween:
            print("No players have odds between 1.05 and 1.1, waiting 30 seconds...")

        data = newData
        time.sleep(30)


    else:
        print('No table tennis games!')
        break


