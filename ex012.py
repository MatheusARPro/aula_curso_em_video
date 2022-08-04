preço = float(input('Qual o preço do produto? R$'))
#novo preço recebe 5%¨de desconto
desconto = (preço / 100) * 5
npreço = preço - desconto
print('O novo preço do produto após o desconto de 5% é R${:.2f} .'.format(npreço))