import time
import random

def choose(maxNum,names,index):
    num = random.randint(1,maxNum+1)
    mess = ['Your mother decided that you were an inconvinence!','Your mother decided you were just a clump of cells!','Your mother thought you might be too expensive!','Your mother thought you weren\'t alive!','Your mother decided you don\'t exist!','You might have had down syndrome, so Your quality of life might not have been the best...','You didn\'t look how your mother wanted you to.','Your mother was convinced to think of herself before you!','Your parents were dating and then they broke up, your mom didn\'t want to be a single mom','Your mom wanted to focus on her career!','Your mom wanted to backpack through europe!','Kids are expensive, your mom knew that soooo.... byeeeee','Your mom didn\'t really want another kid.','Your mom doesn\'t think that fetuses are humans, so she sees nothing wrong with killing them!','Aw, your mom doesn\'t like babies :(','Your mom thought \"Well you might not have been perfectly healthy soooo, might as well kill you now.\"','Your mom isn\'t married and therfore you deserve to die','Well it isn\'t alive anyways; Thought your mom I guess...','It\'s not like I could just put it up for adoption sense I don\'t want it... Let\'s just kill it..','Your mom wanted to do more collage before starting a family','Your mom decided she didn\'t have enough time to raise children','Your mom did not want you, even though other people could have taken care of you :)','Your mom convinced herself that you weren\'t alive anyways','Your mom might have died, so you get to instead :)','Your mother wasn\'t going to survive so you will be sacrificed instead!','Your mom was a teenager, so you get to die :)','Society told your mom that she deserved better than to have to take care of you, so she killed you','Your mom didn\'t what to be a mom, so she killed you... She\'s still a mom, just a bad one and a murderer']
    if(index == 1):
        print('Number',num,'has been eleminated')
    else:
        print(names[random.randint(0,len(names)-1)],'ceased to exist')
    print(mess[random.randint(0,len(mess)-1)])

def wait(maxNum,names,index):
    time.sleep(0.55)
    print('|')
    choose(maxNum,names,index)
    
def start():
    names = ['Camden','Ben','Hannah','Atticus','Schory','Megan','Sophia','August','Angelica','Kamryn','Mason','Madison']
    numOrName = input('Names(1) or Number(2) ')
    if(numOrName=='1')|(numOrName=='names')|(numOrName=='Names'):
        index = 0
        maxNum = len(names)-1
    elif(numOrName=='2')|(numOrName=='number')|(numOrName=='Number'):
        index = 1
        maxNum = input('Number of people:')
        if(maxNum.isnumeric()):
            maxNum = round(int(maxNum))
        else:
            print('That ain\'t working bub')
            start()
    elif(numOrName == 'clear'):
        for x in range(35):
            print("|")
        start()
    else:
        print('No comprendo')
        print('|')
        start()
    print('Calculating abortions...')
    whatNum = round(0.2*maxNum)
    print(whatNum,'of you will die :)')
    for x in range(whatNum):
        wait(maxNum,names,index)
    time.sleep(0.5)
    print('|')
    print('For the rest of you, your moms put you first :) So you get to live')
    start()
start()
