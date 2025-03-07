from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(pageUrl):
    global pages
    html = urlopen(f'http://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.text)
    except AttributeError:
        print("Ta faltando alguma coisa aqui")

    for lin in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in lin.attrs:
            if lin.attrs['href'] not in pages:
                # Page nova
                nova_page = lin.attrs['href']
                print('-' * 20)
                print('http://en.wikipedia.org' + nova_page)
                pages.add(nova_page)
                get_links(nova_page)
        sleep(2)


get_links('')
