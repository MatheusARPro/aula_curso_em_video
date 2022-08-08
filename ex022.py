name = input('Qual seu nome completo ? ')
#nome2 = nome.split()
print(f"""Seu nome em maiusculas : {name.upper()}
Seu nome em minusculas : {name.lower()}
Seu nome completo sem espaços tem {len(name.replace(' ',''))} letras
Seu primeiro nome tem {len(name.split()[0])} letras""")
