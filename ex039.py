from datetime import date


nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade < 18:
    tempo_restante = 18 - idade
    ano = tempo_restante + ano_atual
    print(f'Ainda ira se alistar, faltam apenas {tempo_restante} anos.')
    print(f'Seu alistamento sera em {ano} ')
elif idade == 18:
    print('Você esta na idade cereta para o alistamento, ALISTE-SE!!!')
elif idade > 18:
    tempo_restante = idade - 18
    ano = ano_atual - tempo_restante
    print(f'O alistamento venceu, ja passou {tempo_restante} anos do prazo.')
    print(f'Seu alistamento foi em {ano}')
