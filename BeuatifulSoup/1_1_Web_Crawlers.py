"""
Crawlers pegar links dentro de links
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Eric_Idle')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
