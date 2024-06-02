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
