import time
import random

def choose(maxNum):
    num = random.randint(1,maxNum+1)
    print('Number',num,'has been eleminated')
    mess = ['Your mother decided that you were an inconvinence!','Your mother decided you were just a clump of cells!','Your mother thought you might be too expensive!','Your mother thought you weren\'t alive!','Your mother decided you don\'t exist!','You might have had down syndrome, so Your quality of life might not have been the best...','You didn\'t look how your mother wanted you to.','Your mother was convinced to think of herself before you!','Your parents were dating and then they broke up, your mom didn\'t want to be a single mom','Your mom wanted to focus on her career!','Your mom wanted to backpack through europe!','Kids are expensive, your mom knew that soooo.... byeeeee','Your mom didn\'t really want another kid.','Your mom doesn\'t think that fetuses are humans, so she sees nothing wrong with killing them!']
    print(mess[random.randint(0,len(mess)-1)])

def wait(maxNum):
    time.sleep(1)
    print('|')
    choose(maxNum)
    
def start():
    maxNum = int(input('Number of people:'))
    print('Calculating abortions...')
    if(maxNum > 10):
        wait(maxNum)
        wait(maxNum)
    else:
        wait(maxNum)
    time.sleep(0.5)
    print('|')
    print('For the rest of you, your moms put you first :) So you get to live')
        
start()
