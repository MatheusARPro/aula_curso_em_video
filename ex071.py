print('-_-_-' * 5)
print('       MARBank   ')
print('-_-_-' * 5)
saque = int(input('valor do saque: R$ '))

cinquenta = vinte = dez = um = 0

while True:
    #calcula nota de 50
    while True:
        if saque >= 50 :
            saque -= 50
            cinquenta += 1
        else:
            break
    #calcula nota de 20
    while True:
        if saque >= 20:
            saque -= 20
            vinte += 1
        else:
            break
    #calcula nota de 10
    while True:
        if saque >= 10:
            saque -= 10
            dez += 1
        else:
            break
    #calcula nota de 1
    while True:
        if saque >= 1:
            saque -= 1
            um += 1
        else:
            break
    break

print('-_-_-' * 5)
print(f'''Cédulas de 50 => {cinquenta}
Cédulas de 20 => {vinte}
Cédulas de 10 => {dez}
Cédulas de 1 => {um}''')
print('-_-_-' * 5)
print('Obrigado por usar o MARbank!')
print('-_-_-' * 5)
