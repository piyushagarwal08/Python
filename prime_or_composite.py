import sys
number = int(input("enter any number: "))
if number == 0:
    print("Composite")
    sys.exit(0)
k = 0
for i in range(2,(number//2)+1):
    if number%i == 0:
        k +=1
if k <=0:
    print("Prime")
else:
    print("Composite")
