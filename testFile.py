#I didn't see anything wrong with it so I remade it in python to test it
def main():
    firstTest = 100
    secondTest = 100
    average = 100
    passing = 100
    while firstTest != 0:
        print("Enter first score or 0 to quit")
        firstTest = int(input())
        print("Enter second score")
        secondTest = int(input())
        average = (firstTest+secondTest)/2
        if(average >= 60):
            print("Pass")
        else:
            print("Fail")
    print("End")
            
main()
