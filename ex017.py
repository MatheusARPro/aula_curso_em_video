from math import hypot
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
print('A hypotenusa e igual a {:.2f}'.format(hypot(co, ca)))