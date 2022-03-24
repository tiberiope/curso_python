convidados = []

for n in range(1,11):
    convidado = input('Digite o nome do convidado n° ' + str(n) + ': ')
    convidados.append(convidado)

convidados.sort()

print('Lista de convidados: ')
for convidado in convidados:
    print(convidado)