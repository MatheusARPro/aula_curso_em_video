'''soma = 0
c = 0
maior = 0
menor = 0
media = 0
continua = 5
while continua != 1:
    n = int(input('Digite um numero:'))
    soma = soma + n
    c = c + 1

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = int(input('Gostaria de continuar?Digite 0 Para sim e 1 para Nao. '))
    if continua != 0 and continua != 1:
        print ('Opçao invalida!!!')
        continua = int(input('Gostaria de continuar?Digite 0 Para sim e 1 para Nao. '))

media = soma / c .__float__()'''
#print(f'''A media entre os numeros digitados e igual a {media}
#O maior numero foi {maior} e o menor numero foi {menor}''')


resp = 's'
media = quant = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} numeros, e a média foi {media:.2f}.')
print(f'O maior numero foi {maior}, e o menor numero foi {menor}')
