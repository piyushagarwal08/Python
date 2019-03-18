#CHECK WHETHER GIVEN NUMBER IS PRIME OR NOT
numb = input("enter any number to check for its primality : ")
#numb = int(numb)
try:
    numb = int(numb)
except:
    print("INVALID INPUT ~ pls enter a number")
    print("restart the program")
    quit()

if numb == 0:
    print("zero is not a prime number")
    
div = numb
while div != 0:
    #print("hello")
    
    div = int(div) -1
    c = numb/div
    if div == 1 and c == numb:
        print("the given number ",numb," is prime")
        break
    
    if c == int(c):
        
        print("the given number ",numb," is not prime")
        break
    elif c == numb:
        
        break
    elif c == float(c):
        continue
    

    
        
