#Christopher Weiner
#CS 362
#Assignment 3
#Leap Year - Input Checking/Validation

def leapYearCheck(x):
    if(x % 4) == 0:
        if(x % 100) == 0:
            if(x % 400) == 0:
                print(str(x) + " is a leap year")
                return
            else:
                print(str(x) + " is not a leap year")
                return
        else:
            print(str(x) + " is a leap year")
            return
    else:
        print(str(x) + " is not a leap year")
        return

print("Please enter a number to see if it is a leap year:")
x = input()
if x.isdigit() == False:
    print(str(x) + " is not a number, or includes characters")
    exit()
else: leapYearCheck(int(x))