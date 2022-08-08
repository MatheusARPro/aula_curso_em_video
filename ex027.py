name = input('Digite seu nome: ')

print(f'''Nome completo: {name}
Primeiro nome: {name.split()[0]}
Ultimo nome: {name.split()[len(name.split())-1]}''')
