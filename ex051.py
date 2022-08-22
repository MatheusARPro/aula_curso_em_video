pt = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
r = pt + (razao * 10)
for c in range(pt, r, razao):
    print(c)
