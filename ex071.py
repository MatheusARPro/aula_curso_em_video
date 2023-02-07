'''  print('=' * 30)
print('{:^30}'.format('MARBank'))
print('=' * 30)
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

print('=' * 30)
print(f'Cédulas de 50 => {cinquenta}
Cédulas de 20 => {vinte}
Cédulas de 10 => {dez}
Cédulas de 1 => {um}')
print('=' * 30)
print('{:^30}'.format('Obrigado por usar o MARbank!'))
print('=' * 30)'''


#Resoluçao do Guanabara'
print('=' * 30)
print('{:^30}'.format('MARBank'))
print('=' * 30)
saque = int(input('valor do saque: R$ '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} de cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('{:^30}\n{:^30}'.format('Volte Sempre ao MARBank!','TENHA UM BOM DIA!!'))
print('=' * 30)