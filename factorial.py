print("this is a program to print the factorial of any number greater than zero\n")

factorial_n = input("give me a number to find its factorial which is greater than zero: ")

def factorial(number):
    print("hello " + str(number))
    factorial1 = 1
    
    while number!=0:
        
        factorial1 *= int(number)
        number = int(number) -1

        
    return factorial1
    
    

print("\n")
print(factorial(factorial_n))
