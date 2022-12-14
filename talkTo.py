import time
import random


def start():
    affinity = 0
    print('Well hello there!')
    hi = input('Hi(1) | Hello(2) | Bye(3) ')
    if(hi.isnumeric()):
        hi = int(hi)
    else:
        hi = str(hi)
    if(hi==1):
        affinity += 0.5
        print('A bit bland but that will do...')
        nextP(affinity)
    elif(hi==2):
        affinity += 1
        print('Indeed, a plesure to meet you!')
        nextP(affinity)
    elif(hi==3):
        affinity -= 1
        print('Smart alec huh')
        nextP(affinity)
    elif(hi=='hi')|(hi=='Hi')|(hi=='Hello')|(hi=='hello')|(hi=='byr')|(hi=='Bye'):
        affinity -= 0.5
        print('Do me a favor and type the number, thankssss')
        sudoStart(affinity)
    else:
        affinity -= 1
        print('That was not an option mate')
        sudoStart(affinity)

def nextP(affinity):
    print('Okay so now I will need your name :)')
    name = input('Name:')
    if(-4 <= affinity <= 0):
        print('Well hi',name,'nice to meet you')
    elif(-10 <= affinity <= -5):
        print('FINALLY.. I guess its nice to meet you',name)
    elif(-20 <= affinity <= -11):
        print('Took you long enough',name,'Maybe put the right thing in fast next time')
    elif(-50 <= affinity <= -21):
        print('Frick you',name)

def checkStart(affinity):
    hi = input('Hi(1) | Hello(2) | Bye(3) ')
    if(hi.isnumeric()):
        hi = int(hi)
    else:
        hi = str(hi)
    if(hi==1):
        affinity += 0.5
        print('A bit bland but that will do...')
        nextP(affinity)
    elif(hi==2):
        affinity += 1
        print('Indeed, a plesure to meet you!')
        nextP(affinity)
    elif(hi==3):
        affinity -= 1
        print('Smart alec huh')
        nextP(affinity)
    elif(hi=='hi')|(hi=='Hi')|(hi=='Hello')|(hi=='hello')|(hi=='byr')|(hi=='Bye'):
        affinity -= 0.5
        print('Do me a favor and type the number, thankssss')
        sudoStart(affinity)
    else:
        affinity -= 1
        print('That was not an option mate')
        sudoStart(affinity)
            
def sudoStart(affinity):
    print('|')
    if(-4 <= affinity <= 0):
        print('Come on, just do it right..')
        checkStart(affinity)
    if(-10 <= affinity <= -5):
        print('...I really do not like you, but let\'s try this again :)')
        checkStart(affinity)
    elif(-50 <= affinity <= -11):
        print('I am starting to lose faith here...')
        checkStart(affinity)
    elif(-99 <= affinity <= -51):
        print('._.')
        checkStart(affinity)
    elif(affinity <= -100):
        print('We are done here')
        exit
    else:
        checkStart(affinity)
    
    
start()
