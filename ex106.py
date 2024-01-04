c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;32;40m',
     '\033[0;35;40m'
     );


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print("#" * tamanho)
    print(f"  {msg}  ")
    print("#" * tamanho)
    print(c[0], end='')


def ajuda(comando):
    titulo(f'Acessando o manual da função \'{comando}\'',2 )
    print(c[3], end='')
    help(comando)
    print(c[0])


# Codigo principal
titulo('Sitema de ajuda PyHelp', 1)
while True:
    comando = input(f"{c[4]}Para qual função gostaria de obter ajuda?(Digite sair para finalizar)>>> ")
    if comando.upper() == "SAIR":
        break
    else:
        ajuda(comando)
titulo('Sitema finalizado, até logo!', 1)
