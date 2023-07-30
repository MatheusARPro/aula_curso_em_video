# jogador = {}
# nome = str(input('Nome do Jogador: '))
# partida = int(input(f'Quantas partidas {nome} jogou? '))
# partidas = 0
# total = 0
# lista_gol = []
# while partidas < partida:
#     gols = int(input(f'Quantos gols na {partidas +1}ª? '))
#     partidas += 1
#     total += gols
#     lista_gol.append(gols)
# jogador['Nome'] = nome
# jogador['Gols'] = lista_gol
# jogador['Total de gols'] = total
# print('-=-' *15)
# print(jogador)
# print('-=-' *15)
# for key , value in jogador.items():
#     print(f'{key}: {value}')
# print('-=-' *15)
# print(f'O jogador {nome} jogou no total {partidas} partidas.')
# for gol in range(0, partida):
#     print(f'    => Na {gol+1}ª partida, fez {lista_gol[gol]} gols.')
# print(f'Foi no total de {total} gols.')
# print('-=-' *15)
#
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0,  tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador['gols']):
    print(f'   =>Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
