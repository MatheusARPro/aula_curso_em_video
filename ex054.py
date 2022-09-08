from datetime import date


menor_idade = 0
maior_idade = 0
for c in range(1, 8):
    nasc = int(input(f'digite o {c}º ano de nascimento? '))
    idade = date.today().year - nasc
    if idade < 21:
        menor_idade = menor_idade + 1
    else:
        maior_idade = maior_idade + 1
print(f'''{menor_idade} ainda não atingiram a maior idade
{maior_idade} já atingiram a maior idade''')
