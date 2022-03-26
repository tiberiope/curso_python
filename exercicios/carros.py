class Carros():
    #Representando um carro.

    def __init__(self, fabricante, modelo, ano):
        '''Método construtor de Carros. Inicializa os atributos que descrevem carro.'''

        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 100
        self.odometro = 0

    def carro_descricao(self):
        '''Devolve a descrição do carro.'''
        nome_longo = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
        print(nome_longo.title())

    def carro_leia_odometro(self):
        '''Exibe uma frase que mostra o valor do odômetro do carro.'''
        print('O carro tem ' + str(self.odometro) + ' KM rodados.')

    def carro_altera_odometro(self, novo_odometro):
        '''Altera o odômetro através do valor passado como argumento.'''
        self.odometro = novo_odometro

    def carro_incrementa_odometro(self, novo_odometro):
        '''Incrementa um novo valor ao odômetro.'''
        self.odometro += novo_odometro

    def carro_gasolina(self):
        '''Exibe a quantidade de gasolina no tanque.'''
        print('O tanque de combustível está com ' + str(self.combustivel) + '% da capacidade.')

class CarrosEletricos(Carros):
    '''Representa aspectos específicos de um carro elétrico.
    A classe Carros é a superclasse.
    A classe CarrosEletricos é a subclasse.'''
    def __init__(self, fabricante, modelo, ano):
        '''Construtor da classe CarrosEletricos. Inicializa os parâmetros.'''
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()
        self.pneus = Pneus()

    def carro_gasolina(self):
        print('Bateria com ' + str(self.combustivel) + '% da capacidade.')

class Bateria():
    '''Uma tentativa simples de criar uma bateria'''
    def __init__(self, bateria=100):
        '''Método construtor da classe bateria.'''
        self.bateria = bateria

    def descreve_bateria(self):
        print('A carga atual da bateria é: ' + str(self.bateria))

    def altera_bateria(self, carga_atual):
        '''Altera o valor da bateria.'''
        self.bateria = carga_atual
        print('A carga atual da bateria é: ' + str(self.bateria))

class Pneus():
    def __init__(self, lib_diant_esq=40, lib_diant_dir=40, lib_tras_esq=40, lib_tras_dir=40):
        self.lib_diant_esq = lib_diant_esq
        self.lib_diant_dir = lib_diant_dir
        self.lib_tras_esq = lib_tras_esq
        self.lib_tras_dir = lib_tras_dir

    def descreve_pneus(self):
        print('Pneu esquerdo dianteiro tem: ' + str(self.lib_diant_esq) + ' libras')
        print('Pneu esquerdo traseiro tem: ' + str(self.lib_tras_esq) + ' libras')
        print('Pneu direito dianteiro tem: ' + str(self.lib_diant_dir) + ' libras')
        print('Pneu esquerdo traseiro tem: ' + str(self.lib_tras_esq) + ' libras')

    def altera_pneus(self, lib_diant_esq, lib_diant_dir, lib_tras_esq, lib_tras_dir):
        self.lib_diant_esq = lib_diant_esq
        self.lib_diant_dir = lib_diant_dir
        self.lib_tras_esq = lib_tras_esq
        self.lib_tras_dir = lib_tras_dir






