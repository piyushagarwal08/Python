#TO CREATE A LIST OF COMMON ELEMENTS FROM GIVEN 2 LISTS
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''n = input("enter the number of elements in list 1 : ")
m = input("enter the number of elements in list 2 : ")
list_1 = []
while n==0:
    x = input("element for the list : ")
    list_1.append(x)
#while m==0:
    y = input("elements for the list : ")'''
new = []
c = None
for num in a:
    for same in b:
        if num != same:
            continue
        else:
            new.append(num)

for same in new:
    if c == None:
        c = same
        continue
    if same == c:
        new.pop(same)

        
    
print(new)            

# for finding unique elements in list1 and list 2

if len(a)!=len(set(a)):
    print("True")
