from ex108 import moedas


preço = float(input('Digite o valor do produto: R$'))
print(f'O dobro do preço é R${moedas.moeda(moedas.dobro(preço))}')
print(f'A metade do preço é R${moedas.moeda(moedas.metade(preço))}')
print(f'o preço com 13% de desconto é R${moedas.moeda(moedas.diminuir(preço, 13))}')
print(f'O preço com acréscimo de 10% é R${moedas.moeda(moedas.aumentar(preço, 10))}')
