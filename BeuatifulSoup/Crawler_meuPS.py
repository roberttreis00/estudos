from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from pprint import pprint
import re

url = 'https://www.meups.com.br'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36'}
req = Request(url, headers=HEADERS)
bs = BeautifulSoup(urlopen(req), 'html.parser')

links = bs.find_all('a')
linkS_unicos = set()


def data_publicacao(link_noticia):
    req1 = Request(link_noticia, headers=HEADERS)
    bs2 = BeautifulSoup(urlopen(req1), 'html.parser')

    data = bs2.find(class_='postedon').text
    return data


for link in links:
    if 'href' in link.attrs and re.search('br/noticias/', link.attrs['href']):
        linkS_unicos.add((link.attrs['href'], data_publicacao(link.attrs['href'])))


pprint(linkS_unicos)
