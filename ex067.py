c = nt = r = 0
while True:
    nt = int(input('Digite o numero para ver a tabuada: '))
    print ('¥'*50)
    for c in range(1, 11):
        r = c * nt
        print(f'{nt:2} X {c:2} = {r:2}')
    print ('¥'*50) 
    continuar = input('Gostaria de continuar[S/N]: ') .upper().strip()[0]
    if continuar not in 'Ss':
        break
print ('¥'*50)
print ('Execução Finalizada!') 
