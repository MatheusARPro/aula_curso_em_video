def leia_int(texto):
        while True:
            try:
                numero = int(input(texto))
            except (TypeError, ValueError):
                print('O dado digitado não é um numero inteiro.Tente novamente.')
                continue
            except (KeyboardInterrupt):
                print('O usuário preferiu nao inserir dados.')
                return 0
            else:
                return  numero


def leia_real(texto):
    while True:
        try:
            numero = float(input(texto))
        except (TypeError, ValueError):
            print('O dado digitado não é um número real.Tente Novamente.')
        except (KeyboardInterrupt):
            print('O usuário preferiu nao inserir dados')
            numero = 0
            return 0
        else:
            return numero


inteiro = leia_int('Digite um numero inteiro: ')
real = leia_real('Digite um numero real:')
print(f'O numero inteiro digitado foi {inteiro} e o numero real {real}.')
