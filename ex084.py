cadastro = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso[Kg]: ')))
    if len(cadastro) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    cadastro.append(dados[:])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    dados.clear()
    if resp in 'N':
        break
print('-=-'*30)
print(f'foram cadastradas {len(cadastro)} pessoas.')
print(f'O maior peso foi {mai}Kg, que pertence a ',end='')
for p in cadastro:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso {men}Kg, que pertence a ',end='')
for p in cadastro:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
