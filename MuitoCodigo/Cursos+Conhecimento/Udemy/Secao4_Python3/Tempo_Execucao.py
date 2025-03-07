'''
Código que calcula quanto tempo leva para executar uma código a logica é primeira executa a funcao tempo atual
roda seu código e em seguida para esse tempo atual para outra funcao e vai fazer o calculo e exibir o tempo que foi
gasto
'''
from time import time, sleep


def tempo_fatorado(tempo1, tempo2):
    calculo_tempo = tempo2 - tempo1

    tempo_minutos = calculo_tempo / 60
    tempo_horas = tempo_minutos / 60
    return round(tempo_horas, 2), round(tempo_minutos, 2), round(calculo_tempo, 2)


def tempo_atual():
    tempo = time()
    return int(tempo)


def tempo_final(tempo_inicial):
    tempo_fim = tempo_atual()
    tempo_gasto = tempo_fatorado(tempo_inicial, tempo_fim)
    return tempo_gasto


inicio = tempo_atual()

# meu codigo roda aqui
sleep(1)

tempoo = tempo_final(inicio)

print(f'Você gastou {tempoo[0]} Horas {tempoo[1]} Minutos {tempoo[2]} e Segundos para executar o código!')
