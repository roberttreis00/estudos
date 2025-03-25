import openpyxl

# Nome do arquivo
planilha = "MegaPlanilha.xlsx"

# Abrindo a planilha corretamente
wb = openpyxl.load_workbook(planilha)
ws = wb["MEGA SENA"]

# Criando estrutura de dados
data = {
    "Concurso": [],
    "Game": []
}

# Lendo os dados da planilha
for x, linha in enumerate(ws.values):
    if x == 0:
        continue  # Pulando cabeçalho

    game = []
    for coluna, dado in enumerate(linha):
        if coluna == 0:
            data["Concurso"].append(dado)
        elif 3 <= coluna <= 8:
            game.append(dado)

    data["Game"].append(game)

# Criando nova planilha no mesmo arquivo
wb_novo = openpyxl.Workbook()
ws_novo = wb_novo.active
ws_novo.title = "Resultados Mega Sena"

# Escrevendo os cabeçalhos
ws_novo.append(["Concurso", "Game"])

# Escrevendo os dados
for i in range(len(data["Concurso"])):
    ws_novo.append([data["Concurso"][i], str(data["Game"][i])])

# Salvando o novo arquivo
wb_novo.save("NovaPlanilha.xlsx")
