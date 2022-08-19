preço = float(input('Preço do produto: R$'))
print('''\033[31m%%%FORMAS DE PAGAMENTO%%%\033[m
[1] À VISTA DINHEIRO/CHEQUE.
[2] À VISTA CARTÃO.
[3] 2X NO CARTÃO.
[4] 3X OU MAIS NO CARTÃO''')
pag = int(input('Digite a opção escolhida: '))
print('#'*25)
if pag == 1:
    valor_pag = preço - ((preço / 100 ) * 10)
    print(f'''DESCONTO: 10%
JUROS: 0%
VALOR À PAGAR: R${valor_pag:.2f}''')
elif pag == 2:
    valor_pag = preço -((preço / 100) * 5)
    print(f'''DESCONTO: 5%
JUROS: 0%
VALOR À PAGAR: R${valor_pag:.2f}''')
elif pag == 3:
    parcela = preço /  2
    print(f'''DESCONTO: 0%
JUROS: 0%
VALOR DA PARCELA: R${parcela}
VALOR À PAGAR: R${preço}''')
elif pag == 4:
    par = int(input('NÚMERO DE PARCELAS: '))
    valor_pag = preço + ((preço / 100) * 20)
    parcela = valor_pag / par
    print(f'''DESCONTO: %
JUROS: 20%
VALOR DA PARCELA: R${parcela}
VALOR À PAGAR: R${valor_pag:.2f}''')
else:
    print('OPÇÃO INVALIDA.TENTE NOVAMENTE.')
print('#'*25)
