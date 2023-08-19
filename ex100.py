#importações
from random import randint


#variaveis
numeros = list()

#funções
def sorteio(lista):
    while len(numeros) < 5:
        numeros.append(randint(1, 20))
    for numero in range(0, len(numeros)):
        print(numero, end=' ')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    tamanho_lista = len(numeros)
    for numero in range(tamanho_lista):
        if numeros[numero] % 2 == 0:
            soma += numeros[numero]
    print(soma)



#codigo
print('Sorteando os valores da lista: ', end='')
sorteio(numeros)
print(f'Somando todos os valores pares de {numeros}, temos o resultado ', end='')
somaPar(numeros)