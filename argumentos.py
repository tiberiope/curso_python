def animais(especie='cachorro', nome=''):
    especie = especie
    nome = nome
    print('Eu tenho um ' + especie + ' chamado: ' + nome)

animais('cachorro', 'Frevo')
animais(nome='Pretominha', especie='gato')

print('----------')

def nome_completo(primeiro_nome='', ultimo_nome='', nome_do_meio=''):
    primeiro_nome = primeiro_nome
    ultimo_nome = ultimo_nome
    nome_do_meio = nome_do_meio

    if nome_do_meio != '':
        print('O nome digitado foi: ' + primeiro_nome.title() + ' ' + nome_do_meio.title() + ' ' + ultimo_nome.title())
        ret_nome_completo = primeiro_nome.title() + ' ' + nome_do_meio.title() + ' ' + ultimo_nome.title()
    else:
        print('O nome digitado foi: ' + primeiro_nome.title() + ' ' + ultimo_nome.title())
        ret_nome_completo = primeiro_nome.title() + ' ' + ultimo_nome.title()

    return ret_nome_completo


ret_nome_completo = nome_completo(ultimo_nome='Pessoa', primeiro_nome='artur')
nome_completo(ultimo_nome='Pessoa', primeiro_nome='artur', nome_do_meio='tibério')
nome_completo('primeiro', 'ultimo', 'meio')


print(ret_nome_completo)

