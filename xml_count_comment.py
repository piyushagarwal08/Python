import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et
url = input("enter the url: ")
fhand = urllib.request.urlopen(url).read()
data = et.fromstring(fhand)
lst = data.findall('comments/comment/count')
total_sum = 0
for i in lst:
    total_sum = total_sum + int(i.text)

print(total_sum)    
