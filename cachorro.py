class Cachorro():
    '''Uma tentativa simples de modelar um cachorro.'''

    def __init__(self, nome, idade):
        '''Inicializa os atributos nome e idade'''
        self.nome = nome
        self.idade = idade

    def sentar(self):
        '''Simula um cachorro sentando, em resposta a um comando.'''
        print(self.nome.title() + ' está sentando.')

    def rolar(self):
        '''Simula um cachorro rolando'''
        print(self.nome.title() + ' está rolando.')

meu_cachorro = Cachorro('Aquiles', 6)

meu_cachorro.rolar()
meu_cachorro.sentar()

outro_cachorro = Cachorro('Bingo', 8)

outro_cachorro.rolar()
outro_cachorro.sentar()