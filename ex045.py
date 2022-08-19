from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL' , 'TESOURA')
print(f'''{'%%' * 5}---JOKENPO---{'%%' * 5}
[0] == PEDRA
[1] == PAPEL
[2] == TESOURA''')
jogador = int(input('escolha: '))

if jogador >= 3:
    print('JOGADA INVÁLIDA!')

computador = randint(0, 2)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)



print('><[]><'* 10)
print(f'ESCOLHAS: COMPUTADOR {itens[computador]} X JOGADOR {itens[jogador]}')
print('><[]><'* 10)
if computador == 0: #PEDRA
    if jogador == 0:
        print(f'''EMPATE!!!!!''')
    elif jogador == 1:
        print(f'''JOGADOR VENCEU!!!!!''')
    elif jogador == 2:
        print(f'''COMPUTADOR VENCEU!!!!!''')
elif computador == 1: #PAPEL
    if jogador == 0:
        print(f'''COMPUTADOR VENCEU!!!!!''')
    elif jogador == 1:
        print(f'''EMPATE!!!!!''')
    elif jogador == 2:
        print(f'''JOGADOR VENCEU!!!!!''')
elif computador == 2: #TESOURA
    if jogador == 0:
        print(f'''JOGADOR VENCEU!!!!!''')
    elif jogador == 1:
        print(f'''COMPUTADOR VENCEU!!!!!''')
    elif jogador == 2:
        print(f'''EMPATE!!!!!''')
print('><[]><'* 10)
