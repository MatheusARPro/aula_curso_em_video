from datetime import date


nome = input('Nome do atleta: ')
nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
print('-=-'*10)
if idade <= 9:
    print(f'''Atleta: {nome}
Idade: {idade}
Categoria: MIRIM''')
elif idade > 9 and idade <= 14:
    print(f'''Atleta: {nome}
Idade: {idade}
Categoria: INFANTIL''')
elif idade > 14 and idade <= 19:
    print(f'''Atleta: {nome}
Idade: {idade}
Categoria: JUNIOR''')
elif idade > 19 and idade <= 20:
    print(f'''Atleta: {nome}
Idade: {idade}
Categoria: SÊNIOR''')
else:
    print(f'''Atleta: {nome}
Idade: {idade}
Categoria: MASTER''')
print('-=-'*10)
