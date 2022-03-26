#with open('textos/texto.txt') as arquivos:
caminho_arquivo = 'textos/texto.txt'

#abre o arquivo com o valor padrão 'r' para leitura.
with open(caminho_arquivo) as arquivos:
    for linha in arquivos:
        print(linha)

