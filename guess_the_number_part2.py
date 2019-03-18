#hey welcome to the game show
count = 0
print(''' So are you ready for the game....
Choose a number between 0 and 100...
don't tell me just keep it with you ''')
rules = '''1. if i guess the number larger then your say "too far"
2. if i guess the number smaller then your say "too small"
3. if i guess it correctly don't forget to say "founded".
'''
game = [i for i in range(0,100)]
print(rules)
while(True):
    print("is it : ",game[int(len(game)/2)])
    try:
        
        user = input("is it: ")
        if(user == "too far"):
            game = game[0:int(len(game)/2)]
            count = count + 1
        elif(user == "too small"):
            count = count + 1
            game = game[int(len(game)/2):]
        elif(user == "founded"):
            count = count + 1
            break
        else:
            print("pls enter values as per the rules")
            continue
    except:
        print("that was against rules man...")
        continue

print(f'''i finally founded your number...
you are way too smart it took me {count} chances to guess it.''')
