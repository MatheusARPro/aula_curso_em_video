from random import randint
from time import sleep

num_sort = randint(0, 10)
tentativa = 0
escolha = 's'
print('#' * 55)
while escolha != num_sort:
    print('Estou pensando em um número!')
    escolha = int(input('Qual número de 0 a 10 eu estou "pensando"? '))
    print('PROCESSANDO...')
    sleep(1)
    tentativa = tentativa + 1
    if escolha == num_sort:
        print('PARABÉNS!!!!Você venceu!')
    else:
        print('TENTE NOVAMENTE!!!')
        if escolha < num_sort:
            print('TENTE UM NUMERO MAIOR!!!')
        else:
            print('TENTE UM NUMERO MENOR!!!')
    print('#' * 55)
print(f'VOCÊ ACERTOU APÓS {tentativa} TENTATIVA(S)!!! ')
print('#' * 55)
