num = int(input('Digite um numero de 0 a 9999: '))

#print(f'''Do numero {num}
#A unidade é {num[3]}
#A dezena é {num[2]}
#A centena é {num[1]}
#A milhar é {num[0]}''')

print(f"""Do número {num}
A unidade é {num // 1 % 10 }
A dezena é {num // 10 % 10}
A centena é {num // 100 % 10}
A milhar é {num // 1000 % 10}""")
