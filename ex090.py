# aluno = {}
# nome = str(input('Nome: '))
# media = float(input('Média: '))
# if media < 5:
#     situaçao = 'Reprovado'
# elif media >= 5:
#     situaçao = 'Aprovado'
#
# aluno['Nome'] = nome
# aluno['Média'] = media
# aluno['Situaçao'] = situaçao
#
# for key, value in aluno.items():
#     print(f'{key} = {value}', end='')
#     print()


#Solução do guanabara

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] =  'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
