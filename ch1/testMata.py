from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.matamath.net/views/v4_1/lms/tc_home/tc_home.jsp')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
except HTTPError as e:
    print(e)

