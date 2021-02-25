from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError:
        return None
    return title

title = getTitle('https://www.matamath.net/views/v3/lms/overall/progress.jsp')
print('Title could not be found') if title == None else print(title) 
    