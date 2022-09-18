'''frase = str(input('Digite algo: ')).upper().strip()

frase2 = frase.replace(' ', '')
palindromo = frase2[::-1]
if frase2 == palindromo:
    print(f'{frase} é um PALINDROMO!')
else:
    print(f'{frase} não é um PALINDROMO!')'''


frase = str(input('Digite algo: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Essa frase é uma PALINDROMO!')
else:
    print('Essa frase NÃO É UM PALINDROMO!')