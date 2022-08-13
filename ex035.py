r1 = float(input('Medida da primeira reta: '))
r2 = float(input('Medida da segunda reta: '))
r3 = float(input('Medida da terceira reta: '))

t1 = r1 + r2
t2 = r1 + r3
t3 = r3 + r2

p1 = t1 > r3
p2 = t2 > r2
p3 = t3 > r1

if p1 and p2 and p3:
    print('As retas podem forma um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
