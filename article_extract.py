import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl

url = 'https://www.duckduckgo.com/?q=piyush'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen(url)
file = fhand.read()
soup = BeautifulSoup(file, 'html.parser')
tags = soup('a')
print(len(tags))


