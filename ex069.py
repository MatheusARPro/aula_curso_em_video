print('===' * 15)
tot18 = totmulher = 0
tothomem = 0
while True:
    print('CADASTRO DE PESSOA')
    print('---' * 15)
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 = tot18 + 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if 'F' in sexo:
            break
        elif 'M' in sexo:
                break
    if 'M' in sexo:
        tothomem = tothomem + 1
    if 'F' in sexo and idade < 20:
        totmulher = totmulher + 1
    print('---' * 15)
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if 'N' in continua:
            break
        elif 'S' in continua:
            break
    if 'N' in continua:
        break
    print('---' * 15)

print('====FIM DO PROGRAMA====')
print(f'Total de pessoas acima dos 18 anos: {tot18}')
print(f'Total de homens cadastrados: {tothomem}')
print(f'Total de mulheres com menos de 20 anos: {totmulher}')
