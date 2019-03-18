def password_generator():   
    password = None
    user = input('wanna generate a new password : Y/N ')
    import random
    while user == 'Y' :
        i = 0
        while int(i) < 1:
        
            low_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            up_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            symbol = random.choice('`~!@#$%^&*()-_<,>./?{[}]')
            number = random.choice('1234567890')
            if password == None :    
                password = low_letter + up_letter + symbol + number
                continue
            password = password + low_letter + up_letter + symbol + number
        
            i = i+1

        print("new password : " + password)
        user = input('wanna generate a new password : Y/N ')
        password = None
        
        if user == 'N':
            print('end')

        while user != 'Y' and user != 'N':
            print('invalid input')
            user = input('wanna generate a new password : Y/N ')
            
     
         

password_generator()    


