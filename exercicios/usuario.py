class Usuario():
    '''classe de usuários'''

    def __init__(self, primeiro_nome, ultimo_nome, idade, altura, nacionalidade):
        '''Inicializa os atributos teste e teste1.'''
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.altura = altura
        self.nacionalidade = nacionalidade

    def usuario_descricao(self):
        print('O usuário ' + self.primeiro_nome + ' ' + self.ultimo_nome + ' é ' + self.nacionalidade +
              ', tem ' + str(self.idade) + ' de idade e ' + str(self.altura) + ' m de altura.' )

    def usuario_saudacao(self):
        print('Bem-vindo, ' + self.primeiro_nome + '!')

usuario1 = Usuario('Artur', 'Pessoa', 33, 1.80, 'brasileiro')

usuario1.usuario_saudacao()
usuario1.usuario_descricao()