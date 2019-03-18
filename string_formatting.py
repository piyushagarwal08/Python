people = 10
x = f"there are {people} type of people"

binary = "binary"
do_not = "don't"
y = f"know{binary} or {do_not}"

print(x,y)
print(f"i said '{x}'")

z = False
z_ = "funny? {}"
print(z_.format(z))

print("i am piyush")
print("i am in love with {} since a long time".format('harshita'))


f = "{} {} {} {}"
print(f.format(1,2,3,4))
print(f.format("l","o","v","e"))
print(f.format(True, False, True, False))
print(f.format(f,f,f,f))





learn = "\ti love learning"
learn_2 = "i'm interested\non in python"
backslash = "i'm \\a\\lover"
b = """
i'll do a list:
\t* harshita
\t* loves
me\n\t i think """
print(learn)
print(learn_2)
print(backslash)
print(b)
