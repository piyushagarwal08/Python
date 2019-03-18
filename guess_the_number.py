#GUESS THE NUMBER
game = "start"
while str(game) != "exit" :
    
   
    count = 1
    guess = input("GUESS THE NUMBER THAT WILL BE UPCOMING IF YOU CAN : ") 
    import random
    for x in range(1):
        r = random.randint(1,10)
        print(r)

   
    if 10 > int(guess)-int(r) >= 4:
        print("you guessed too high")
    elif (int(guess) - int(r)) <= 3 and (int(guess) - int(r)) != 0:
        print("you guessed very near")    
    elif int(guess) == int(r):
        print("woah! you guessed it correct. you are a Genius.")

    game = input("Do you wish to exit the game, if yes type exit : ")
    count += 1

print("you guessed the number " + str(count) + " times")   
    
