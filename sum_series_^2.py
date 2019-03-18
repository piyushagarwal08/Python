sums = 0
n = int(input("enter value of n: "))
for i in range(1,n+1):
    sums = sums + (i**i)/i
print(sums)
