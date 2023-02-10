times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('#'*105)
print('{:^105}'.format('Brasileirão'))
print(f'Os 5 primeiros colocado são: \n{times[0:5]}')
print('+'*105)
print(f'Os 4 ultimos colocados são: \n{times[16:]}')
print('+'*105)
print(f'Lista Alfabética: \n{sorted(times)}')
print('+'*105)
if 'Chapecoense' in times:
    posicao = times.index('Chapecoense') + 1
    print(f'O Chapecoense esta na {posicao}ª posição!')
else:
    print('O Chapecoense não esta entre os 20 primeiros colocados do Brasileirão! ')
print('#'*105)
