from tempfile import TemporaryFile

with TemporaryFile(mode='w+') as file:
    print(file.name)
    file.write('Batatinha Fritas')  # colocar o B de bytes
    file.seek(0)
    print(file.read())
