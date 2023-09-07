#função
def fatorial(numero, show=False):
    """
    ->Função para calcular o fatorial de um número.
    :param numero: número que vai ser calculado.
    :param show: (OPCIONAL) mostra ou não a conta.
    :return: o valor fatorial do número.
    """
    fat = 1
    for num in range(numero, 0, -1):
        fat *= num
    if show == True:
        while numero > 0:
            print(f'{numero} ', end='')
            print('X ' if numero > 1 else ' = ', end='')
            if numero == 0 :
                break
            numero -= 1
    return fat


#codigo
print(fatorial(5, show=True))
#help(fatorial)