from random import randint
from time import sleep

# resultados = {'Jogador 1': randint(1,6),
#            'Jogador 2': randint(1,6),
#            'Jogador 3': randint(1,6),
#            'Jogador 4': randint(1,6)
#            }
# for key,value in resultados.items():
#     print(f'O {key} tirou o valor {value}!')
#     sleep(0.8)
#
# resultados_ordenados = sorted(resultados.items(), key= lambda item: item[1], reverse=True)
# print(f'{"RANKING":-^30}')
# for j , p in enumerate(resultados_ordenados):
#     print(f'{j+1}° colocado: {p[0]} com um valor {p[1]} no dado')
#     sleep(0.8)


#Resoluçao do Guanabara
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k ,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
    