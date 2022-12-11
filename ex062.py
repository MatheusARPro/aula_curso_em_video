pt = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
c = 0
while c < 10:
    print(pt)
    c = c + 1
    r = pt + razao
    pt = r
n = 1
while n != 0:
    n = int(input('''Gostaria de ver mais termos?
Digite a quantidade ou Digite "0" para finalizar:'''))
    if n == 0:
        print('Finalizado!!')
    else:
        n1 = c + n
        while c < n1:
            print(pt)
            c = c + 1
            r = pt + razao
            pt = r