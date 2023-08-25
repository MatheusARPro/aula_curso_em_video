#impotações
from time import sleep


#funções
# def linha():
#     print('-=-' * 25)
#
#
# def maior(*num):
#     tamanho = len(num)
#     print('Analisando os valores passados...')
#     for numero in num:
#         print(f'{numero},', end='')
#         sleep(0.5)
#     print(f'Foram passados no total {tamanho} numeros ao todo.')
#     maior_numero = 0
#     sleep(0.5)
#     for numero in num:
#         if numero >= maior_numero:
#             maior_numero = numero
#     print(f'O maior numero passado foi o {maior_numero}')
#
#
# #codigo
# linha()
# maior(1, 2, 3, 5, 10)
# linha()
# maior(30, 45, 76, 14, 43, 98, 20)
# linha()
# maior(3, 7, 9, 1, 2, 4, 9, 3)
# linha()


#Soluçao do guanabara
#função
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados ...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados  {cont}  valores ao topo.')
    print(f'o maior valor informado foi {maior}')


#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)