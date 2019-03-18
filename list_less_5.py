#PROGRAM TO PRINT OUT ALL ELEMENTS OF A LIST LESS THAN 5
i=1
list_1 = []
while i<=10:
    list_value = input("enter integer values to insert in the list : ")
    list_1.append(list_value)
    i +=1

print(list_1)
for value in list_1:
    if int(value) < 5:
        print(value)

new_list = [ value for value in list_1 if int(value) < 5]
print(new_list)

user_num = input("insert a new numbe and i will give a list of numbers smaller than ur : ")
less_than_list = [value for value in list_1 if int(value) < int(user_num)]
print(less_than_list)
