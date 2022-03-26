# with open('textos/texto.txt') as arquivos:
caminho_arquivo = 'textos/texto.txt'

# abre o arquivo com o valor padrão 'r' para leitura.
with open(caminho_arquivo) as arquivo:
    for linha in arquivo:
        print(linha)

# modo 'w' apaga o conteúdo do arquivo.
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('----------\nOlá, Mundo!')

while True:
    texto_usuario = input('Deseja continuar? (digite S para CONTINUAR): ')

    if texto_usuario.lower() != 's':
        break

    else:
        with open(caminho_arquivo, 'a') as arquivo:
            texto_usuario = input('O que deseja escrever? ')
            arquivo.write('\n' + texto_usuario)

#printa o arquivo com duas quebras de linha
with open(caminho_arquivo, 'r') as arquivo:
    for linha in arquivo:
        print(linha)

print('----------\n')

#printa o arquivo com apenas uma quebra de linha
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
