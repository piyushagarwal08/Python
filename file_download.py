import urllib.request, urllib.parse, urllib.error
import ssl
url = input("enter the url")
#ssl certificate layer code
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_node = ssl.CERT_NONE
file = urllib.request.urlopen(url).read()
print(file)
