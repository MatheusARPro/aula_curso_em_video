def dobro(valor):
    res =  valor * 2
    return res

def metade(valor):
    res = valor / 2
    return res

def aumentar(valor, percentual):
    aumento = (percentual / 100) * valor
    res = valor + aumento
    return res

def diminuir(valor, percentual):
    diminuiçao = (percentual / 100) * valor
    res = valor - diminuiçao
    return res

def moeda(valor):
    decimal = str(f'{valor:,.2f}')
    formatado = decimal.replace(".", ",")
    return formatado
