dias= int(input('Por quantos dias o carro ficou alugado? '))
km = float(input('Quantos quilometros foram percorridos nesse periodo? '))
totpag = (dias * 60) + (km * 0.15)
print('O carro que foi alugado por {} dias e percorreu {}km, tera um custo total de aluguel igual a R${:.2f}'.format(dias, km, totpag))