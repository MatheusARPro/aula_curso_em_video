def coleta_dado_digitado(pre_texto):
    dado = input(f'{pre_texto}')
    return dado

def verifica_monetario(pre_texto):
    while True:
        dado = coleta_dado_digitado(pre_texto=pre_texto)
        if dado.isnumeric() == False:
            print(f'"ERRO" {dado} não é um preço válido, tente novamente.')
        else:
            return float(dado)
