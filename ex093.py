jogador = {}
nome = str(input('Nome do Jogador: '))
partida = int(input(f'Quantas partidas {nome} jogou? '))
partidas = 0
total = 0
lista_gol = []
while partidas < partida:
    gols = int(input(f'Quantos gols na {partidas +1}ª? '))
    partidas += 1
    total += gols
    lista_gol.append(gols)
jogador['Nome'] = nome
jogador['Gols'] = lista_gol
jogador['Total de gols'] = total
print('-=-' *15)
for key , value in jogador.items():
    print(f'{key}: {value}')
print('-=-' *15)
print(f'O jogador {nome} jogou no total {partidas} partidas.')
for gol in range(0, partida):
    print(f'    => Na {gol+1}ª partida, fez {lista_gol[gol]} gols.')
print(f'Foi no total de {total} gols.')
print('-=-' *15)
