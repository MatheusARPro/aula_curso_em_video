valores = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o ultimo valor: ')))
print(f'Os valores digitados foram: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    posicao = valores.index(3) + 1
    print(f'O valor 3 foi digitado na {posicao}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares Digitados foram ', end=' ')
for c in range(0, len(valores)):
     if valores[c] % 2 == 0:
         print(valores[c],end=' ')