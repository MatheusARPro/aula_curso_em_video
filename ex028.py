from random import randint


num_sort = randint(0, 5)
escolha = int(input('Qual numero de 0 a 5 o programa esta "pensando"? '))

if escolha == num_sort:
    print('PARABÉNS!!!!Você venceu!')
else:
    print('Que pena, você PERDEU!!!')
    print(f'Eu estava pensando no numero {num_sort}!!')
