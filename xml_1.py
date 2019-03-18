import xml.etree.ElementTree as ET
data = '''<person>
    <hello>
        <yellow>xjhjs</yellow>
        <name>piyush</name>
    </hello>
    
    <hello>
        <yellow>xjhjs</yellow>
        <name>ravi</name>
    </hello>
    </person>'''
tree = ET.fromstring(data)
lst = tree.findall('hello/name')
print(len(lst))
for i in lst:
    print(i.text)
