
name = str( input('Qual seu nome completo ? '))

print(f"""Seu nome em maiusculas : {name.upper()}
Seu nome em minusculas : {name.lower()}
Seu nome completo sem espaços tem {len(name.replace(' ',''))} letras
Seu primeiro nome tem {len(name.split()[0])} letras""")


'''
name = str( input('Qual seu nome completo ? ')).strip()

print(f"""Seu nome em maiusculas : {name.upper()}
Seu nome em minusculas : {name.lower()}
Seu nome completo sem espaços tem {len(name) - name.count(' ')} letras
Seu primeiro nome tem {name.find(' ')} letras""")
'''

