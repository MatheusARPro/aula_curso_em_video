soma = 0
for c in range(0, 6):
    numero = input('Digite um valor: ')
    if numero.isnumeric():
        if int(numero) % 2 == 0:
            soma += int(numero)
print(f'A soma dos numeros pares é igual a {soma}')
