#ROCK_PAPER_SCISSORS
new = input("do you wish to start a new game : Y/N  ")

new = str(new)
if new == 'Y':
    print("\n rock equals r , paper equals p , scissor equals s ")
    
    player_1 = input("Player 1 : enter rock paper or scissor : ")
    player_2 = input("Player 2 : enter rock paper or scissor : ")

    while str(player_1) == str(player_2):
        
        print("Its a draw")
        player_1 = input("Player 1 : enter rock paper or scissor : ")
        player_2 = input("Player 2 : enter rock paper or scissor : ")

    player_1 = str(player_1)
    player_2 = str(player_2)




    while new == 'Y':
        
        if player_1 == 'r' and player_2 == 's': 
            print("player 1 wins")
        elif player_1 == 's' and player_2 == 'r':
            print("player 2 wins")
            
        if player_1 == 's' and player_2 == 'p':
            print("player 1 wins")
        elif player_1 == 'p' and player_2 == 's':
            print("player 2 wins")

        if player_1 == 'r' and player_2 == 'p':
            print("player 2 wins")
        elif player_1 == 'p' and player_2 == 'r':
            print("player 1 wins")
            
        new = input("do you wish to start a new game : Y/N  ")
        new = str(new)
        if new == 'N':
            print("game ends")
            break
        player_1 = input("Player 1 : enter rock paper or scissor : ")
        player_2 = input("Player 2 : enter rock paper or scissor : ")
        player_1 = str(player_1)
        player_2 = str(player_2)

else:
    print("game end")
 
