'''continua = True
while continua:
    numero = int(input('Digite um numero: '))
    if numero <= 1 and numero % 2 == 0:
        print('Este número não pode ser PRIMO.')
    else:
        primo = False
        for numero_indice in range(2, numero):
            if numero % numero_indice == 0:
                ...  # É a mesma coisa de "pass"
            else:
                primo = True
        if primo is True:
            print('Com certeza este número é primo.')
        else:
            print('Este número não é primo.')
    continuar = int(input("Quer continuar? Digite 0 para sim e 1 para não: "))
    if continuar == 1:
        continua = False'''


num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[031m', end='')
    print(f'{c} ',  end='')
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('e por isso ele NÃO É PRIMO!')