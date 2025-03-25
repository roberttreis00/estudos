import os
import shutil
import zipfile
import tempfile
from bs4 import BeautifulSoup
from googletrans import Translator
import re


def translate_epub(input_file, output_file, target_language='pt'):
    """
    Traduz um arquivo .epub para o idioma alvo especificado.

    Args:
        input_file (str): Caminho para o arquivo .epub de entrada
        output_file (str): Caminho para o arquivo .epub de saída traduzido
        target_language (str): Código do idioma alvo (ex: 'pt' para português)
    """
    # Criar diretório temporário para extrair o arquivo .epub
    temp_dir = tempfile.mkdtemp()

    try:
        # Extrair o arquivo .epub (que é basicamente um arquivo ZIP)
        print(f"Extraindo {input_file} para {temp_dir}")
        with zipfile.ZipFile(input_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Inicializar o tradutor
        translator = Translator()

        # Encontrar todos os arquivos HTML/XHTML no diretório temporário
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith(('.html', '.xhtml', '.htm')):
                    file_path = os.path.join(root, file)
                    print(f"Traduzindo {file_path}")

                    # Ler o arquivo HTML
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Analisar o HTML
                    soup = BeautifulSoup(content, 'html.parser')

                    # Encontrar todos os elementos de texto
                    text_elements = soup.find_all(text=True)

                    # Traduzir cada elemento de texto que não seja código ou script
                    for element in text_elements:
                        # Ignorar scripts, estilos, etc.
                        if element.parent.name in ['script', 'style', 'code']:
                            continue

                        # Ignorar texto vazio
                        if not element.strip():
                            continue

                        # Traduzir o texto
                        try:
                            translated_text = translator.translate(element, dest=target_language).text
                            # Substituir o texto original pelo traduzido
                            element.replace_with(translated_text)
                        except Exception as e:
                            print(f"Erro ao traduzir texto: {str(e)}")

                    # Salvar o arquivo traduzido
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))

        # Criar um novo arquivo .epub com o conteúdo traduzido
        print(f"Criando novo arquivo .epub: {output_file}")
        with zipfile.ZipFile(output_file, 'w') as zip_ref:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zip_ref.write(file_path, arcname)

        print(f"Tradução concluída. Arquivo salvo como {output_file}")

    finally:
        # Limpar o diretório temporário
        shutil.rmtree(temp_dir)


# Exemplo de uso
if __name__ == "__main__":
    translate_epub("OpenPyXL Python Library_ Powerful.epub", "livro_traduzido.epub", "pt")
