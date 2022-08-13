from random import randint
from time import sleep

num_sort = randint(0, 5)
print('#'* 55)
print('Estou pensando em um número!')
escolha = int(input('Qual número de 0 a 5 eu estou "pensando"? '))
print('PROCESSANDO...')
sleep(3)
print('#'* 55)
if escolha == num_sort:
    print('PARABÉNS!!!!Você venceu!')
else:
    print('Que pena, você PERDEU!!!')
    print(f'Eu pensei no {num_sort} e não no número {escolha}!!')
print('#'* 55)
