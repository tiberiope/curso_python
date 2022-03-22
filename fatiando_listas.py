alimentos = ['Tomate', 'Batata', 'Uva', 'Banana', 'Ovos', 'Pão', 'Pizza']
print(alimentos)

#pega os elementos da posição 2 e 3
print(alimentos[2:4])

#pega da posição 2 até o final
print(alimentos[2:])

#pega da posição 0 até a 4
print(alimentos[:5])

#pega os elementos, pulando de 2 em 2
print(alimentos[::2])

#pega os 3 últimos elementos
print(alimentos[-3:])

print(alimentos)

#percorre a lista de alimentos e printa da posição 2 à 4
for alimento in alimentos[2:5]:
    print(alimento)
