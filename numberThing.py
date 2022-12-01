import time
import random

maxNum = 'null'
i = 'null'

def start():
    print('Only input positive whole numbers')
    i = 0
    maxNum = input('Max num: ')
    if(maxNum.isnumeric()):
        maxNum = int(maxNum)
        if(maxNum > 1000):
            print('That\'s a little too big...')
            start()
        else:
            run(maxNum,i)
    else:
        print('That doesn\'t work')
        start()
        
def run(maxNum,i):
    while i < maxNum:
        print('i =',i)
        i += random.randint(-6,7)
        time.sleep(0.05)
    end(maxNum,i)

def end(maxNum,i):
    i = maxNum
    print('i =',maxNum)
    start()
start()
