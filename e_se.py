cor = 'amarela'

if (cor == 'azul'):
    print(cor)
elif (cor == 'amarelo'):
    print(cor)
else:
    print('Não é azul, nem amarelo!')
print('----------')

carros = ['audi', 'bmw', 'ferrari', 'honda']

for carro in carros:
    if (carro == 'bmw'):
        carro = carro.upper()
    else:
        carro = carro.title()

    print(carro)
print('----------')
'''comentário aqui
   e aqui também!'''

nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))

if (idade < 16):
    print(nome + ', você tem ' + str(idade) + ' anos e não pode votar!')

elif (idade >= 16 and idade < 18):
    print(nome + ', você tem ' + str(idade) + ' anos e seu voto não é obrigatório!')

elif (idade>= 18 and idade < 60):
    print(nome + ', você tem ' + str(idade) + ' anos e seu voto é obrigatório!')
else:
    print(nome + ', você tem ' + str(idade) + ' anos e seu voto não é obrigatório!')
print('----------')

ingredientes_pedidos = ['mostarda', 'calabresa', 'queijo']
ingredientes = ['mostarda', 'queijo', 'salsa', 'tomate', 'calabresa', 'cebola']

for ingrediente in ingredientes:

    if ingrediente in ingredientes_pedidos:
        print('Ingrediente ' + ingrediente + 'já está na lista.')
    else:
        print('Adicionando ' + ingrediente + ' lista de pedidos')
        ingredientes_pedidos.append(ingrediente)

print('\nSua lista está pronta:')
for ingrediente in ingredientes_pedidos:
    print(ingrediente)
print('----------')

ingredientes_pedidos = []
continuar = 's'

while continuar.lower() == 's':
    ingrediente = input('Digite o ingrediente de sua preferência: ')
    ingredientes_pedidos.append(ingrediente.title())
    continuar = input('Deseja continuar? s ou n ')

print('A sua lista está pronta: ')

for ingrediente in ingredientes_pedidos:
    print(ingrediente)

