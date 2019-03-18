#TO CREATE COMMON LIST OUT OF TWO RANDOM GENERATED LIST
import random

a = random.sample(range(1,100), 15)
b = random.sample(range(1,100), 17)

print(a,"\n",b)

result = [i for i in set(a) if i in b]
print(result)
