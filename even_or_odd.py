#PROGRAM TO IDENTIFY A NUMBER TO BE EVEN OR ODD
print("enter any number to be identified as even or odd")
number = input("the number : ")

if int(number) % 2 == 0:
    
    if int(number) % 4 ==0:
        print("given number is EVEN and a multiple of 4 as well")
    else:
        print("the given number " + str(number) + " is even")

else:
    print("the given number " + str(number) + " is odd")

check = input("give me a new number : ")
c = int(number) / int(check)
if c % 2 ==0:
    print("new number evenly divides the old number")
else:
    print("new number doesn't divide")
