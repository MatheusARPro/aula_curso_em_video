# #variaveis
# inicio = fim = passo = 0
#
#
# #funções
# def linha():
#     print('=' * 40)
#
#
# def contador(inicio, fim, passo):
#     if passo == 0:
#         passo = 1
#     if inicio > fim:
#         while inicio > fim:
#             print(inicio, end=' ')
#             inicio -= passo
#         print('FIM!')
#     else:
#         fim += 1
#         for numero in range(inicio, fim, passo):
#             print(numero, end=' ')
#         print('FIM!')
#
#
# #codigo
# linha()
# print('Contagem de 1 ate 10 de 1 em 1: ')
# contador(1, 10, 1)
# linha()
# print('Contagem de 10 ate 0 de 2 em 2: ')
# contador(10, 0, 2)
# linha()
# print('Agora é sua vez de personalizar a contagem,vamos la!')
# inicio = int(input('Início: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))
# linha()
# contador(inicio, fim, passo)
# linha()


#Soluçao do Guanabara

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont  >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
