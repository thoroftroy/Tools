test1 = "null"
test2 = "null"
test3 = "null"
average = "null"
#define the programs before calling them
def housekeeping(test1,test2,test3,average):
    #Let it be noted this will crash if you input a string, I could make a check for that but I am being a little lazy with this program
    print("Enter score for test 1 or a negative number to quit")
    test1 = int(input())
    if(test1 < 0):
        print("End program")
        endOfJob()
    else:
        print("Test 1 is = ",test1)
    #now let's do the next number and get all of them inputed in this thing
    print("Enter score for test 2 or a negative number to quit")
    test2 = int(input())
    if(test2 < 0):
        print("End program")
        endOfJob()
    else:
        print("Test 2 is = ",test2)
    #now let's do number 3
    print("Enter score for test 3 or a negative number to quit")
    test3 = int(input())
    if(test3 < 0):
        print("End program")
        endOfJob()
    else:
        print("Test 3 is = ",test3)
    mainCalc(test1,test2,test3,average)
#this will be what actually does the calculations
def mainCalc(test1,test2,test3,average):
    average = (test1+test2+test3) / 3 #note this would be better to put into a list so that it is expandable, having 3 be a number that is a variable of the list length
    print("Average is:",average)
    endOfJob()
#and now for the end of job thing... I do not know why you really need one but here it is
def endOfJob():
    print("End of program, will now restart")
    test1 = "null"
    test2 = "null"
    test3 = "null"
    average = "null"
    housekeeping(test1,test2,test3,average)
#call the programs
housekeeping(test1,test2,test3,average)
#This is such an odd way to do this... I am going to totally rewrite it
#while test1 >= 0:
    #mainloop()
    
    
    
    
