'''numeros = []
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
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')'''

#Sugestao do Guanabara
núm = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares foram: {núm[0]}')
print(f'Os valores impares foram: {núm[1]}')
