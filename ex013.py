sal = float(input('Qual o salário do funcionário? R$'))
aumento = (sal / 100) * 15
nsal = sal + aumento
print('O novo salário com o aumento de 15% sera de R${:.2f} .'.format(nsal))