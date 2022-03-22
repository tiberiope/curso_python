alimentos = ['Tomate', 'Batata', 'Uva', 'Banana', 'Ovos', 'Pão', 'Pizza']

#a lista "alimentos2" sofre alteração quando a lista "alimentos" é modificada.
alimentos2 = alimentos
alimentos.append("Chocolate")
alimentos.sort(reverse=True)
print(alimentos2)
print(alimentos)

#a lista "alimentos2" não sofre alteração quando a lista "alimentos" é modificada.
alimentos2 = alimentos[:]
alimentos.sort()
alimentos.append("Suco")
print(alimentos2)
print(alimentos)