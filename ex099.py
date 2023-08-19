#impotações
from time import sleep


#funções
def linha():
    print('-=-' * 25)


def maior(*num):
    tamanho = len(num)
    print('Analisando os valores passados...')
    for numero in num:
        print(f'{numero},', end='')
        sleep(0.5)
    print(f'Foram passados no total {tamanho} numeros ao todo.')
    maior_numero = 0
    sleep(0.5)
    for numero in num:
        if numero >= maior_numero:
            maior_numero = numero
    print(f'O maior numero passado foi o {maior_numero}')


#codigo
linha()
maior(1, 2, 3, 5, 10)
linha()
maior(30, 45, 76, 14, 43, 98, 20)
linha()
maior(3, 7, 9, 1, 2, 4, 9, 3)
linha()