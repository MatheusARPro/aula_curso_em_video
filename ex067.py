c = nt = r = 0
while True:
    nt = int(input('Digite o numero para ver a tabuada: '))
    print ('¥'*40)
    if nt < 0:
        break
    for c in range(1, 11):
        r = c * nt
        print(f'{nt:2} X {c:2} = {r:2}')
    print ('¥'*40)
print ('Execução Finalizada!')
