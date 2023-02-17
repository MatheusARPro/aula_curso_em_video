from random import randint
from time import sleep


jogos = []
jogo = []
print('~'*50)
print(f'\033[0:30:42m{"JOGOS-PARA-A-MEGA-SENA":-^50}\033[m')
print('~'*50)
resp = int(input('\033[0:36mQuantos jogos gostaria de fazer?\033[m '))
print(f'{"GERANDO OS SEUS JOGOS":-^50}')
for l in range(0, resp):
    for j in range(0, 6):
        valor = randint(1, 60)
        if valor in jogo:
            valor = randint(1, 60)
            jogo.append(valor)
        else:
            jogo.append(valor)
    jogos.append(jogo[:])
    jogo.clear()
for jo in range(0 , len(jogos)):
    print('Processando...')
    sleep(2)
    print(f'\33[0:35:40mJogo {jo+1}: {sorted(jogos[jo])}\033[m')
print(f'{"JOGUE COM SABEDORIA":-^50}')
print('~'*50)
