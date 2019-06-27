#cipher
import string
def encrypt(x):
    dict={}
    for i in range(len(string.printable)):
        dict[string.printable[i]] = string.printable[i-6]
    for i in x:
        print(dict.get(i),end='')

def decrypt(x):
    dict = {}
    for i in range(len(x)):
        dict[string.printable[i]] = string.printable[i+6]           
    for i in x:
        print(dict.get(i),end='')

encrypt("hello")


             
