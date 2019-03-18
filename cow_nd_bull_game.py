#COWS AND BULL...GAME
def cow_bull_game():
    print("RULES --> ")
    print('''(1) no. of cows shows the digits which are guessed correctly and are at correct position.\n(2) no. of bulls shows the digits which are guessed correctly but are at wrong position.\n(3) enter only 4-digit whole numbers.''')
    
    print("\nTHE GAME BEGINS!!!!!")

#variables are declared over here    
    import random
    cow = 0
    bull = 0
    
    numb = random.sample('1234567890',4)
    number = list(numb)
    show = "lose"
    count = 0

#the game logic is beginning from here
    while int(cow) != 4:
        count = count + 1
        cow = 0
        bull = 0
        i = 0
        
        user = input("\nguess the possibly generating 4-digit number : ")
        user_number = list(user)
        if len(user_number) > 4:
            print("\nINVALID INPUT : please enter only 4- digit number")

#code to calculate the number of cows
        try:
            while i <=3 : 
                if number[i] == user_number[i]:
                    cow = cow + 1
                i = i + 1     
        except:
            print("\nINVALID INPUT : please enter only 4- digit number")
            continue
        print("cow : " + str(cow))

#code to calculate the number of bulls        
        for m in user_number:
            for n in number:
                if m == n:
                    bull = bull + 1
                    continue
                else:
                    continue
        print("bull : " + str(bull))
        
        if user == show:
             print(number)
    print("GAME OVER!!!" + "YOU GUESSED IT IN " + str(count) + " TURNS")
cow_bull_game()    
        
