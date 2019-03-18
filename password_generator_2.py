#password generating sample solutions
def password_generator():
    
    start = input("wanna generate a new password : ")
    while start == 'Y' :
    
        import random

        s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!~`@#$%^&*()-_"
        passlen = 8
        p = " ".join(random.sample(s,passlen))
        print(p)
        start = input("wanna generate a new password : ")

    print("program end")

password_generator()    
