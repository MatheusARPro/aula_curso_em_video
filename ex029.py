vel = float(input('Qual a velocidade do veiculo em Quilometros[km]: '))

if vel > 80:
    print('Você ultrapassou o limite de velocidade, e foi multado.')
    multa = (vel - 80) * 7
    print(f'O valor da multa será de R${multa:.2f}')
