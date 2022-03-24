escreva = ''

while True:
    print('Para encerrar o programa, digite "s".')
    escreva = input('Escreva aqui: ')
    if escreva.lower() == 'c':
        continue
        print('Não vai printar isto')
    elif escreva.lower() == 's':
        print('Programa finalizado!')
        break
    else:
        print(escreva)