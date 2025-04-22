produto = {
    'nome': 'coca cola',
    'preco': 7.90,
    'categoria': 'casual'
}

dc = {key: valor.upper() if isinstance(valor, str) else valor for key, valor in produto.items()}

print(dc)
