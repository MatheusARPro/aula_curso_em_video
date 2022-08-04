r = float(input('Quanto você tem na carteira? R$'))
d = r/5.14
e = r/5.29
l = r/6.31
print('-'*50)
print('Com R${:.2f} e possivel comprar US${:.2f} dólar(es)'.format(r, d))
print('Com R${:.2f} e possível comprar €${:.2f} euro(s)'.format(r, e))
print('Com R${:.2f} e possivel comprar £${:.2f} libra(s)'.format(r, l))
print('-'*50)