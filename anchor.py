import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input("enter the url: ")
position = int(input("enter the index value"))
position = position - 1
repeat = int(input("how many times to repeat the process"))
count = 1
while(count<repeat+1):
    fhand = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(fhand, 'html.parser')
    tags = soup('a')
    tag = tags[position]
    print(tag.get('href', None))
    url = tag.get('href', None)
    count = int(count) + 1

    
