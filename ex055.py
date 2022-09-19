ma_peso = 0
me_peso = 0
nome1 = 0
nome2 = 0
for c in range(0, 5):
    print('++' * 20)
    peso = float(input('Peso: '))
    if c == 0:
        ma_peso = peso
        me_peso = peso
    else:
        if peso > ma_peso:
            ma_peso = peso
        if peso < me_peso:
            me_peso = peso
print(f'O maior pes foi {ma_peso}Kg \nO menor peso foi {me_peso}Kg')
