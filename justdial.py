import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

url = input("enter the website url : ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while(url != 'n'):
    
    fhand = urllib.request.urlopen(url)
    file = fhand.read()
    soup = BeautifulSoup(file, 'html.parser')
    tags = soup('b')
    print(len(tags))



        
