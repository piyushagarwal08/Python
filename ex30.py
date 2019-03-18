people = 30
cars = 40
trucks = 15
cars -= 20
if cars > people and cars < trucks:
    print("We should take the cars.")

elif cars < people or cars == trucks:
    print("We should not take the cars")

else:
    print("We can't decide")

if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("Maybe we could take the truck.")
else:
    print("We can't decide yet")

if people > trucks:
    print("Alright , lets take the truck")
else:
    print("Fine, lets stay home then")
