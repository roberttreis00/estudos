'''
    Calculadora monstra
    Aplicar os conhecimentos de *args empacotar e **desempacotar
'''


def calculadora_avancada(*args, **kwargs):
    result = []

    for numero in args:
        operacoes = []
        for operacao, valor in kwargs.items():
            match operacao:
                case 'multiplicar':
                    operacoes.append(numero * valor)
                case 'dividir':
                    operacoes.append(numero / valor)
                case 'soma':
                    operacoes.append(numero + valor)

        result.append(operacoes)

    return result


print(calculadora_avancada(50, dividir=2, multiplicar=2, soma=2))
