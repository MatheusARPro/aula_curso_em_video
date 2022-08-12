n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o ultimo número: '))
n_maior = 0
n_menor = 0

if n1 > n2 and n1 > n3:
    n_maior = n1
else:
    if n1 < n2 and n1 < n3:
        n_menor = n1
    else:
        if n2 > n1 and n2 > n3:
            n_maior = n2
if n2 < n1 and n2 < n3:
    n_menor = n2
else:
    if n3 > n1 and n3 > n2:
        n_maior = n3
    else:
        if n3 < n1 and n3 < n2:
           n_menor = n3
print(f'O maior número é {n_maior}')
print(f'O menor número é {n_menor}')
