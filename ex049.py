numero = int(input('Digite o numero para ver a tabuada: '))
print('#' * 15)
for multiplicador in range(1, 11):
    print(f'{numero:2} X {multiplicador:2} = {numero*multiplicador}')
print('#' * 15)
