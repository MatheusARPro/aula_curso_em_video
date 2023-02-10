palavras = ('Python', 'Matheus', 'Programar', 'Hardware', 'Estudar', 'Formar', 'Programação', 'Programador', 'Trabalho', 'Faculdade', 'Curso')
for c in palavras:
    print(f'\nNa palavra "{c.upper()}" temos as vogais: ',end=' ')
    for vogal in c:
        if vogal.upper() in 'AEIOU':
            print(vogal.upper(), end=' ')
