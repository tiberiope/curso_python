class Restaurante():
    '''Classe restaurante'''

    def __init__(self, restaurante_nome, tipo_cozinha):
        '''Inicializa os atributos restaurante_nome e tipo_cozinha.'''
        self.restaurante_nome = restaurante_nome
        self.tipo_cozinha = tipo_cozinha

    def restaurante_descricao(self):
        print('O nome do restaurante é: ' + self.restaurante_nome)
        print('O tipo de comida é: ' + self.tipo_cozinha)

    def restaurante_aberto(self):
        print('O restaurante ' + self.restaurante_nome + ' está aberto.')

restaurante1 = Restaurante('Bela Vista', 'italiana')
print(restaurante1.restaurante_nome)
print(restaurante1.tipo_cozinha)

restaurante1.restaurante_descricao()
restaurante1.restaurante_aberto()
print('----------')
restaurante2 = Restaurante('Sabor Regional', 'nordestina')
restaurante3 = Restaurante('Paulista', 'pastel')
restaurante4 = Restaurante('Sun Tzu', 'japonesa')

restaurante2.restaurante_descricao()
restaurante3.restaurante_descricao()
restaurante4.restaurante_descricao()

