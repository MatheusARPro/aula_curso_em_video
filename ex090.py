aluno = {}
nome = str(input('Nome: '))
media = float(input('Média: '))
if media < 5:
    situaçao = 'Reprovado'
elif media >= 5:
    situaçao = 'Aprovado'

aluno['Nome'] = nome
aluno['Média'] = media
aluno['Situaçao'] = situaçao

for key, value in aluno.items():
    print(f'{key} = {value}', end='')
    print()