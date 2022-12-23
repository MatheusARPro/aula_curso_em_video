cont = soma = 0
while True:
    num = int(input('Digite um numero (para parar digite 999): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma do {cont} digitados e igual a {soma}.')
