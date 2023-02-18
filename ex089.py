alunos = []
nota = []
nome = []
while True:
    pessoa = str(input('Aluno: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    nome.append(pessoa)
    nota.append(n1)
    nota.append(n2)
    nome.append(nota[:])
    alunos.append(nome[:])
    resp = 'a'
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
    nota.clear()
    nome.clear()
print('-'*30)
print(f'{"REGISTRO DE NOTAS":^30}')
print('-'*30)
print(f'{"ID":<5}|{"Aluno":^16}|{"Media":>7}')
print('-'*30)
for a in range(0, len(alunos)):
    media = (alunos[a][1][0] + alunos[a][1][1]) / 2
    print(f'{a:<5}|{alunos[a][0]:16}|{media:>7.2f}')
print('-'*30)
aluno = int
while aluno != 999:
    aluno = int(input('Digite o ID do aluno para ver as notas [999 para finalizar]:  '))
    if aluno != 999:
        print(f'Aluno: {alunos[aluno][0]}'
              f'\nNota 1: {alunos[aluno][1][0]}'
              f'\nNota 2: {alunos[aluno][1][1]}')
print('FINALIZANDO...')
print('<<<VOLTE SEMPRE>>>')
