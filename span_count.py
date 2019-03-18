import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input("enter the url: ")
fhand = urllib.request.urlopen(url).read()
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('span')
total_count = 0
for tag in tags:
    total_count = total_count + int(tag.contents[0])

print(total_count)    
