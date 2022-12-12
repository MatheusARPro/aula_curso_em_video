soma = 0
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

media = soma / c .__float__()
print(f'''A media entre os numeros digitados e igual a {media}
O maior numero foi {maior} e o menor numero foi {menor}''')