#Python File to make you look like a hacker, this also makes a grand screensaver

#Imports
import random
import time

#Global Varianles
randomNum = None
randomCharacters = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}","|","/","?","<",">",";",":","0","1"]
bianary = ["1","0"]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Randomy displays a bunch of symbols
def randomSymbols(timeToDisplay):
    print(f"{bcolors.OKGREEN}")
    lineNum = 0
    #x = 0
    while timeToDisplay > 0 or timeToDisplay < 0:
        print(lineNum,end=' ')
        randomNum = random.randint(1, 100)
        i = random.randint(160,220) #Change this to your screen size
        e = 1
        while e < i:
            print(random.choice(randomCharacters), end='')
            e += 1
        
        print(random.choice(randomCharacters))
        lineNum += 1
        sleepTime = random.randint(1,1000)
        sleepTime = sleepTime / 10000
        time.sleep(sleepTime)
        timeToDisplay -= 1

    main()

#Randomly displays a bunch of 1s and 0s
def randomBianary(timeToDisplay):
    print(f"{bcolors.OKGREEN}")
    lineNum = 0
    while timeToDisplay > 0 or timeToDisplay < 0:
        print(lineNum,end=' ')
        i = random.randint(230,230) #Change this to whatever size your terminal is
        e = 1
        while e < i:
            print(random.choice(bianary),end='')
            e += 1
        
        print(random.choice(bianary))
        lineNum += 1
        sleepTime = random.randint(1,1000)
        sleepTime = sleepTime / 10000
        time.sleep(sleepTime)

        timeToDisplay -= 1
    
    main()

def main():
    print(f"{bcolors.ENDC}")

    print("Symbols[0] or Bianary[1] or TimedSymbols[2] or TimedBianary[3]?")
    choice = input()
    if choice == "0":
        randomSymbols(-1)
    elif choice == "1":
        randomBianary(-1)
    elif choice == "2":
        print("Input number of lines to draw")
        timeToDisplay = int(input())
        timeToDisplay
        randomSymbols(timeToDisplay)
    elif choice == "3":
        print("Input number of lines to draw")
        timeToDisplay = int(input())
        randomBianary(timeToDisplay)
    elif choice == "":
        randomSymbols(-1)
    else:
        print("Invalid Input")
        main()

main()
