aluno = input('Aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('='*20)
media = (n1 + n2) / 2
if media < 5.00:
    print(f'''Aluno: {aluno}
Média: {media:.2f}
Status: \033[31mREPROVADO\033[m''')
elif media >= 5.00 and media <= 6.99:
    print(f'''Aluno: {aluno}
Média: {media:.2f}
Status: \033[33mRECUPERAÇÃO\033[m''')
elif media >= 7.00:
    print(f'''Aluno: {aluno}
Média: {media:.2f}
Status: \033[32mAPROVADO\033[m''')
print('='*20)
