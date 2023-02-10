from random import randint

numaleatorio = (randint(0,100), randint(0,100), randint(0, 100), randint(0, 100), randint(0,100))
print(f'Numeros Gerados: {numaleatorio}')
menor = 101
maior = 0
for num in range(0, len(numaleatorio)):
    if numaleatorio[num] > maior:
        maior = numaleatorio[num]
    if numaleatorio[num] < menor:
        menor = numaleatorio[num]
print(f'O maior numero gerado foi: {maior}')
print(f'O menor numero gerado foi: {menor}')
