#Python File to make you look like a hacker, this also makes a grand screensaver

#Imports
import random
import time
#import tty
#import sys
#import termios

#orig_settings = termios.tcgetattr(sys.stdin)

#tty.setcbreak(sys.stdin)

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
def randomSymbols():
    print(f"{bcolors.OKGREEN}")
    #x = 0
    while True:
        randomNum = random.randint(1, 100)
        i = random.randint(160,240) #Change this to your screen size
        e = 1
        while e < i:
            print(random.choice(randomCharacters), end='')
            e += 1
        
        print(random.choice(randomCharacters))
        sleepTime = random.randint(1,1000)
        sleepTime = sleepTime / 10000
        time.sleep(sleepTime)

#This section is an attempt to stop when a key is pressed, I'm having trouble getting it to work though
        #if x == chr(27):
        #    x=sys.stdin.read(1)[0]
        #    break

    #main()

#Randomly displays a bunch of 1s and 0s
def randomBianary():
    print(f"{bcolors.OKGREEN}")
    while True:
        i = random.randint(240,240) #Change this to whatever size your terminal is
        e = 1
        while e < i:
            print(random.choice(bianary),end='')
            e += 1
        
        print(random.choice(bianary))
        sleepTime = random.randint(1,1000)
        sleepTime = sleepTime / 10000
        time.sleep(sleepTime)
    
    main()

def main():
    print(f"{bcolors.ENDC}")

    print("Symbols[0] or Bianary[1]?")
    choice = input()
    if choice == "0":
        randomSymbols()
    elif choice == "1":
        randomBianary()
    else:
        print("Invalid Input")
        main()

main()

#termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
