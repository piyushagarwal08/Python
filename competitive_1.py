T = int(input())
for i in range(0,T):
    
    N = int(input())

    elements_Array = list(map(int,input().split()))

    X = int(input())

    try:
        found = elements_Array.index(X)
    except:
        found = -1
    print(found)
