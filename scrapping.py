import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("enter url")
fhand = urllib.request.urlopen(url)
file = fhand.read()
soup = BeautifulSoup(file, 'html.parser')
work = soup('pre')
print(len(work))
for i in work:
    print(i.text)
