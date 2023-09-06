#função
def voto(nasc):
    """
    -> mostra a condição de voto de uma pessoa de acordo com a data de nascimento.
    :param nasc: ano de nascimento.
    :return: retorna a situação.
    """
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos: VOTO É OPCIONAL!'
    elif idade >= 18 and idade < 70:
        return f'Com {idade}: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade}: NÃO VOTA!'


#codigo
print('-' * 30)
nascimento = int(input('Qual o ano de nascimento: '))
print(voto(nascimento))
