casa = float(input('\033[34mQual o valor da casa? '))
salario = float(input('\033[34mQual o valor da renda do comprador? '))
ano = int(input('\033[34mQuantos anos ira durar o parcelamento? '))

mes = ano * 12
parcela = casa / mes
limite = (salario / 100) * 30

if parcela <= limite:
    print(f'''\033[36mDuração do finaciamento: \033[33m {ano} ano(s) \033[m
\033[36mValor da parcela mensal:  \033[33m R${parcela:.2f} \033[m
\033[36mDentro do limite de 30% da renda: \033[33m SIM \033[m
\033[36mStatus: \033[32m APROVADO \033[m''')
elif parcela > limite:
    print(f'''\033[36mDuração do finaciamento: \033[33m {ano} ano(s) \033[m
\033[36mValor da parcela mensal:  \033[33m R${parcela:.2f} \033[m
\033[36mDentro do limite de 30% da renda: \033[33m NÃO \033[m
\033[36mStatus: \033[31m NEGADO \033[m''')
