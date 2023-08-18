# Variables
inicio = fim = passo = 0


# Functions
def linha():
    print('=' * 40)


def contador(inicio, fim, passo):
    if inicio > fim:
        while inicio > fim:
            print(inicio, end=' ')
            inicio -= passo
        print('FIM!')
    else:
        for numero in range(inicio, fim, passo):
            print(numero, end=' ')
        print('FIM!')


# code
linha()
print('Contagem de 1 ate 10 de 1 em 1: ')
contador(1, 11, 1)
linha()
print('Contagem de 10 ate 0 de 2 em 2: ')
contador(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem,vamos la!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contador(inicio, fim, passo)
linha()
