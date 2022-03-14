import random
boxes = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]"]
markedboxes = []
winner = None

def screen():
    print("""->WELCOME TO Tic Tak Toe<-       TURN:""",len(markedboxes),"""
                """,boxes[0],boxes[1],boxes[2],"""
                """,boxes[3],boxes[4],boxes[5],"""
                """,boxes[6],boxes[7],boxes[8],"""
""")
def mainscreen():
    while len(markedboxes) < 9 and winner == None:
        screen()
        if len(markedboxes)%2 == 0:
            print("Player 1, MARK[O]")
        else:
            print("Player 2, MARK[X]")

        s = int(input("WHICH PLACE YOU WANNA MARK?"))
        #s = random.randint(0,8)
        #print(s)
        markingsign(s-1)
    

    

def markingsign(s):
    if s in markedboxes:
        print("This space is already marked, please mark other space")
        mainscreen()
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

def winannoucer(s):
    global winner
    if s == 1:
        print("PLayer 1 WON Congo!!")
    elif s == 2:
        print("PLayer 2 WON")
    elif s == 3:
        print("OwO, Seems like all places are filled now!!")
    winner = s


mainscreen()