<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.bhaskar.com")
soup = BeautifulSoup(r.content,features = "html.parser")
#for link in soup.find_all('a'):
   # print(link.text, link.get('href'))
   #print("<a href = '%s'>%s</a>"%(link.get("href"),link.text) )
data = soup.find_all("div", {class":"
=======
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.bhaskar.com")
soup = BeautifulSoup(r.content,features = "html.parser")
#for link in soup.find_all('a'):
   # print(link.text, link.get('href'))
   #print("<a href = '%s'>%s</a>"%(link.get("href"),link.text) )
data = soup.find_all("div", {class":"
>>>>>>> 4c479d7e2005e07f435d14fdc1acbbc842e10244
