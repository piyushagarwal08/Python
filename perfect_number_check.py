def check(num):
    
    a=[]
    if num == 1 or num == 0:
        print("perfect")
    else:
        for i in range(1,num):
            if num % i ==0:
                a.append(i)
                continue
        b = sum(a)
        if b == num:
            print("perfect")
        else:
            print("not perfect")
    
check(28)
