numeros = []
par = []
impar = []
numeros.append(par)
numeros.append(impar)
for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}º valor: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')
