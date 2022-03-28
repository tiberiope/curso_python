import exercicio3a

continuar = 's'
while continuar.lower() == 's':
    escolha = input("Escolha P para par ou I para impar: ")
    a = int(input("Escolha o primeiro valor: "))
    b = int(input("Escolha o segundo valor: "))

    if (escolha.upper() == 'I'):
        if exercicio3a.div_resto(exercicio3a.soma(a,b), 2) == 1:
            print('Deu IMPAR... Parabéns, você venceu!')
        else:
            print('Deu PAR... Você perdeu!')

    elif (escolha.upper() == 'P'):
        if exercicio3a.div_resto(exercicio3a.soma(a,b), 2) == 0:
            print('Deu PAR... Parabéns, você venceu!')
        else:
            print('Deu IMPAR... Você perdeu!')

    continuar = input('Deseja jogar novamente? s para sim: ')