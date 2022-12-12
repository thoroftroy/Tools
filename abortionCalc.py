import time
import random

def choose(maxNum):
    num = random.randint(1,maxNum+1)
    print('Number',num,'has been eleminated')
    mess = ['Your mother decided that you were an inconvinence!','Your mother decided you were just a clump of cells!','Your mother thought you might be too expensive!','Your mother thought you weren\'t alive!','Your mother decided you don\'t exist!','You might have had down syndrome, so Your quality of life might not have been the best...','You didn\'t look how your mother wanted you to.','Your mother was convinced to think of herself before you!','Your parents were dating and then they broke up, your mom didn\'t want to be a single mom','Your mom wanted to focus on her career!','Your mom wanted to backpack through europe!','Kids are expensive, your mom knew that soooo.... byeeeee','Your mom didn\'t really want another kid.','Your mom doesn\'t think that fetuses are humans, so she sees nothing wrong with killing them!','Aw, your mom doesn\'t like babies :(','Your mom thought \"Well you might not have been perfectly healthy soooo, might as well kill you now.\"','Your mom isn\'t married and therfore you deserve to die','Well it isn\'t alive anyways; Thought your mom I guess...','It\'s not like I could just put it up for adoption sense I don\'t want it... Let\'s just kill it..','Your mom wanted to do more collage before starting a family','Your mom decided she didn\'t have enough time to raise children','Your mom did not want you, even though other people could have taken care of you :)','Your mom convinced herself that you weren\'t alive anyways']
    print(mess[random.randint(0,len(mess)-1)])

def wait(maxNum):
    time.sleep(0.25)
    print('|')
    choose(maxNum)
    
def start():
    maxNum = int(input('Number of people:'))
    print('Calculating abortions...')
    whatNum = round(0.2*maxNum)
    print(whatNum,'of you will die :)')
    for x in range(whatNum):
        wait(maxNum)
    time.sleep(0.5)
    print('|')
    print('For the rest of you, your moms put you first :) So you get to live')
        
start()
