cs = int(input('Quntos termos gostaria de ver? '))
pt = 0
st = 1
print(f'{pt} - {st} - ', end='')
c = 2
while c != cs:
    ts = pt + st
    print(f'{ts} - ', end='')
    c = c + 1
    pt = st
    st = ts
print('FIM.')
