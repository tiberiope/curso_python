#lista de strings
carros = ['ferrari', 'mustang', 'bmw', 'civic', 'jeep willys']

#percorre a lista atribuindo à "carro" um item da lista "carros"
for carro in carros:
    print("Eu quero um carro do modelo: " + carro)

#lista de números (de 0 a 99) com o método "range"
numeros = list(range(0, 100))
print(numeros[-1])

#lista de números (de 1 a 100) com o método "range"
numeros2 = list(range(1, 101))
print(numeros2[-1])

#lista pulando de 3 em 3 (de 1 ao 103
numeros3 = list(range(1,104,3))
print(numeros3)

#for com lista de números
numeros = list(range(1,11))
for n in numeros:
    print(n)

#for com range
for n in range(1,11):
    print(n)

#for para adicionar itens na lista
numeros = []
for n in range(1,11):
    #adicionando números na lista
    numeros.append(n)
    print(numeros)
