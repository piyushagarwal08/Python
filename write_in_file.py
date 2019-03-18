from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = Request('http://www.practicepython.org/assets/nameslist.txt')
fhand = urlopen(req).read()
soup  = BeautifulSoup(fhand, 'html.parser' )
names = soup('pre')
print(names)
for he in names:
    print("hello")
    print(he.text)
fname = input("enter text file name: ")
open_file = open(fname, 'w')
for name in names:
    open_file.write(name.text)
open_file.close()
