#função
def leiaint(texto):
    numero = 0
    inteiro = False
    while True:
        n = str(input(texto))
        if n.isnumeric():
            numero = int(n)
            inteiro = True
        else:
            print('\033[0:31mERRO!\033[mDigite um número inteiro.')
        if inteiro == True:
            break
    return numero


#codigo
n = leiaint('digite um numero: ')
print(f'\033[0:32mVoce digitou o numero inteiro {n}')
