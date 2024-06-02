from ex109 import moedas


preço = float(input('Qual o preço do produto: R$'))
print(f'O dobro do preço é R${moedas.dobro(preço, True)}')
print(f'A Metade do preço é R${moedas.metade(preço, True)}')
print(f'O preço do produto com aumento de 13% é R${moedas.aumentar(preço, 13, True)}')
print(f'O preço com desconto de 10% é R${moedas.diminuir(preço, 10, True)}')
