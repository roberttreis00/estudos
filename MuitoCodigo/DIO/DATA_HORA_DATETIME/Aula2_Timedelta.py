from datetime import datetime, timedelta

# Gestao lava jato
horario_de_entrada = datetime.today()
tempo_para_lavar = timedelta(minutes=60)

calculo = horario_de_entrada + tempo_para_lavar


print(f'Vou entregar o lavado: {calculo.strftime("%H:%M")}')
