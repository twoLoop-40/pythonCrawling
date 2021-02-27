from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
for link in bs.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
        