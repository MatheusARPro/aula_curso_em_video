n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O valor {n1} é maior que o valor {n2}')
elif n2 > n1:
    print(f'O valor {n2} é maior que o valor {n1}')
else:
    print(f'Não existe valor maior, os valores "{n1}" e "{n2}" são iguais')
