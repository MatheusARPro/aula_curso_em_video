matriz = [[0, 0, 0,], [0, 0, 0,], [0, 0, 0,]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor na posição [{linha,coluna}]:'))
print('+' *30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]',end='')
    print()
print('+' *30)
somapar = somacoluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
        if linha == 0 or matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
for v in matriz:
    somacoluna += v[2]
print(f'A soma dos valores pares é igual a {somapar}')
print(f'A soma dos valores da coluna 3 é igual a {somacoluna}')
print(f'O maior valor da segunda linha é {maior}')
