'''n = int(input('Digite o numero que deseja calcular o fatorial: '))
while n < 0:
    print('NUMERO INVALIDO,TENTE NOVAMENTE!!!')
    n = int(input('Digite o numero que deseja calcular o fatorial: '))
if n == 0 or n == 1:
    print(f'{n}! = 1 ')
else:
    f = n
    fd = n
    while f > 1:
        f -= 1
        fd *= f
print(f'{n}! = {fd}')'''


'''n = int(input('Digite o numero que deseja calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' X ' if c > 1 else ' = ', end='' )
    f *= c
    c -= 1
print(f'{f}')'''


from  math import factorial
n = int(input('Digite o numero que deseja calcular o fatorial: '))
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(' X ' if c > 1 else ' = ', end='' )
    c -= 1
print(factorial(n))

