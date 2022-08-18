numero = int(input('Digite um numero: '))
print('''Qual vai ser a base de conversão? 
[ 1 ]Binário
[ 2 ]Octal
[ 3 ]Hexadecimal ''')

base = int(input('Sua escolha: '))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if base == 1:
    print(f'O numero {numero}, convertido para binário é: {binario[2:]}')
elif base == 2:
    print(f'O numero {numero}, convertido para octal é: {octal[2:]}')
elif base == 3:
    print(f'O numero {numero}, convertido para hexadecimal é: {hexadecimal[2:]}')
else:
    print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE.')
