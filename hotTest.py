#program to tell you if you are beutiful
import time
import random

def areYou():
    print('So you want to know if you are hot?')
    are = input('Yes(1) or No(2) ')
    if(are == 'Yes')|(are == 'yes')|(are == 'y')|(are == '1'):
        print('Well let\'s find out then..')
        randomizeHot()
    else:
        print('...')
        time.sleep(1)
        why = input('Then why are you here??? ')
        print('bye')
        exit

def randomizeHot():
    points = 0
    time.sleep(0.75)
    print('First fill out this questionair...')
    print('Answer each quesiton with A B C etc or a number if prompted')
    time.sleep(0.75)
    print('What color of hair do you have? ')
    hairColor = input('A. Black | B. Blonde | C. Red | D. Brown | E. Dyed | F. Other ')
    if(hairColor == 'A')|(hairColor == 'a'):
        points += 5
    elif(hairColor == 'B')|(hairColor == 'b'):
        points += 3
    elif(hairColor == 'C')|(hairColor == 'c'):
        points += 7
    elif(hairColor == 'D')|(hairColor == 'd'):
        points += 4
    elif(hairColor == 'E')|(hairColor == 'e'):
        points += 8
    elif(hairColor == 'F')|(hairColor == 'f'):
        points += 9
    else:
        print('...That wasn\'t an option')
        points -= 10
    time.sleep(0.25)
    print('|')
    hairLength = input('How long is your hair (in terms of % football fields (ex: 2% of football fields[only type the number])) ')
    if(hairLength.isdigit()):
        points += 2
    else:
        print('....That wasn\'t a number buddy')
        points -= 10
    time.sleep(0.25)
    print('|')
    print('What style of hair do you consider yourself to have? (what option fits best)')
    hairStyle = input('A. Bedhead | B. Bangs | C. Short | D. Long and Flowing | E. Curly | F. Afro | G. Other | H. Bald ')
    if(hairStyle == 'A')|(hairStyle == 'a'):
        points -= 3
    elif(hairStyle == 'B')|(hairStyle == 'b'):
        points -= 6
    elif(hairStyle == 'C')|(hairStyle == 'c'):
        points += 3
    elif(hairStyle == 'D')|(hairStyle == 'd'):
        points += 4
    elif(hairStyle == 'E')|(hairStyle == 'e'):
        points += 8
    elif(hairStyle == 'F')|(hairStyle == 'f'):
        points += 9
    elif(hairStyle == 'G')|(hairStyle == 'g'):
        points += random.randint(1,12)
    elif(hairStyle == 'H')|(hairStyle == 'h'):
        points += 7
    else:
        print('...That wasn\'t an option')
        points -= 10
    time.sleep(0.25)
    print('|')
    print('What color of eyes do you have? ')
    eyeColor = input('A. Blue | B. Brown | C. Green | D. Red | E. Other ')
    if(eyeColor == 'A')|(eyeColor == 'a'):
        points += 4
    elif(eyeColor == 'B')|(eyeColor == 'b'):
        points += 2
    elif(eyeColor == 'C')|(eyeColor == 'c'):
        points += 7
    elif(eyeColor == 'D')|(eyeColor == 'd'):
        points += 7
    elif(eyeColor == 'E')|(eyeColor == 'e'):
        points += random.randint(1,6)
    else:
        print('...That wasn\'t an option')
        points -= 10
    time.sleep(0.25)
    print('|')
    print('What shape/size of eyes do you have? ')
    eyeShape = input('A. Round | B. Small | C. Large | D. Thin | E. Other ')
    if(eyeShape == 'A')|(eyeShape == 'a'):
        points += 4
    elif(eyeShape == 'B')|(eyeShape == 'b'):
        points += 2
    elif(eyeShape == 'C')|(eyeShape == 'c'):
        points += 7
    elif(eyeShape == 'D')|(eyeShape == 'd'):
        points += 7
    elif(eyeShape == 'E')|(eyeShape == 'e'):
        points += random.randint(1,6)
    else:
        print('...That wasn\'t an option')
        points -= 10
    time.sleep(0.25)
    print('|')
    height = input('What is your height in inches? (ex: 72in=6ft) ')
    if(height.isdigit()):
        height = int(height)
        if(height >= 70):
            points += 6
        else:
            points += 3
    else:
        print('....That wasn\'t a number buddy')
        points -= 10
    time.sleep(0.25)
    print('|')
    print('What color of skin do you have? ')
    skinColor = input('A. White | B. Tan | C. Brown | D. Black | E. Red | F. Yellow | G. Other ')
    points += 10
    time.sleep(0.25)
    print('|')
    print('What is your gender?')
    gender = input('A. Male | B. Female | C. Other? ')
    if(gender == 'C')|(gender == 'c'):
        points -= 20
    else:
        points += 4
    time.sleep(0.25)
    print('|')
    howSleep = input('How many hours do you generally sleep a night? ')
    if(howSleep.isdigit()):
        howSleep = int(howSleep)
        if(howSleep > 4):
            points += 6
        else:
            points += 3
    else:
        print('....That wasn\'t a number buddy')
        points -= 10
    time.sleep(0.25)
    print('|')
    print('Do you think that you are hot? ')
    isHot = input('A. Yes | B. No ')
    if(isHot == 'A')|(isHot == 'a'):
        points += 10
    elif(isHot == 'B')|(isHot == 'b'):
        points -= 10
    else:
        print('Not an option mannnn...')
        points -= 10
    time.sleep(0.25)
    print('|')
    print('Do you like cheese? ')
    likeCheese = input('A. Yes | B. No ')
    if(isHot == 'A')|(isHot == 'a'):
        points += 10
    elif(isHot == 'B')|(isHot == 'b'):
        points -= 10
    else:
        print('Not an option mannnn...')
        points -= 10
    time.sleep(0.25)
    print('|')
    print('What is your favorite animal? ')
    taco = input('A. Taco ')
    if(isHot == 'A')|(isHot == 'a'):
        points += 100
    else:
        print('Not an option mannnn...')
        points -= 100
    count = random.randint(3,10)
    hotCalc(points,count)

def hotCalc(points,count):
    print('Calculating Hottness...')
    while count < 10:
        time.sleep(1)
        print('...')
        count += 1
        hotCalc(points,count)
    print('Done!')
    time.sleep(0.5)
    print(points,'Total Points')
    print('|')
    print('|')
    print('|')
    print('|')
    if(points > 110):
        print('You are hot!')
    else:
        print('Ugly.. Very Ugly')
    print('|')
    print('|')
    print('|')
    print('|')
    areYou()
    
areYou()
