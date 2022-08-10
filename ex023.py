#forma string(nao funciona corretamente.)
'''
num = int(input('Digite um numero de 0 a 9999: '))
n = str(num)

print(f"""Analisando o numero {num}
A unidade é {n[3]}
A dezena é {n[2]}
A centena é {n[1]}
A milhar é {n[0]}""")
'''

#forma matematica(funcional.)
num = int(input('Digite um numero de 0 a 9999: '))

print(f"""Analisando o numero {num}
A unidade é : {num // 1 % 10 }
A dezena é : {num // 10 % 10}
A centena é : {num // 100 % 10}
A milhar é : {num // 1000 % 10}""")
