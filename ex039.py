from datetime import date


nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade < 18:
    tempo_restante = 18 - idade
    print(f'Ainda ira se alistar, faltam apenas {tempo_restante} anos.')
elif idade == 18:
    print('Você esta na idade cereta para o alistamento, ALISTE-SE!!!')
elif idade > 18:
    tempo_restante = idade - 18
    print(f'O alistamento venceu, ja passou {tempo_restante} anos do prazo.')