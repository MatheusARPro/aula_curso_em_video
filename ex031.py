dis = int(input('Qual vai ser a ditancia da viagem em quilometros(km): '))

if dis <= 200:
    preco = dis * 0.5
    print(f'O preço da viagem será de R${preco}')
else:
    preco = dis * 0.45
    print(f'O preço da viage será de R${preco}')