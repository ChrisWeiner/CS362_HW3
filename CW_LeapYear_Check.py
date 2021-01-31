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
try:
    x = int(x)
    if(x < 0):
        print(str(x) + " is less than zero, cannot check if it's a leap year")
    else:
        leapYearCheck(int(x))
except ValueError:
        print(str(x) + " is not a valid number, or includes characters")