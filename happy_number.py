def happy(n):
    happy_set = []
    past = set()
    while n!= 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    happy_set.append(n)
    return happy_set
for x in range(1,20):
    print(happy(x))
