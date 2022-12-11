n = int(input('Digite o numero que deseja calcular o fatorial: '))
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
print(f'{n}! = {fd}')
