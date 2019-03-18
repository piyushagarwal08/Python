def work(var,add):

    i = 0
    numbers = []
    while i <var:

        print(f"At the top i is: {i}")
        numbers.append(i)

        i = i+add
        print("Numbers now: ", numbers)
        print(f"At the bottom is {i}")

        print("The Numbers: ")
        for num in numbers:
            print(num)

work(3,2)
