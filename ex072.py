numeros = ('zero',  'um', 'dois', 'três', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resp = int(input('Digite um numero entre 0 e 20: '))
    if resp < 0 or resp > 20:
        print('Numero inválido.Tente novamente.')
    else:
        break
print(f'Você digitou o número {numeros[resp]}')
