from urllib.error import HTTPError
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import sleep

link_now = 'https://en.wikipedia.org/wiki/Eric_Idle'
link_search = 'https://en.wikipedia.org/wiki/South_Shields'
links_infinitos = set()
links_ja_visitado = set()
ten = 1

# Definir um cabeçalho para simular um navegador real
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
            if url.startswith('http') and '/wiki' in url:
                cj.add(url)

    return cj


while ten <= 100:
    conjunto = conjunto_links_unicos(link_now)
    links_infinitos.update(conjunto)

    if links_infinitos is None:
        break

    if link_search in conjunto:
        print(f'Oba achei o link depois de {ten} Tentativas')
        break
    else:
        ten += 1

    if link_now in links_ja_visitado:
        continue

    links_ja_visitado.add(link_now)
    link_now = links_infinitos.pop()
    sleep(0.2)
    print(link_now)
