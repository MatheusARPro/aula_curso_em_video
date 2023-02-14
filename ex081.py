valores = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if continua in 'N':
        break
print('-+-'*15)
print(f'Foram digitados {len(valores)} numeros.')
print(f'A ordem decrescente dos valores é {sorted(valores, reverse=True)}.')
if 5 in valores:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')
