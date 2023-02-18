cadastro = list()
dados = list()
pesado = list()
leves = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso[Kg]: ')))
    cadastro.append(dados[:])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    dados.clear()
    if resp in 'N':
        break
print('-=-'*30)
print(f'foram cadastradas {len(cadastro)} pessoas.')
for p in cadastro:
    if p[1] <= 70:
        leves.append(p[0])
    elif p[1] >= 90:
        pesado.append(p[0])
print(f'Das pessoas cadastradas, {len(leves)} são mais leves, com peso igual ou inferior a 70Kg, são elas:\n{leves}')
print(f'Das pessoas cadastradas, {len(pesado)} são mais pesadas, com peso igual ou superior a 90Kg,são elas:\n{pesado}')
