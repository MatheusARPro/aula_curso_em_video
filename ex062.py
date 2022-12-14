'''pt = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
c = 0
while c < 10:
    print(f' {pt}', end='')
    print(',' if c < 9 else '...', end='')
    c = c + 1
    r = pt + razao
    pt = r
n = 1
while n != 0:
    n = int(input('''#Gostaria de ver mais termos?
#Digite a quantidade ou Digite "0" para finalizar:'''))
'''
    if n == 0:
        print('Finalizado!!')
    else:
        n1 = c + n
        while c < n1:
            print(f' {pt}', end='')
            print(',' if c < n1 else '...', end='')
            c = c + 1
            r = pt + razao
            pt = r
'''



pt = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
termo = pt
c = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while c < total:
        print(f' {termo}', end='')
        print(',' if c < 9 else '...', end='')
        termo += razao
        c = c + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?  '))
print(f'Progressão finalizada com {total} termos mostrados.')
