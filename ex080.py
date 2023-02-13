valores = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero >= valores[-1]:
        valores.append(numero)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print(f'A ordem dos valores digitados são: {valores}')