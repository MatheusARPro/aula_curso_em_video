numero = int(input('Digite o numero para ver a tabuada: '))
print('#' * 15)
for multiplicador in range(1, 11):
    resultado = multiplicador * numero
    print(f'{multiplicador:2} X {numero} = {resultado}')
print('#' * 15)
