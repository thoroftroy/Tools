import random
import time


def characterCreation():
    colorList = ['red','orange','yellow','green','blue','purple', 'pink','brown','black','gray','white','Red','Orange','Yellow','Green','Blue','Purple', 'Pink','Brown','Black','Gray','White']
    print('Hello there')
    name = input('What is your name? ')
    favFood = input('What is your favorite food? ')
    favColor = input('What is your favorite color? ')
    if(favColor in colorList):
        favColor = favColor
    else:
        favColor = random.choice(colorList)
        print('...How about',favColor,'instead :)')
    lFavColor = input('What is your least favorite color? ')
    if(lFavColor in colorList):
        lFavColor = lFavColor
    else:
        lFavColor = random.choice(colorList)
        print('...How about',lFavColor,'instead :)')
    if(favColor == lFavColor):
        print('..But those are the same color')
        time.sleep(0.5)
        print('Oh well, moving on')
    else:
        print('Alrighty Let\'s get on with this')
    print('So just to confirm... Here is what you told me :)')
    time.sleep(0.2)
    print('Name:',name)
    time.sleep(0.5)
    print('Favorite Food:',favFood)
    time.sleep(0.5)
    print('Favorite Color:',favColor)
    time.sleep(0.5)
    print('Least Favorite Color:',lFavColor)
    time.sleep(0.7)
    if(favColor == lFavColor):
        print('...Even though your least and favorite colors are the same')
    else:
        print('I think that\'s right...')
    conf = input('Is all that correct? ')
    if(conf=='no')|(conf=='No'):
        print('alrightttttt... Let\'s do this again then')
        characterCreation()
    else:
        print('Let\'s move on then..')

def main():
    characterCreation()
    
main()
