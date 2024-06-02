def dobro(valor , show=False):
    res = valor * 2
    if show == True:
        return moeda(res)
    else:
        return res


def metade(valor, show=False):
    res = valor / 2
    if show == True:
        return moeda(res)
    else:
        return res


def aumentar(valor, percentual, show=False):
    aumento = (percentual / 100) * valor
    res = valor + aumento
    if show == True:
        return moeda(res)
    else:
        return res


def diminuir(valor, percentual, show=False):
    diminuiçao = (percentual / 100) * valor
    res = valor - diminuiçao
    if show == True:
        return moeda(res)
    else:
        return res


def moeda(valor):
    decimal = str(f'{valor:,.2f}')
    formatado = decimal.replace(".", ",")
    return formatado


def resumo(preco, aumento, reducao):
    print('-' *33)
    print(f'{"Registro de Valores":^33}')
    print('=' *33)
    print(f'{"Preço analisado: ":20}{"R$":>3}{moeda(preco)}')
    print(f'{"Dobro do preço: ":20}{"R$":>3}{dobro(preco, True)}')
    print(f'{"Metade do preço: ":20}{"R$":>3}{metade(preco, True)}')
    print_aumento = f'{aumento}% de aumento: '
    print(f'{print_aumento:20}{"R$":>3}{aumentar(preco, aumento, True)}')
    print_reducao = f'{reducao}% de redução: '
    print(f'{print_reducao:20}{"R$":>3}{diminuir(preco, reducao, True)}')
    print('-' *33)
