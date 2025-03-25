from tempfile import NamedTemporaryFile

with NamedTemporaryFile(suffix='.mp3', prefix='planilhabacana_', delete=False, mode='w+') as file:
    print(file.name)
    input()
