from datetime import datetime


# carteira_de_trabalho = {}
# carteira_de_trabalho['Nome'] = str(input('Nome: '))
# ano_de_nascimento = int(input('Ano de nascimento: '))
# carteira_de_trabalho['Idade'] = date.today().year - ano_de_nascimento
# carteira_de_trabalho['CTPS'] = int(input('Numero da carteira de trabalho(0 se nao possuir): '))
# if carteira_de_trabalho['CTPS'] != 0:
#     carteira_de_trabalho['Contratação'] = int(input('Ano de contratação: '))
#     carteira_de_trabalho['Salário'] = float(input('Salário: R$'))
#     aposenta = (carteira_de_trabalho['Contratação'] - ano_de_nascimento) + 35
#     carteira_de_trabalho['Aposentadoria'] = aposenta
# print('-=-' *20)
# for key, value in carteira_de_trabalho.items():
#     print(f'{key} : {value}')
# print('-=-' *20)


#Solução do Guanabara
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0 :
    dados['contratação'] = int(input('Ano de Contrataçao: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
