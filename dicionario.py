alien_0 = {'cor': 'verde', 'pontuacao': 5}
print('Cor: ' + alien_0['cor'])
print('Pontuação: ' + str(alien_0['pontuacao']))

alien_0['cor'] = 'azul'
alien_0['pontuacao'] = 10

print('Nova cor: ' + alien_0['cor'])
print('Nova pontuação: ' + str(alien_0['pontuacao']))
print('----------')
print(alien_0)

alien_0['posicao_x'] = 0
alien_0['posicao_y'] = 25
print(alien_0)

alien_0['qualquer'] = 'erro!'
print(alien_0)

del alien_0['qualquer']
print(alien_0)

for atributo, valor in alien_0.items():
    print('Atributo: ' + atributo)
    print('Valor: ' + str(valor) + '\n')

