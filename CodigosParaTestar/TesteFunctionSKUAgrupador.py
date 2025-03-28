import re
from Custos_Produtos_ALL import CustoProdutosALL


def extrair_agrupador(codigo):
    """Extrai o agrupador do código do produto, removendo cor/tamanho."""
    opcao1 = re.match(r"^([A-Za-z0-9]*?)(C.*)?$", codigo)
    retorno1 = opcao1.group(1) if opcao1 else codigo
    qtd_caracteres1 = len(retorno1)

    opcao2 = re.match(r"^([A-Za-z0-9]+?)([A-Z]+.*)?$", codigo)
    retorno2 = opcao2.group(1) if opcao2 else codigo
    qtd_caracteres2 = len(retorno2)

    opcao3 = re.match(r"^([A-Za]+[z0-9]+)", codigo)
    retorno3 = opcao3.group(1) if opcao3 else codigo
    qtd_caracteres3 = len(retorno3)

    b = retorno1

    if qtd_caracteres2 < qtd_caracteres1 and qtd_caracteres2 != 1:
        if qtd_caracteres2 == qtd_caracteres3:
            b = retorno1
        else:
            b = retorno2
    elif qtd_caracteres1 == 0 and qtd_caracteres2 == 1:
        b = retorno3
    elif qtd_caracteres1 == qtd_caracteres2 and qtd_caracteres3 > qtd_caracteres2:
        b = retorno1

    # Turma do 3
    if qtd_caracteres2 == 1 and qtd_caracteres3 < qtd_caracteres1 or qtd_caracteres2 == qtd_caracteres3:
        if retorno3.startswith('R'):
            b = retorno1
        else:
            b = retorno3

    print(f'Retorno1 {retorno1}| Retorno2 {retorno2}| Retorno3 {retorno3}|'
          f'SKU: {codigo}| Resultado: {b}')
    return b


print(extrair_agrupador('CC3516BRANCO'))
