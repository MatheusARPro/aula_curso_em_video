name = input('Digite seu nome: ').strip()

print(f'''Nome completo: {name.title()}
Primeiro nome: {name.split()[0].title()}
Ultimo nome: {name.split()[len(name.split())-1].title()}''')
