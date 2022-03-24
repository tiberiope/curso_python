dicionario = {'nome' : 'identificação de um objeto ou pessoa', 'capacete' : 'peça colocada na cabeça para proteção',
              'flauta' : 'instrumento musical de sopro', 'barbeador' : 'objeto utilizado para fazer a barba'}

palavra = input('Digite uma palavra para saber o significado: ')

if palavra in dicionario:
    print('O significado é: ' + dicionario[palavra])
else:
    print('Palavra não encontrada!')


