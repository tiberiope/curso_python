#Ou: import carros
#Ou: from carros import *
from carros import Carros, CarrosEletricos

#Ou: meu_carro1 = carros.Carros('ferrari', 'M50', 2016)
meu_carro1 = Carros('ferrari', 'M50', 2016)
meu_carro1.carro_descricao()
meu_carro1.carro_leia_odometro()

print('----------\nMudando o odômetro: ')
meu_carro1.odometro = 5
meu_carro1.carro_leia_odometro()

print('----------\nMudando odômetro por parâmetro: ')
meu_carro1.carro_altera_odometro(15)
meu_carro1.carro_leia_odometro()

print('----------\nIncrementa o odômetro: ')
meu_carro1.carro_incrementa_odometro(102)
meu_carro1.carro_leia_odometro()

print('----------\nIncrementa o odômetro: ')
meu_carro1.carro_incrementa_odometro(24)
meu_carro1.carro_leia_odometro()

print('----------\nMinha moto: ')
meu_carro2 = Carros('Kawazaki', 'Ninja', 2014)
meu_carro2.carro_descricao()
meu_carro2.carro_altera_odometro(14000)
meu_carro2.carro_leia_odometro()
meu_carro2.carro_incrementa_odometro(200)
meu_carro2.carro_leia_odometro()

print('----------\n')
carro1 = Carros('Jeep', 'Wrangler', 2000)
carro1.carro_gasolina()

print('----------')
carro_eletrico1 = CarrosEletricos('Tesla', 'S', 2016)
carro_eletrico1.carro_descricao()
carro_eletrico1.carro_incrementa_odometro(130)
carro_eletrico1.carro_leia_odometro()
carro_eletrico1.carro_gasolina()

print('----------')

carro_eletrico1 = CarrosEletricos('Honda', 'Civic', 2016)
carro_eletrico1.carro_descricao()
carro_eletrico1.bateria.descreve_bateria()
carro_eletrico1.bateria.altera_bateria(15)
print('----------')
carro_eletrico2 = CarrosEletricos('Jeep', 'Willys', 1950)
carro_eletrico2.carro_descricao()
carro_eletrico2.bateria.descreve_bateria()
carro_eletrico2.pneus.descreve_pneus()
carro_eletrico2.pneus.altera_pneus(33,31,28,29)
carro_eletrico2.pneus.descreve_pneus()