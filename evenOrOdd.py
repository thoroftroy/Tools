#program to tell you if your input is an odd number
def isOdd():
    num = input('Input a number ')
    if(num.isdigit()):
        num = int(num)
        if (num % 2) == 0:
             print ('The number is even')
        else:
            print ('The number is odd')
        isOdd()
    else:
        print('Cry')
        isOdd()
        
        
isOdd()
    
