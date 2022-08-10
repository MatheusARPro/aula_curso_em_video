'''city = input('Qual sua cidade? ').upper().strip()

if 'SANTO' in city :
    print('O nome da sua cidade possui a palavra "Santo".')
else :
    print('O nome da sua cidade não possui a palavra "Santo"')
'''


'''c = input('Qual a sua cidade? ').upper().strip()

print('Existe Santo no nome da cidade?','SANTO' in c)
'''

cid = str(input('Em qu cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
