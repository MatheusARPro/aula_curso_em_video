from random import randint

resultado = int
print('-*-' *20)
print('PAR OU IMPAR')
print('-*-' * 20)
while True:
    escolha = str(input('Escolha Par ou Impar [P/I]: ').upper().strip()[0])
    computador = randint(1, 10)
    jogador = int(input('Digite sua jogada: '))
    resultado = computador + jogador
    tot = resultado
    if resultado % 2 == 0:
        if 'P' in escolha:
            print('---' *20)
            print(f'O Computador jogou {computador}, o total foi {resultado}, deu PAR!! ')
            print('Você venceu!!!')
            print('nContinue...')
            print('---' * 20)
        else:
            print('---' * 20)
            print(f'O Computador jogou {computador}, o total foi {resultado}, deu PAR!! ')
            print('Você perdeu!!!')
            print('---' * 20)
            break
    else:
        if 'I' in escolha:
            print('---' * 20)
            print(f'O Computador jogou {computador}, o total foi {resultado}, deu IMPAR!! ')
            print('Você venceu!!!')
            print('Continue...')
            print('---' * 20)
        else:
            print('---' * 20)
            print(f'O Computador jogou {computador}, o total foi {resultado}, deu IMPAR!! ')
            print('Você perdeu!!!')
            print('---' * 20)
            break
    print('O jogo acabou!!!')
