#A PROGRAM TO DETECT A NUMBER IN A LIST
def number_detector():
    import random
    random_list = sorted(random.sample("0123456789", 6))
    count = 0
    print(random_list)
    detect_numb = input("enter the number you wish to find in ordered list: ")  
    for numb in random_list:
        if numb == detect_numb:
            print(True)
            count = count + 1
        else:
            continue
    if count == 0 :
        print(False)

def binary_search():
    n = int(input("size of random list : "))

    from random import SystemRandom
    rand_gen = SystemRandom()
    random_list = sorted([rand_gen.randrange(100) for i in range(n)])
    
    '''from random import SystemRandom
    rand_gen = SystemRandom()
    random_list = sorted(rand_gen.randrange(10) for i range(n))'''

    
    detect_numb = int(input("enter the number you wish to find in ordered list: "))
    m = len(random_list)
    print(random_list)
    #main algorithm
    while m!= 1:    
        if detect_numb < random_list[round(m/2)]:
            random_list = random_list[:round(m/2)]
            m = len(random_list)
        elif detect_numb >= random_list[round(m/2)]:
            random_list = random_list[round(m/2):]
            m = len(random_list)
    #output code       
    if random_list[0] == detect_numb:
        print(True)
    else:
        print(False)

#call the preferred method overhere
binary_search()
    
