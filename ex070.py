valor_total = menor_valor = c = maior_mil = 0
produto_barato = ' '
while True:
    produto = str(input('Produto: '))
    valor = float(input('Valor: R$ '))
    valor_total += valor
    c += 1
    if valor > 1000:
        maior_mil += 1
    if c == 1:
        menor_valor = valor
        produto_barato = produto
    if valor < menor_valor:
        menor_valor = valor
        produto_barato = produto
    while True:
        continuar = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if 'S' in continuar or 'N' in continuar:
            break
    if continuar in 'N':
        break

print(f'Total gasto: R${valor_total:.2f}')
print(f'Produtos acima de R$1.000,00: {maior_mil}')
print(f'Produto mais barato: {produto_barato} por {menor_valor}')
