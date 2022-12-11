n1 = 0
cont = 0
s = 0
while n1 < 999 :
    n1 = int(input('Digite um número: '))
    if n1 != 999:
        s = s + n1
        cont = cont + 1
        print('Para finalizar digite [999].')
    else:
        print('Finalizado!!!')
print(f'Foram digitados no total {cont} numeros , e a soma entre eles e igual a {s}!!!')
