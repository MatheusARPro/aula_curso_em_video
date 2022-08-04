lar = float(input('Qual a largura da parede? ' ))
alt = float(input('Qual a altura da parede? '))
area = lar * alt
#1 litro de tinta cobre area de 2m²
tinta = area / 2
print('Para cobrir a parede serao nescessarios {:.3f } litros de tinta.'.format(tinta))