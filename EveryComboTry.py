import time
#to make this stupid program we are not gonna do it the way they do
#my first thought was to simply loop through each number, this gets us part of the way there
def try1():
    digit1 = [1,2,3,4,5,6,7,8,9]
    digit2 = digit1
    digit3 = digit1
    i = 0

    while i < len(digit1):
        print(digit1[i],digit2[i],digit3[i])
        i += 1
#now I am going to try to loop them all
#now this provided us with a bit more variation but it isn't truly all combanations
def try2():
    digit = [1,2,3,4,5,6,7,8,9]
    times = 0
    i = 0
    e = 0
    o = 0
    while times <= 100:
        print(digit[i],digit[e],digit[o])
        i += 1
        e += 2
        o += 3
        if(i >= 9):
            i = 0
        if(e >= 9):
            e = 0
        if(o >= 9):
            o = 0
        times += 1
#heres a new idea, this will print every combonation of the 3 numbers of 1 2 and 3 but I want all 9
def try3():
    print("Start")
    a = 1
    b = 2
    c = 3
    d=[]
    d.append(a)
    d.append(b)
    d.append(c)
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                print(d[i],d[j],d[k])
#onto the next try
#using the same sort of thing as before but modified slightly. This finally gets us every possible combonation of 3 digits
#however it looks nothing like the original, and I don't think while loops are the best option for this program
def try4():
    d = [0,1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                print(d[i],d[j],d[k])

def main():
    cont = None
    print("Here are my tries and which one I think works best!")
    time.sleep(0.5)
    print("First off is try number 1 it works pretty okay I guess...")
    print("My first thought was to simply loop through each number, this gets us part of the way there")
    cont = input("Press ENTER to continue...")
    try1()
    cont = input("Press ENTER to continue...")
    print("Sooo that wasn't the best, lets show you the next version")
    print("now I am going to try to loop them all. This provided us with a bit more variation but it isn't truly all combanations")
    cont = input("Press ENTER to continue...")
    try2()
    cont = input("Press ENTER to continue...")
    print("Here's a new idea, this will print every combonation of the 3 numbers of 1 2 and 3 but I want all 9")
    cont = input("Press ENTER to continue...")
    try3()
    cont = input("Press ENTER to continue...")
    print("And as you can see... That only gets digits 1-3")
    print("So now...")
    time.sleep(0.2)
    print("using the same sort of thing as before but modified slightly")
    print("This finally gets us every possible combonation of 3 digits however it looks nothing like the original")
    print("and I don't think while loops are the best option for this program")
    cont = input("Press ENTER to continue...")
    try4()
    cont = input("Press ENTER to continue...")
    print("So yeah, I did it it just took me way longer than it should have...")
    
main()
