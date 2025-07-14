import PyPDF2
import os
from google_images_search import GoogleImagesSearch
from PIL import Image

def gerar_relatorio_pdf(diretorio, diretorio_imagem):

    arquivos_pdf = [f for f in os.listdir(diretorio) if f.endswith('.pdf')]
    arquivo_final = PyPDF2.PdfWriter()
    nome_arquivo = pesquisa_imagem()
    imagem_para_pdf(diretorio_imagem + nome_arquivo, 'pdf/capa.pdf')
    capa = PyPDF2.PdfReader('pdf/capa.pdf').pages[0]
    arquivo_final.add_page(capa)

    for nome_arquivo in sorted(arquivos_pdf):
        caminho_completo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_completo, 'rb') as arquivo_leitura:
            for pagina in PyPDF2.PdfReader(arquivo_leitura).pages:
                texto_extraido = pagina.extract_text() or ''
                if texto_extraido:
                    arquivo_final.add_page(pagina)

    with open('relatorio.pdf', 'wb') as pdf_saida:
        arquivo_final.write(pdf_saida)

        return None

def pesquisa_imagem():
    # Configurar a API do Google Imagens
    gis = GoogleImagesSearch('AIzaSyDJ9r5DSYA7KTLuyBGc8-GjQAL5P85EksU', '737dd31d95ed449c2')

    q = input("Digite o termo de pesquisa para imagens: ")

    # Definir os parâmetros de busca
    search_params = {
        'q': q,
        'num': 2,  # número de imagens que você quer obter
        'safe': 'high',  # filtro de segurança
        'fileType': 'jpg'  # tipo de arquivo das imagens
    }

    # Realizar a busca
    gis.search(search_params=search_params)

    # Obter os resultados
    for image in gis.results():
        # Aqui você pode fazer o que quiser com as imagens, como salvá-las em um diretório
        file_name = os.path.basename(image.url)
        image.download('image/' + file_name)

    print("Acesse o diretorio 'documents/helo/script/desafios/image/' para ver as imagens baixadas.")
    caminho =  input("Informe o nome da imagem que deseja adicionar ao relatório: ")
    return caminho + '/' + caminho

    # input("Pressione Enter para continuar...")
    #
    # # Limpar os resultados
    # gis.clear_search_results()

def imagem_para_pdf(caminho_imagem, caminho_pdf):
    imagem = Image.open(caminho_imagem)
    if imagem.mode != 'RGB':
        imagem = imagem.convert('RGB')
    imagem.save(caminho_pdf, 'PDF')

if __name__ == '__main__':
    diretorio = 'arquivo_teste'
    diretorio_imagem = 'image/'
    gerar_relatorio_pdf(diretorio, diretorio_imagem)



# 📄 Desafio 1: Gerador de Relatórios a Partir de Vários PDFs
# Descrição: Dado um diretório com vários PDFs de relatórios mensais, crie um script que:
#
# Leia todos os arquivos PDF de um diretório específico.
#
# Extraia o conteúdo textual de cada um.
#
# Monte um único arquivo .txt ou .pdf com todos os textos organizados por ordem alfabética do nome do arquivo.
#
# Extra: Adicione uma capa no PDF final com um sumário simples.