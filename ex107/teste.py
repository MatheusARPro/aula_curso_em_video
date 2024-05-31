from ex107 import moedas


preço = float(input('Digite o preço do produto: R$'))
print(f'O dobro do preço é R${moedas.dobro(preço)}')
print(f'A metade do preço é R${moedas.metade(preço)}')
print(f'O preço aumentado em 10% é R${moedas.aumentar(preço, 10)}')
print(f'O preço diminuido em 13% é R${moedas.diminuir(preço, 13)}')
