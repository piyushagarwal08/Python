<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
url = "https://www.justdial.com"
r = requests.get(url)
#soup = BeautifulSoup(r.content,features = "html.parser")
print(r.content)
#for link in links:
  #  if "http" in link.get("href"):
        
       # print("<a href = '%s'>%s</a>"%(link.get("href"),link.text) )
=======
import requests
from bs4 import BeautifulSoup
url = "https://www.justdial.com"
r = requests.get(url)
#soup = BeautifulSoup(r.content,features = "html.parser")
print(r.content)
#for link in links:
  #  if "http" in link.get("href"):
        
       # print("<a href = '%s'>%s</a>"%(link.get("href"),link.text) )
>>>>>>> 4c479d7e2005e07f435d14fdc1acbbc842e10244
