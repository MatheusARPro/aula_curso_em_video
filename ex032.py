from calendar import isleap

ano = int(input('Digite um ano: '))

if isleap(ano) == True:
    print(f'O ano {ano} é um ano Bissexto!')
else:
    print(f'O ano {ano} não é um ano bissexto!')
