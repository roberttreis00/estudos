import random

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_questoes_acertadas = 0

for questao in perguntas:
    print()
    print(f'Pergunta: {questao.get('Pergunta')}\n')
    print('Opções:')

    opcoes = questao['Opções']
    random.shuffle(questao['Opções'])

    for opcao, alernativa in enumerate(opcoes):
        print(f'{opcao}) {alernativa}')
    opcao_escolhida = input('Escolha uma opção: ')
    if opcoes[int(opcao_escolhida)] == questao['Resposta']:
        print('Acertou \U0001F44D')
        qtd_questoes_acertadas += 1
    else:
        print('Errou \U0000274C')

print(f'Parabens, você acertou {qtd_questoes_acertadas} questões!')
