def notas(*num,sit=False):
    '''
    Função para a analise de notas e situaão de alunos.
    :param num: Nota dos aluno
    :param sit: Situação das notas do aluno
    :return: Retorna um dicionário com as informações do aluno
    '''
    nota = dict()
    nota['Quantidade'] = len(num)
    nota['Maior'] = max(num)
    nota['Menor'] = min(num)
    nota['Media'] = sum(num) / len(num)
    if sit:
        if nota['Media'] >= 7:
            nota['Situação'] = 'BOA'
        elif nota['Media'] >= 5:
            nota['Situação'] = 'RAZOÁVEL'
        elif nota['Media'] < 5:
            nota['Situação'] = 'RUIM'
    return nota


boletim = notas(3.5, 2, 5, 10, 7.5, 8, 6, sit=True)
print(boletim)
# help(notas)