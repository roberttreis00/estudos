from scipy import stats


def media_aparada(populacao, porcentagem_desejada):
    # ordenar a lista
    populacao_ordenada = sorted(populacao)
    qtd_desejada = int(len(populacao) * porcentagem_desejada)

    for x in range(0, qtd_desejada):
        populacao_ordenada.pop()

    populacao_ordenada.reverse()
    for x in range(0, qtd_desejada):
        populacao_ordenada.pop()

    qtd_total_n = len(populacao_ordenada)
    media = sum(populacao_ordenada) / qtd_total_n

    return media


conjunto = [200, 100, 50, 45, 35, 29, 25, 22, 15, 14, 10, 9, 8, 12, 27, 30, 42, 38, 6, 3, 2]
print(media_aparada(conjunto, 0.1))
print(stats.trim_mean(conjunto, 0.1))
