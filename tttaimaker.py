import random
import pandas as pd
from pandas.core import indexing, series
import sys
sys.setrecursionlimit(2000)

n = 0
boxes = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]"]
markedboxes = []
winner = None

def mainscreen():
    while len(markedboxes) < 9 and winner == None:
        s = random.randint(0,8)
        if s in markedboxes:
            pass
        else:
            markedboxes.append(s)
            boxes.pop(s)
            if len(markedboxes)%2 == 0:
                x = "[X]"
            else:
                x = "[O]"
            boxes.insert(s,x)
            gamecomplete =  winchecker()
            if gamecomplete:
                winannoucer(gamecomplete)


def winchecker():
    for i in range(0,7,3):
        if boxes[i] == "[O]" and boxes[i+1] == "[O]" and boxes[i+2] == "[O]":
            return 1
        elif boxes[i] == "[X]" and boxes[i+1] == "[X]" and boxes[i+2] == "[X]":
            return 2

    for i in range(0,3):
        if boxes[i] == "[O]" and boxes[i+3] == "[O]" and boxes[i+6] == "[O]":
            return 1
        elif boxes[i] == "[X]" and boxes[i+3] == "[X]" and boxes[i+6] == "[X]":
            return 2
        
    if boxes[0] == "[O]" and boxes[4] == "[O]" and boxes[8] == "[O]":
        return 1
    elif boxes[0] == "[X]" and boxes[4] == "[X]" and boxes[8] == "[x]":
        return 2
    elif boxes[2] == "[X]" and boxes[4] == "[X]" and boxes[6] == "[X]":
        return 2
    elif boxes[2] == "[O]" and boxes[4] == "[O]" and boxes[6] == "[O]":
        return 1
    elif len(markedboxes) == 9:
        return 3
    
    return 0

dbseries =[]
def winannoucer(s):
    global winner
    global dbseries
    global dict
    winner = s 
    if s == 1 or 2 or 3:
        mergedtttdata= ''.join([str(item) for item in markedboxes])
        if len(mergedtttdata) == 9:
            reboot()
        else:
            dbseries.append(mergedtttdata)
            reboot()
        print(mergedtttdata)
       

        
def reboot():
    if len(dbseries) < 300:
        global boxes
        global winner
        markedboxes.clear()
        boxes = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]"]
        winner = None
        mainscreen()
    else:
        dota = pd.Series(dbseries)
        dota.to_csv(r'C:\Users\KRITESH OJHA\Desktop\SICSR CODES\pythn\tttdata.csv', index=False)
mainscreen()