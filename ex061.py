pt = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
c = 0
while c < 10:
    print(f' {pt}', end='')
    print(',' if c < 9 else '...', end='')
    c = c + 1
    r = pt + razao
    pt = r
print('FIM')
