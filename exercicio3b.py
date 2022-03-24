import exercicio3a

operacao = input('Digite a operação desejada (s = soma, sub = subtração, d = divisão, m = multiplicação: ')
if (operacao == 's') or (operacao == 'sub') or (operacao == 'd') or (operacao == 'm'):
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))

if operacao == 's':
    print(exercicio3a.soma(a, b))

elif operacao == 'sub':
    print(exercicio3a.sub(a, b))

elif operacao == 'd':
    print(exercicio3a.div(a, b))

elif operacao == 'm':
    print(exercicio3a.mult(a, b))

else:
    print('Operação não localizada!')
