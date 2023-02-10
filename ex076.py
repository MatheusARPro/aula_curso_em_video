produtos = ('Caneta', 1.50, 'Caderno', 15.00, 'Celular', 1500, 'Notebook', 2000, 'Mochila', 100, 'Lapis', 1, 'Apontador', 1.25, 'Borracha', 0.5)
print('-'*35)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('-'*35)
for c in range(0 , len(produtos), 2):
    print(f'{produtos[c]:-<23}R$ {produtos[c + 1]:8.2f}')
print('-'*35)

#sugestao do Guanabara
listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'canetas', 22.30,
            'Livro', 34.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)