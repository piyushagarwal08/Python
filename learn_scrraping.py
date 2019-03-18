'''
import urllib.request
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page,features='lxml')
'''
'''
print(soup.prettify()) #prints complete html code of page
print(soup.title.string)
links = soup.find_all('a')
print(type(links))
print(len(links))
print(links[2].get('href'))
print(links[2])
'''
'''
all_tables = soup.find_all('table')
print(len(all_tables))
print(all_tables[0])
'''
'''
required_table = soup.find('table',class_="wikitable sortable plainrowheaders")
#print(required_table.prettify())
a = []
b = []
c = []
d = []
e =[]
f = []
g = []
for row in required_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 6:
        a.append(cells[0].find(text=True))
        b.append(states[0].find(text=True))
        c.append(cells[1].find(text=True))
        d.append(cells[2].find(text=True))
        e.append(cells[3].find(text=True))
        f.append(cells[4].find(text=True))
        g.append(cells[5].find(text=True))

import pandas as pd

df= pd.DataFrame(a,columns=['Number'])
df['Year_Capital'] = f
df['State/UT'] = b
print(df)        
'''    

