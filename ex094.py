pessoas = {}
lista_pessoa = []
lista_mulher = []
acima_media = []
soma_media = 0
media = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    pessoas['Idade'] = int(input('Idade: '))
    lista_pessoa.append(pessoas.copy())
    while True:
        continuar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
        if 'S' in continuar or 'N' in continuar:
            break
    if continuar in 'N':
        break
print('=*=' *20)
print(f'Total de pessoas adastradas: {len(lista_pessoa)}')
for p in range(0, len(lista_pessoa)):
    soma_media += lista_pessoa[p]['Idade']
media = soma_media / len(lista_pessoa)
print(f'Média de idade do grupo: {media:.2f}')
for p in range(0, len(lista_pessoa)):
    if lista_pessoa[p]['Sexo'] in 'F':
        lista_mulher.append(lista_pessoa[p]['Nome'][:])
print(f'Mulheres cadastradas: {lista_mulher}')
for p in range(0 , len(lista_pessoa)):
    if lista_pessoa[p]['Idade'] > media:
        acima_media.append(lista_pessoa[p]['Nome'])
print(f'Pessoas com idade acima da média: {acima_media}')
