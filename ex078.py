valores = list()
maior = 0
menor = float('inf')
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if valores[cont] > maior:
        maior = valores[cont]
    if valores[cont] < menor:
        menor = valores[cont]
print(f'os valores digitados foran: {valores}')
print(f'O maior valor foi o valor {maior} nas posições ',end='')
'''for c in range(0, len(valores)):
    if valores[c] == maior:
        print(f'{valores.index(maior, c)}...',end='')'''
#Sugestao do Guanabara
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'\nO menor valor foi o valor {menor} nas posições ',end='')
'''for c in range(0, len(valores)):
    if valores[c] == menor:
        print(f'{valores.index(menor, c)}...',end='')'''
#sugestao do Guanabara
for i , v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
