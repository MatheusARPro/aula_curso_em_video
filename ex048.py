soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 == 1:
        i = c
        if i % 3 == 0:
            soma = soma + i
            cont = cont + 1
print(f'A soma dos {cont} numeros impares, divisiveis por 3 no intervalo de 1 a 500 é {soma}')
