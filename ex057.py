'''sexo = '0'
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o sexo[M/F]: ')).upper().strip()[0]
    if sexo != 'F' and sexo != 'M':
        print('SEXO INVÁLIDO!')
if sexo == 'M':
    print('Você digitou o sexo "MASCULINO"! ')
elif sexo == 'F':
    print('Você digitou o sexo "FEMININO"!')'''


sexo = str(input('Informe o Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Invalido. Por favor, informe o sexo: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print(f'Sexo informado: {sexo}')
