times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('#'*80)
print('{:^80}'.format('Brasileirão'))
print('#'*80)
print('Lista em ordem de classificação')
for t in times:
    print(t)
print('+'*80)
print(f'Os 5 primeiros colocado são:')
for t in times[:5]:
    print(t)
print('+'*80)
print(f'Os 4 ultimos colocados são: ')
for t in times[16:]:
    print(t)
print('+'*80)
print(f'Lista Alfabética:')
for t in sorted(times):
    print(t)
print('+'*80)
if 'Chapecoense' in times:
    posicao = times.index('Chapecoense') + 1
    print(f'O Chapecoense esta na {posicao}ª posição!')
else:
    print('O Chapecoense não esta entre os 20 primeiros colocados do Brasileirão! ')
print('#'*80)
