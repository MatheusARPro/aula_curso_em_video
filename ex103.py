#funçao
def ficha(txt='<desconhecido>', gols=0):
    """
    ->Mostra a quantidade de Gols de um Jogador!
    :param txt: Nome do jogador.
    :param gols: Quantidade de gols.
    :return: nome com quantidade de gols.
    """
    print(f'O jogador {txt} marcou {gols} gols no campeonato!')


#codigo
nome = str(input('Nome do jogador: '))
gol = str(input('Quantos gols marcados: '))
if gol.isnumeric():
    g = int(gol)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)
help(ficha)
