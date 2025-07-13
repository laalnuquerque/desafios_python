import os
import PyPDF2
from numpy.ma.core import indices

livro_casa = 'a culpa e das estrelas.pdf'

def frequencia_palavra():
    # Remove pontuação e converte o texto para minúsculas
    texto = ''
    with open(livro_casa, 'rb') as arquivo:
        conteudo = PyPDF2.PdfReader(arquivo)
        for pagina in conteudo.pages:
            texto += pagina.extract_text() or ''
        # conteudo = arquivo.read()
        # conteudo = conteudo.lower()
        for char in '.,;:!?':
            texto = texto.replace(char, '')

        # Divide o texto em palavras
        palavras = texto.split()
        # print(palavras)

        # Cria um dicionário para contar a frequência das palavras
        frequencia = {}
        lista_palavras = {'Ela'}
        for palavra in palavras:
            if palavra in lista_palavras:
                if len(frequencia) == 0:
                    frequencia[palavra] = 1
                else:
                    frequencia[palavra] +=1


        # Ordena as palavras por frequência (decrescente)
        palavras_ordenadas = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)
        print(palavras_ordenadas)

        with open(livro_casa, 'rb') as arquivos:
            paginas_pares = []
            leitor = PyPDF2.PdfReader(arquivos)
            escritor = PyPDF2.PdfWriter()

            for num_pages, pagina in enumerate(leitor.pages):
                num_pages += 1
                if num_pages % 2 == 0:
                    escritor.add_page(leitor.pages[num_pages])
                    paginas_pares.append(pagina)

            print(f'Número de páginas pares: {len(paginas_pares)}')

            print(f'O arquivo PDF tem {num_pages} páginas.')

            ## Verifica se o arquivo PDF tem páginas
            ## Obter a primeira página
            # primeira_pagina = leitor.pages[0]

            ## Adicionar a página ao objeto PdfFileWriter
            # for i in paginas_pares:
            #     escritor.add_page(leitor.pages[1])

            ## Escrever a página em um novo arquivo
            with open('saida.pdf', 'wb') as pdf_saida:
                escritor.write(pdf_saida)

        return palavras_ordenadas

if __name__ == '__main__':
    frequencia_palavra()


# Nível: Intermediário
# Descrição:
# Receba um texto qualquer e retorne as palavras mais comuns nele, em ordem decrescente de frequência.
#
# Exemplo de entrada: "o rato roeu a roupa do rei de roma"
# Saída esperada: