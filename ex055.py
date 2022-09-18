ma_peso = 0
me_peso = 0
nome1 = 0
nome2 = 0
for c in range(0, 5):
    print('++' * 20)
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    if peso >= ma_peso:
        ma_peso = peso
        nome1 = nome
    else:
        if peso <= me_peso:
            me_peso = peso
            nome2 = nome
print(f'O mais pesado foi {nome1} com {ma_peso}Kg \nO mais leve foi {nome2} com {me_peso}Kg')
