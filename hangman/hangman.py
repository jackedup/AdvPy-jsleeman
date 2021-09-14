# -*- coding: utf-8 -*-
import statssave
import random
def getword():
    wordfile = open('dict.txt', 'r')
    lines = wordfile.readlines()
    for line in lines:
      line = line.rstrip()
    return random.choice(lines)
def drawHangman(hangmanerrors, word, guesses):
    newword = ""
#     """ """ print("""
#                      ┌───────────────────────┐
#                      │                       │
#                      │                       │
#                      │                       │
#                    xxxx                      │
#                   x    x                     │
#                   x    x                     │
#                    xxxx                      │
#                     x                        │
#                xxxxxxxxxxxxx                 │
#             xxxx    x      xx                │
#            xx       x                        │
#                     x                        │
#                    xx                      xx│
#                  xxx xx                    xx│
#                 xx    xxx                xxxx│
#                 x       x               xxx  │
#                                        xx    │
#                                       xx     │
#                                      xx      │
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""") 
#     """ """
    for i in range(len(word)):
        if word[i] in guesses:
            newword += word[i]
        else:
            newword += "_"
    if newword == word:
        print("You Won!")
        statssave.addPlayerGame(playerPicker(), True)
        quit()
    print(": errors")
    print(newword)
def statsMenu():
    print(statsMenu)
    return
def createPlayerMenu():
    pname = input("New player name: ")
    if statssave.addPlayer(pname):
        print("player " + pname + " created!")
        MenuScreen()
    else:
        print ("player " + pname + " already exists")
        createPlayerMenu()
    
def playerPicker():
    playerin = input("input player name: \n")
    return playerin
def MenuScreen():
    menuinput = input("play(p), quit(q), playerstats(s), createplayer(c): \n")
    if menuinput == "p":
        gameLoop()
        return
    elif menuinput == "q":
        quit()
        return
    elif menuinput == "s":
        statsMenu()
        return
    elif menuinput == "c":
        createPlayerMenu()
        return
    else:
        MenuScreen()
    return
def getInput():
    input2 = input('input a letter:  \n')
    if len(input2) == 1:
        return input2
    else:
        return getInput()

def gameLoop():
    guesses2 = ""
    gameword = getword()
    gameword = gameword.strip()

    print(gameword)
    while(True):
        drawHangman(0,gameword, guesses2)
        guesses2 += getInput()

def saveData(playa):
    statssave.updatePlayer(playa, 100, 1,1)
    return
MenuScreen()
