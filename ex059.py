c = 0
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
while c != 5:
    print('---' * 10)
    print('''Oque deseja fazer agora?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    c = int(input('Digite a sua opção: '))
    if c == 1:
        r = n1 + n2
        print(f'{n1} + {n2} = {r}')
    elif c == 2:
        r = n1 * n2
        print(f'{n1} X {n2} = {r}')
    elif c == 3:
        if n1 > n2:
            print(f'{n1} e maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} e maior que {n1}.')
    elif c == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outor valor: '))
    elif c < 1 and c > 5:
        print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
print('OBRIGADA ')
