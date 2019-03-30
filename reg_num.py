import re
number = input("enter your mobile number: ")
a = re.match(r'^[+91]+\-[789][0-9]{9}',number)
print(a,a.group())
