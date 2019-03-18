import urllib.request, urllib.parse, urllib.error
import json
#import ssl

url = input("enter the url : ")

#ssl certificate layer code
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_node = ssl.CERT_NONE'''

data = urllib.request.urlopen(url).read()
js = json.loads(data)
#print(json.dumps(js, indent=4))

work = js["comments"]
add = 0
for i in work:
    add = add + int(i['count'])
print(add)    
