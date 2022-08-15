numero = int(input('Digite um numero: '))
base = int(input('Qual vai ser a base de conversão?(Digite [1]Binário, [2]Octal, [3]Hexadecimal) '))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if base == 1:
    print(f'O numero {numero}, convertido para binário é: {binario}')
elif base == 2:
    print(f'O numero {numero}, convertido para octal é: {octal}')
elif base == 3:
    print(f'O numero {numero}, convertido para hexadecimal é: {hexadecimal}')
    