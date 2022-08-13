'''from calendar import isleap

ano = int(input('Digite um ano: '))

if isleap(ano) == True:
    print(f'O ano {ano} é um ano Bissexto!')
else:
    print(f'O ano {ano} não é um ano bissexto!')
'''

from datetime import date


ano = int(input('Que ano gostaria de analisar? Coloque 0 para o ano atual. '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} NÃO é bissexto!')
