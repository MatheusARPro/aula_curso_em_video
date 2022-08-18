from random import randint
from time import sleep


print(f'''{'%%' * 5}---JOKENPO---{'%%' * 5}
[0] == PEDRA
[1] == PAPEL
[2] == TESOURA''')
jogador = int(input('escolha: '))

PEDRA = 0
PAPEL = 1
TESOURA = 3

sleep(2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

computador = randint(0, 2)
print('><[]><'* 5)
print(f'ESCOLHAS: CPU {computador} X JOGADOR {jogador}')
print('><[]><'* 5)
if computador == PEDRA:
    if jogador == PEDRA:
        print(f'''EMPATE!!!!!''')
    elif jogador == PAPEL:
        print(f'''JOGADOR VENCEU!!!!!''')
    elif jogador == TESOURA:
        print(f'''CPU VENCEU!!!!!''')
elif computador == PAPEL:
    if jogador == PEDRA:
        print(f'''CPU VENCEU!!!!!''')
    elif jogador == PAPEL:
        print(f'''EMPATE!!!!!''')
    elif jogador == TESOURA:
        print(f'''JOGADOR VENCEU!!!!!''')
elif computador == TESOURA:
    if jogador == PEDRA:
        print(f'''JOGADOR VENCEU!!!!!''')
    elif jogador == PAPEL:
        print(f'''CPU VENCEU!!!!!''')
    elif jogador == TESOURA:
        print(f'''EMPATE!!!!!''')
else:
    print('ESCOLHA INVÁLIDA!')
print('><[]><'* 5)
