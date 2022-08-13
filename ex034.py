salario = float(input('Qual é o salário do funcionario? R$'))

if salario > 1250.00:
    aumento = (salario / 100) * 10
    n_salario = salario + aumento
    print(f'''Pelo salário ser superior a R$1250,00, então o aumento será de 10%, 
e o novo salário passará a ser de R${n_salario:.2f}''')
else:
    if salario <= 1250.00:
        aumento = (salario / 100) * 15
        n_salario = salario + aumento
        print(f'''Pelo salário ser inferior a R$1250,00, então o aumento será de 15%, 
e o novo salário passará a ser de R${n_salario:.2f}''')
