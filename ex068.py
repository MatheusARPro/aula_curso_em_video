'''from random import randint

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
    print('O jogo acabou!!!')'''



#soluçao do Guananbara
#colocando pq achei interessante
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint( 0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ' , end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0 :
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!!Você venceu {v} vez(es).')