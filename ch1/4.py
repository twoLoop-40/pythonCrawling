from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

try:
    html = urlopen('http://www.pythonscrapingthisurldoesnotexits.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('서버 없음!')
else:
    print('된다!')
