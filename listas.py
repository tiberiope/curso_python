#cria uma lista
carros = ['ferrari', 'fusca', 'civic']

#substitui a posição 1 da lista
carros[1] = 'jeep willys'

#adiciona um novo item ao final da lista
carros.append('bmw')

#percorre a lista
print(carros)
print(carros[0].title())
print(carros[1].title())
print(carros[2].title())

#O -1 é o último item da lista
print('O \"último\" carro é o: ' + carros[-1].title())

#insere um item na posição 1 da lista
carros.insert(1, 'wrangler')
print(carros)

#insere um item com cada letra numa posição
carros.extend('uno')
print(carros)

#deleta um item específico da lista
del carros[3]
print(carros)

#remove o último item da lista
carros.pop()
print(carros)

#remove um item específico da lista
carros.pop(4)
print(carros)

#elimina o elemento pelo valor
carros.remove('n')
print(carros)