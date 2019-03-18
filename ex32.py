the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1,'pennies',2,'dimes', 3, 'quarters']

for number in the_count:
    print(f"this count is {number}")

for fruit in fruits:
    print(f'A fruit : {fruit}')

for i in change:
    print("I got", i)
elements = []
for i in range(0,6):
    print(f"Adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"elements: {i}")
