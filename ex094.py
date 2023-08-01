# pessoas = {}
# lista_pessoa = []
# lista_mulher = []
# acima_media = []
# soma_media = 0
# media = 0
# while True:
#     pessoas['Nome'] = str(input('Nome: '))
#     pessoas['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
#     pessoas['Idade'] = int(input('Idade: '))
#     lista_pessoa.append(pessoas.copy())
#     while True:
#         continuar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
#         if 'S' in continuar or 'N' in continuar:
#             break
#     if continuar in 'N':
#         break
# print('=*=' *20)
# print(f'-Total de pessoas adastradas: {len(lista_pessoa)}')
# for p in range(0, len(lista_pessoa)):
#     soma_media += lista_pessoa[p]['Idade']
# media = soma_media / len(lista_pessoa)
# print(f'-Média de idade do grupo: {media:.2f}')
# for p in range(0, len(lista_pessoa)):
#     if lista_pessoa[p]['Sexo'] in 'F':
#         lista_mulher.append(lista_pessoa[p]['Nome'][:])
# print(f'-Mulheres cadastradas: {lista_mulher}')
# for p in range(0 , len(lista_pessoa)):
#     if lista_pessoa[p]['Idade'] > media:
#         acima_media.append(lista_pessoa[p])
# print('-Pessoas com idade acima da média:')
# for p in range(0, len(acima_media)):
#     print(f'  Nome: {acima_media[p]["Nome"]} ', end=';')
#     print(f'Sexo: {acima_media[p]["Sexo"]} ', end=';')
#     print(f'Idade: {acima_media[p]["Idade"]} ', end=';')
#     print()
# print('<< ENCERRADO >>')


#Solução do Guanabara
pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp= str(input('Quer continuar? [N/S] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if resp == 'N':
        break
print('-=' *30)
print(f'A) Ao todo foram temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ' , end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'lista das pessoa que estão acima da media: ' , end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ' , end='')
        print()
print('<<ENCERRADO>>')
