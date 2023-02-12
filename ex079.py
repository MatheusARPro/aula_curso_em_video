valores = []
while True:
    valor = int(input('digite um valor: '))
    if valor in valores:
        print('Número duplicado,não vou adicionar!')
    else:
        valores.append(valor)
    while True:
        continuar = str(input('Quer continuar [S/N] ?')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print(f'Os numeros digitados foram: {sorted(valores)}')