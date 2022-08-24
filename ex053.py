frase = str(input('Digite algo: ')).upper().strip()

frase2 = frase.replace(' ', '')
palindromo = frase2[::-1]
if frase2 == palindromo:
    print(f'{frase} é um PALINDROMO!')
else:
    print(f'{frase} não é um PALINDROMO!')
