# jogador = {}
# lista_gol = []
# time = list()
# while True:
#     lista_gol.clear()
#     jogador.clear()
#     nome = str(input('Nome do Jogador: '))
#     partida = int(input(f'Quantas partidas {nome} jogou? '))
#     partidas = 0
#     while partidas < partida:
#         gols = int(input(f'Quantos gols na {partidas +1}ª? '))
#         partidas += 1
#         lista_gol.append(gols)
#     jogador['Nome'] = nome
#     jogador['Gols'] = lista_gol[:]
#     jogador['Total'] = sum(lista_gol)
#     resp = str(input('Quer continuar? [S/N] ')).upper()[0]
#     while True:
#         if resp in 'SN':
#             break
#         print('ERRO! Por favor responda sim[S]/não[N].')
#     time.append(jogador.copy())
#     if resp == 'N':
#         break
# print('-=-'*20)
# print('cod ', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
# print('-'*40)
# for k, v in enumerate(time):
#     print(f'{k:>3} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-'*40)
# while True:
#     levantamento = int(input('Digite o código do jogador para ter acesso ao levatamento dele:(999 para finalizar)'))
#     if levantamento == 999:
#         break
#     if levantamento >= len(time):
#         print(f'ERRO! Não existe jogador com o código {levantamento}')
#     else:
#         print('LEVANTAMENTO DO JOGADOR')
#         print('-'*40)
#         print(f'Nome: {time[levantamento]["Nome"]}')
#         print('Gols por partida:')
#         jogo = 0
#         for gol in range(0, len(time[levantamento]['Gols'])):
#             print(f'=> na {gol+1}ª partida: {time[levantamento]["Gols"][gol]} gols')
# if levantamento == 999:
#     print('<<<<<<<<<<ENCERRADO>>>>>>>>>>')

#Solução do Guanabára
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S OU N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('<<VOLTE SEMPRE>>')


#solução do micael
# OU PODE SER FEITO DESSA FORMA, MAS FALTA INCREMENTAR ESSE PAPO DE ADICIONAR JOGADOR..
# BASICAMENTE VAI TER QUE FAZER A MESMA JOGADA, SÓ QUE CADASTRA UM JOGADOR(DICIONÁRIO)
# E DAÍ FAZ PARA CADA JOGADOR UM CADASTRO DIFERENTE.. SALVA OS JOGADORES EM UMA LISTA E REPLICA OS TREM TUDO.


# def main():
#     lista_de_pessoas = []
#     while questiona_continua():
#         lista_de_pessoas.append(monta_dicionario(ler_nome(), ler_sexo(), ler_idade()))
#     quantidade_pessoas = conta_pessoas(lista_de_pessoas)
#     idade_media = calcula_media_idade(lista_de_pessoas)
#     lista_mulheres = calcula_quantidade_mulheres(lista_de_pessoas)
#     lista_idade_acima_media = calcula_idade_acima_da_media(lista_de_pessoas, int(idade_media))
#     formata_saida(quantidade_pessoas, idade_media, lista_mulheres, lista_idade_acima_media)
#
#
# def formata_saida(quantidade_pessoas, idade_media, lista_mulheres, lista_idade_acima_media):
#     print(f'''
#         Quantidade de pessoas:
#         {quantidade_pessoas}\n
#         Idade média entre as pessoas cadastradas:
#         {idade_media},\n
#         Dentre as pessoas cadastradas, estas são mulheres:
#         {lista_mulheres},\n
#         Estas são as pessoas que tem idade acima da média:
#         {lista_idade_acima_media}
#     ''')
#
#
# def ler_nome():
#     return str(input("Nome: "))
#
#
# def ler_sexo():
#     return str(input("Sexo[M/F]: "))
#
#
# def ler_idade():
#     return int(input("Idade: "))
#
#
# def questiona_continua():
#     continua = str(input("Quer registrar alguém? [SIM] | [NÃO] \n"))
#     if "SIM" in continua[0:3].strip().upper():
#         return True
#     else:
#         return False
#
#
# def monta_dicionario(nome, sexo, idade):
#     dicionario = {
#         "nome": nome,
#         "sexo": sexo,
#         "idade": idade
#     }
#     return dicionario
#
#
# def conta_pessoas(lista_de_pessoas: list = any):
#     quantidade_de_pessoas = len(lista_de_pessoas)
#     return quantidade_de_pessoas
#
#
# def calcula_media_idade(lista_de_pessoas: list = any):
#     soma_idades = 0  # lógicamente funciona com '0' mas o correto é colocar 'int'
#     for pessoa in lista_de_pessoas:
#         idade_da_pessoa = int(pessoa["idade"])
#         soma_idades += idade_da_pessoa
#     idade_media_das_pessoas = soma_idades / len(lista_de_pessoas)
#     return idade_media_das_pessoas
#
#
# def calcula_quantidade_mulheres(lista_de_pessoas: list = any):
#     lista_mulheres = []
#     for pessoa in lista_de_pessoas:
#         sexo_feminino = str(pessoa["sexo"])
#         if "F" in sexo_feminino[0].strip().upper():
#             lista_mulheres.append(pessoa["nome"])
#     return lista_mulheres
#
#
# def calcula_idade_acima_da_media(lista_de_pessoas: list = any, idade_media: int = 0):
#     lista_pessoas_idade_acima_da_media = []
#     for pessoa in lista_de_pessoas:
#         idade = int(pessoa["idade"])
#         if idade > int(idade_media):
#             lista_pessoas_idade_acima_da_media.append(pessoa["nome"])
#     return lista_pessoas_idade_acima_da_media
#
#
# #IMPORTANTE!!! SIGNIFICA QUE 'SE O NOME DO ARQUIVO QUE TÁ SENDO EXECUTADO É IGUAL DO QUE O MAIN(NOME PADRÃO DO AQUIVO
# #PYTHON) ENTÃO ( : ) FAÇA'
# if __name__ == "__main__":
#     main()
