#STRING LISTS
string = input("insert a word to check whether its pallindrome or not : ")
string = str(string)
new_string = string[::-1]
print(new_string)

if string == new_string:
    print("PALLINDROME")
else :
    print("NOT PALLINDROME")
