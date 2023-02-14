valores = []
while True:
    numero = int(input('Digite um valor: '))
    valores.append(numero)
    contin = ' '
    while contin not in 'SN':
        contin = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if contin in 'N':
        break
listapar = []
listaimpar = []
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        listapar.append(valores[c])
    else:
        listaimpar.append(valores[c])
print('-+-'*15)
print(f'Você digitou os valores {valores}')
print(f'Os valores pares são {listapar}')
print(f'Os valores impares são {listaimpar}')