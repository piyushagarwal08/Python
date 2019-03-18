#count the sum of all digits present in text file
import re
file = open('test.txt')
b = list()
for line in file:
    line = line.rstrip()
    a = re.findall('[0-9]+' ,line)
    if len(a) < 1 : continue
    for i in range(0,len(a)):
        n = float(a[i])
        b.append(n)
print(sum(b))

