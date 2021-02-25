from urllib.request import urlopen
from bs4 import BeautifulSoup

url_1 = 'http://www.pythonscraping.com/pages/warandpeace.html'
html = urlopen(url_1)
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())


