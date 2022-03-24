from exercicio3a import soma
escolha = input("Escolha P para par ou I para impar: ")
a = int(input("Escolha o primeiro valor: "))
b = int(input("Escolha o segundo valor: "))


if (escolha.upper() == 'I'):
    if (soma(a,b) % 2 == 1):
        print('Deu IMPAR... Parabéns, você venceu!')
    else:
        print('Deu PAR... Você perdeu!')

elif (escolha.upper() == 'P'):
    if (soma(a,b) % 2 == 0):
        print('Deu PAR... Parabéns, você venceu!')
    else:
        print('Deu IMPAR... Você perdeu!')