# -*- coding: utf-8 -*-
import statssave
import random
import os

currentPlayer = ""

def getword():
    wordfile = open('dict.txt', 'r')
    lines = wordfile.readlines()
    for line in lines:
      line = line.rstrip()
    return random.choice(lines)
def drawHangman(hangmanerrors, word, guesses):
    os.system("clear")
    hangmanerrors = 0
    newword = ""

    guessnum = len(guesses)
    badguesses = guessnum
    for i in range(len(word)):
        if word[i] in guesses:
            newword += word[i]
            badguesses -= 1
        else:
            newword += "_"
    if badguesses == 7:
        statssave.addPlayerGame(currentPlayer, False)
        MenuScreen()
        return
    if newword == word:
        statssave.addPlayerGame(currentPlayer, True)
        MenuScreen()
        return
    print(str(badguesses) + "/6 wrong characters")
    print(newword)
def statsMenu():
    pname = currentPlayer
    playerstats = statssave.getPlayer(pname)
    for key in playerstats:
        print(str(key) + " : " + str(playerstats[key]))
    input("Press enter to continue")
    MenuScreen()
    return
def createPlayerMenu():
    pname = input("New player name: ")
    global currentPlayer
    if statssave.addPlayer(pname):

        print("player " + pname + " created!")
        currentPlayer = pname
        MenuScreen()
    else:
        print ("player " + pname + " already exists")
        createPlayerMenu()
    
def playerPicker():
    os.system("clear")
    playerin = input("input player name: \n")
    return playerin
def MenuScreen():
    global currentPlayer
    os.system("clear")
    print("Current Player is: " + currentPlayer)

    menuinput = input("play(p), quit(q), playerstats(s), createplayer(c): \n")
    if menuinput == "p":
        if (currentPlayer == ""):
            currentPlayer = playerPicker()
            print (currentPlayer)
            input("press")
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
        print("Please only type one letter!")
        return getInput()

def gameLoop():
    guesses2 = ""
    gameword = getword()
    gameword = gameword.strip()

    while(True):
        drawHangman(0,gameword, guesses2)
        guesses2 += getInput()

def saveData(playa):
    statssave.updatePlayer(playa, 100, 1,1)
    return
MenuScreen()
