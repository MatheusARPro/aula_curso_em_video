produtos = ('Caneta', 1.50, 'Caderno', 15.00, 'Celular', 1500, 'Notebook', 2000, 'Mochila', 100, 'Lapis', 1, 'Apontador', 1.25, 'Borracha', 0.5)
print('-'*35)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('-'*35)
for c in range(0 , len(produtos), 2):
    print(f'{produtos[c]:-<23}R$ {produtos[c + 1]:8.2f}')
print('-'*35)
