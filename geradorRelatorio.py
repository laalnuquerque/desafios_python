import PyPDF2
import os

def gerar_relatorio_pdf(diretorio):

    arquivos_pdf = [f for f in os.listdir(diretorio) if f.endswith('.pdf')]
    arquivo_final = PyPDF2.PdfWriter()

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


if __name__ == '__main__':
    diretorio = 'arquivo_teste'
    gerar_relatorio_pdf(diretorio)



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