sexo = '0'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo[M/F]: ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('SEXO INVÁLIDO!')
if sexo == 'M':
    print('Você digitou o sexo "MASCULINO"! ')
elif sexo == 'F':
    print('Você digitou o sexo "FEMININO"!')
