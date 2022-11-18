#Fun quiz thing
import time
import random
points = 'null'
fake = 'null'

def start():
    fake = 0
    points = 0
    print('|')
    print('|')
    print('Welcome to the QUIZZ')
    print('|')
    print('|')
    time.sleep(0.75)
    print('What quiz would you like to take?')
    chooseQuiz = input('Personality(1) | Hottness(2) | ')
    if(chooseQuiz == '1')|(chooseQuiz == 'Peronality')|(chooseQuiz == 'personality'):
        personalityQuiz(fake,points)
    elif(chooseQuiz == '1')|(chooseQuiz == 'Hottness')|(chooseQuiz == 'hotness'):
        hotnessQuiz(fake,points)
    else:
        print('No comprendo, start over')
        start()

def personalityQuiz(fake,points):
    time.sleep(0.75)
    print('Answer each question with A,B,C,D, etc')
    print('|')
    #Question 1, cheese
    time.sleep(0.25)
    print('|')
    print('Question 1: Do you like cheese? ')
    cheese = input('A:Yes | B:No | C:Maybe | D:CHEESEEE | E:Taco ')
    if(cheese == 'a')|(cheese == 'A'):
        print('Good')
        points += 10
    elif(cheese == 'b')|(cheese == 'B'):
        print('oh')
        points -= 10
    elif(cheese == 'c')|(cheese == 'C'):
        print('Well that\'s alright I suppose...')
        points += 5
    elif(cheese == 'd')|(cheese == 'D'):
        print('TACOOOO')
        points += 10
    else:
        print('Try answering with one of the answers next time :)')
        fake += 1
    #Question 2, favorite animal
    time.sleep(0.25)
    print('|')
    print('Question 2: Which of these is your favorite pet? ')
    animal = input('A:Cat | B:Dog | C:Bird | D:Snake | E:Fish | F:Taco ')
    if(animal == 'a')|(animal == 'A'):
        print('Sounds like you are a cool cat ;)')
        points += 10
    elif(animal == 'b')|(animal == 'B'):
        print('Dogs are super loyal')
        points += 10
    elif(animal == 'c')|(animal == 'C'):
        print('Fly little birdie wooo... NO NOT INTO THE FAN')
        points += 15
    elif(animal == 'd')|(animal == 'D'):
        print('Danger noodle')
        points += 15
    elif(animal == 'e')|(animal == 'E'):
        print('well you probably have the memory of one too..')
        points -= 10
    elif(animal == 'f')|(animal == 'F'):
        print('TACOOOOO')
        points += 15
    else:
        if(fake == 0):
            print('Try answering with one of the answers next time :)')
        elif(fake == 1):
            print('Seriosly, just type one of the options')
        fake += 1
    #Question 3, color
    time.sleep(0.25)
    print('|')
    print('Question 3: Which of these is your favorite color? ')
    color = input('A:Red | B:Blue | C:Green | D:Yellow | E:Purple | F:Pink | G:Brown | H:White | I:Black | J:Gray | K:Cyan | L:Orange | M:Taco ')
    if(color == 'a')|(color == 'A'):
        print('BLOOD FOR THE BLOOD GOD')
        points += 10
    elif(color == 'b')|(color == 'B'):
        print('Cool blueee')
        points += 10
    elif(color == 'c')|(color == 'C'):
        print('Some nice nature green')
        points += 10
    elif(color == 'd')|(color == 'D'):
        print('Ew pee')
        points -= 10
    elif(color == 'e')|(color == 'E'):
        print('Purple is just so epic')
        points += 15
    elif(color == 'f')|(color == 'F'):
        print('Ooooo pinkyyy')
        points += 15
    elif(color == 'g')|(color == 'G'):
        print('Like poop? Ew')
        points -= 15
    elif(color == 'h')|(color == 'H'):
        print('Meh kinda bland')
        points += 5
    elif(color == 'i')|(color == 'I'):
        print('r/foundTheEmo')
        points -= 5
    elif(color == 'j')|(color == 'J'):
        print('Gray..? Could you be more boring??')
        points -= 25
    elif(color == 'k')|(color == 'K'):
        print('The even cooler blue ;)')
        points += 15
    elif(color == 'l')|(color == 'L'):
        print('To each their own I guess...')
        points -= 5
    elif(color == 'm')|(color == 'M'):
        print('TACOOOO')
        points += 20
    else:
        if(fake == 0):
            print('Try answering with one of the answers next time :)')
        elif(fake == 1):
            print('Seriosly, just type one of the options')
        elif(fake == 2):
            print('...Are you doing this to annoy me?')
        fake += 1
    #Question 4, food
    time.sleep(0.25)
    print('|')
    print('Question 4: Which of these is your favorite food? ')
    food = input('A:Pizza | B:French Fries | C:French People | D:Burger | E:Potato | F:Egg | G:White Baby Hands | H:Curry | I:Beans | J:Uranium 235   | K:Apple Pie | L:Fried Chicken | M:Sandwich  ')
    if(food == 'a')|(food == 'A'):
        print('Valid answer')
        points += 10
    elif(food == 'b')|(food == 'B'):
        print('Salty')
        points += 5
    elif(food == 'c')|(food == 'C'):
        print('FINALLY SOMEONE GETS ME')
        points += 25
    elif(food == 'd')|(food == 'D'):
        print('Borgur')
        points += 10
    elif(food == 'e')|(food == 'E'):
        print('r/foundTheIdahoDude')
        points += 10
    elif(food == 'f')|(food == 'F'):
        print('Greg was a good son ;\')')
        points += 15
    elif(food == 'g')|(food == 'G'):
        print('Based')
        points += 15
    elif(food == 'h')|(food == 'H'):
        print('Someone likes da spice')
        points += 10
    elif(food == 'i')|(food == 'I'):
        print('Beans beans the magical fruit, the more you eat the more you toot')
        points += 10
    elif(food == 'j')|(food == 'J'):
        print('only 1 gram will fill you for life')
        points += 15
    elif(food == 'k')|(food == 'K'):
        print('r/foundTheAmerican')
        points += 10
    elif(food == 'l')|(food == 'L'):
        print('KFC! KFC!')
        points += 15
    elif(food == 'm')|(food == 'M'):
        print('Go make me a sandwich woman')
        points += 10
    else:
        if(fake == 0):
            print('Try answering with one of the answers next time :)')
        elif(fake == 1):
            print('Seriosly, just type one of the options')
        elif(fake == 2):
            print('...Are you doing this to annoy me?')
        elif(fake == 3):
            print('COME ONNNN!! JUST ANSWER CORRECTLY')
        fake += 1
    #Question 5, math
    time.sleep(0.25)
    print('|')
    print('Question 5: What is f(x)=4x^16+32 if x=2 ')
    math = input('A:The heck? | B:8 | C:4x+32 | D:65568 | E:64 ')
    if(math == 'a')|(math == 'A'):
        print('Coward')
        points -= 25
    elif(math == 'b')|(math == 'B'):
        print('..How did you get that?')
        points -= 10
    elif(math == 'c')|(math == 'C'):
        print('Hey you didn\'t even try')
        points -= 15
    elif(math == 'd')|(math == 'D'):
        print('Gooodddd *clap clap*')
        points += 15
    elif(math == 'e')|(math == 'E'):
        print('mhm.. whatever..')
        points -= 5
    else:
        if(fake == 0):
            print('Try answering with one of the answers next time :)')
        elif(fake == 1):
            print('Seriosly, just type one of the options')
        elif(fake == 2):
            print('...Are you doing this to annoy me?')
        elif(fake == 3):
            print('COME ONNNN!! JUST ANSWER CORRECTLY')
        elif(fake == 4):
            print('I am so done with you... Just stop please T-T')
        fake += 1
    #Question 6, dispose of a body
    time.sleep(0.25)
    print('|')
    print('Question 6: How should you dispose of a body? ')
    dispose = input('A:Seriously what the heck!? | B:No | C:Acid | D:Bury it 10ft under | E:Bury it with a flower on top ')
    #Question 7, yes
    time.sleep(0.25)
    print('|')
    print('Question 7: What is the name of t̵̨̢̠̘͕̝̫̦̦̰̙̤̟͖͇̱̯̯̩̝̪͍̬͔͋̎̏̈́̒̅͛͗̉͗͂͌̉́̕͝ͅḩ̴̱̯̠̭͖͚̹̟͎̜̫͍̬͕̝̰̹̝͕̽͐̑͐̓̃̀̈́̔̿͌̈̈́̄͌̽͌̅̊̚̕͜é̴̢̛̻̙̪͉̖̱̱̘̺̞̼͎̙̘͈͙̲̪͑̎̃̄̂̒̅͗͗͌̀̇͑́͝ ̴̡̲̲̞̬̦̫̠̙̦͉̪͕̣̗̜̤̩̣̤̝̰̓̇̊̾̂̈́͌͜͝d̵̠̱̱̞̺̘̝͇͎͓̩̟͔͔̯̮̞̲͎͚̯͉̫̫͛̓͛̏̇̒͜å̵̤̗͑̈́̔͆ŗ̶͕̭͇̠̮͕̏͆̉̔̇̑͒̂̀͘k̶̢̡̟̱̺͎̬̱̭̼̬̲̣͔̬̠̤̠̤͎͔̯̭͔̥̠̤͋͛̊̽̑̽́̅͊́͊̍́̋̇͒́̈́̉̓̏̎͜͜͜ ̴͖͙̮͍͇͕͚̩̫̣͙̪͚͖̫̿̿l̴̡̢̢̛̫͔̫̭͎͙͊̔̽̃̆̆̇́̂̄́̇̾̔͐̀͒̑͑̌̽̽̈́̒̕̕͝͝o̴̡̡̡̡̡̝̙̮͎̯͎͈̰͙̭͖̥̫͇̞̣̺̲̱͌̍̐̀̒̂̅̿̆͗͌͒̂̊͜͜͜͝ͅŕ̶̨̢̞̗̞̖̗͒̽̒̅̌̃̌͆͑̊̃́́͆̒̇͂͑͌̋͗̂̀̚̕̚͜͝ḑ̴̳̝̠̭͉̭̠̩̼͖̞̙̰̜̤̥̄͑́͑́͐͊̾̎̒͠ͅͅ ')
    dispose = input('A:... | B:I.. What? | C:Should I know that...? | D:Well Jerry of course | E:Taco ')
    #Question 8, are you okay
    time.sleep(0.25)
    print('|')
    print('(っ◔◡◔)っ')
    hug = input('A:Yes | B:No ')
    #Question 9, ready
    time.sleep(0.25)
    print('|')
    print('Are you tired of this? ')
    tired = input('A:Yes | B:No ')
    #Question 10, end
    time.sleep(0.25)
    print('|')
    print('Do you want it to end? ')
    end = input('A:Yes | B:No ')
    if(end == 'a')|(end == 'A'):
        time.sleep(0.25)
        print('Okay, let\'s end this...')
        time.sleep(0.75)
    elif(end == 'b')|(end == 'B'):
        time.sleep(0.25)
        print('okay :) let\'s stay here and chat for a while')
        time.sleep(2)
        print('What do you want to talk about?')
        print('A:Taco B:Che...')
        time.sleep(1)
        print('No, you don\'t need that anymore')
        time.sleep(0.5)
        want = input('Just tell me what you want :) ')
        if(input == ''):
            print()
    else:
        print('Let\'s just go..')
        
    
    
def hotnessQuiz(fake,points):
    time.sleep(0.75)
    
    
    
    
start()
