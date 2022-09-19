h_maisvelho = 0
mulheres = 0
tot_idade = 0
for p in range(0, 4):
    print('##' * 10)
    nome = str(input('Nome: ')).strip()
    sexo = input('Sexo [M/F]: ').upper()
    idade = int(input('Idade: '))
    tot_idade = tot_idade + idade
    if sexo == 'F' and idade <= 20:
        mulheres = mulheres + 1
    elif sexo == 'M' and idade >= h_maisvelho:
        h_maisvelho = idade
        hnome = nome
print('##' * 10)
print(f'A quantidade de mulheres abaixo de 20 anos é {mulheres}')
media = tot_idade / 4
print(f'A idade média do grupo é {media}')
print(f'O homem mais velho foi {hnome}')
print('##' * 10)
