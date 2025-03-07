def gerar_operacao(operacao):
    def calcular_operacao(n1, n2):
        match operacao:
            case '+':
                return n1 + n2
            case '-':
                return n1 - n2
            case '*':
                return n1 * n2
            case '/':
                return n1 / n2

    return calcular_operacao


soma = gerar_operacao('+')
print(soma(1, 50))
