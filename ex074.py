from random import randint

'''numaleatorio = (randint(0,100), randint(0,100), randint(0, 100), randint(0, 100), randint(0,100))
print(f'Numeros Gerados: {numaleatorio}')
menor = 101
maior = 0
for num in range(0, len(numaleatorio)):
    if numaleatorio[num] > maior:
        maior = numaleatorio[num]
    if numaleatorio[num] < menor:
        menor = numaleatorio[num]
print(f'O maior numero gerado foi: {maior}')
print(f'O menor numero gerado foi: {menor}')'''

#resoluçao do Guanabara
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteado foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi; {min(numeros)}')