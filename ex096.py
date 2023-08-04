def mostralinha():
    print('-'*60)


def area():
    area = com * lar
    print(f'A área total do terreno {com} X {lar} e de {area}m².')


mostralinha()
print(f'{"CONTROLE DE TERRENO":^60}')
mostralinha()
com = float(input('Comprimento do terreno (m): '))
lar = float(input('Largura do terreno (m): '))
area()
mostralinha()
