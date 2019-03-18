import pandas as pd
import numpy as np
import random
m = random.randint()
c = random.randint()
d_m = 2*np.mean(m*x + c - y)*x
d_c = 2*np.mean(m*x + c - y)

while (d_m !=0 and d_c != 0):
    m = m - d_m
    c = c - d_c

print(m)
print(c)
    
