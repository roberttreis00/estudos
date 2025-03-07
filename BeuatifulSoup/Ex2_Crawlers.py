from pprint import pprint
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://bar.wikipedia.org/wiki/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}


def conjunto_links_unicos(link):
    cj = set()

    # Criar uma requisição com cabeçalho
    req = Request(link, headers=HEADERS)
    try:
        open_url = urlopen(req)
    except HTTPError:
        return

    bs = BeautifulSoup(open_url, 'html.parser')

    links = bs.find_all('a')
    for link_http in links:
        url = link_http.attrs
        if 'href' in url:
            url = url['href']
            if url.startswith('http') and '/wiki/' in url:
                cj.add(url)

    return cj


pprint(conjunto_links_unicos(url))
