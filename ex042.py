r1 = float(input('Medida da primeira reta: '))
r2 = float(input('Medida da segunda reta: '))
r3 = float(input('Medida da terceira reta: '))

t1 = r1 + r2
t2 = r1 + r3
t3 = r3 + r2

p1 = t1 > r3
p2 = t2 > r2
p3 = t3 > r1

equilatero = r1 == r2 == r3
isoceles = r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1
escaleno = r1 != r2 != r3 != r1

if p1 and p2 and p3:
    print('-=-'*15)
    print('As retas podem formar um triângulo!')
    if equilatero:
        print('TIPO DO TRIÂNGULO: EQUILÁTERO')
    elif isoceles:
        print('TIPO DO TRIÂNGULO: ISÓSCELES')
    elif escaleno:
        print('TIPO DO TRIÂNGULO: ESCALENO')
    print('-=-' * 15)
else:
    print('As retas acima não forma um triângulo.')
