#lista sofre alteração na função
lista_cor = ['Vermelho', 'Verde', 'Preto', 'Branco', 'Azul']
clone_lista = lista_cor

def lista_funcao(lista):
    for cor in lista:
        print(cor)
        lista.pop()

lista_funcao(clone_lista)
print(lista_cor)
print('----------')

#lista não sofre alteração na função
lista_cor = ['Vermelho', 'Verde', 'Preto', 'Branco', 'Azul']

clone_lista = lista_cor[:]

lista_funcao(clone_lista)
print(lista_cor)
print('----------')

#lista não sofre alteração na função
lista_funcao(lista_cor[:])
print(lista_cor)