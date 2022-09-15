m_peso = 0

for c in range(0, 5):
    print('++' * 20)
    print('  DETECTOR DE PESO  ')
    print(f'''O mais pesado foi: 
    Peso: {m_peso}Kg''')
    print('++' * 20)
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    if peso >= m_peso:
        m_peso = peso
