num = 28
perfect=[]
for number in range(1,num): 
    a = []
    if number > 1:
        for i in range(1,number):
            if number % i == 0:
                a.append(i)
                continue
        b = sum(a)
        if b == number:
            perfect.append(number)
        else:
            continue
    elif number == 0 or number == 1:
        print("true")
print(perfect)
