#this is a program to tell user the year they will be turning 100
name = input("enter your name : ")
age = input("enter your age : ")
year_range = 100 - int(age)
year = 2018 + int(year_range)


copies = input("no. of times your statement should be printed")
while copies!=0:
    print("you will turn 100 after " + str(year_range) + " years .")
    print(" that is in " + str(year) )
    copies = int(copies) - 1 

