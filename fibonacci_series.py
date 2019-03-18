#FIBONACCI SERIES
def fibonacci():
    
    print("This is a program to print the number of fibonacci elements a user asks for")
    i = input("\n how many Fibonacci numbers you wish to generate : ")
    a = 1
    b = 0
    i = int(i)
    j = 0
    print(a)
    while int(j) != i-1:
    
        c = int(b) + int(a)
        print(c)
    
        b = a
        a = c
        j = j+1

    print("program ends")    
    
    
fibonacci()
