from engine import leiaint
#criar menu
#1 ver pesssoas cadastradas
#2 cadastrar noova pessoa
#3 sair do sistema


def set_line(simple:bool=False):
    """Mostra linha entre as opçoes"""
    if simple == True:
        print("-" *60)
    else:
        print("=" *60)

def show_menu():
    '''Show the system menu'''    
    set_line()
    print(f'{"MENU":^60}')
    set_line()
    set_line(True)
    menu_text = f'''
    1 - Ver pessoas cadastradas
    2 - Cadastrar nova pessoa
    3 - Sair do sistema
    '''
    print(menu_text)
    set_line(True)

def set_option():
    while True:
        try:
            option = int(input('Selecione uma opção (1-3): '))
            if 1 <= option <= 3:
                return option
            else:
                print("Por favor, escolha uma opção válida (1-3)!")
        except ValueError:
            print("Por favor, insira um número válido correspondente ao menu!")

def option_1(name=str):
    print('Pessoas Cadastradas:')
    with open(f"ex115/{name}.txt", "r") as archive:
        archive = archive.readlines()
        for line in archive:
            print(line.strip())
       
def option_2(archive=str,name='Desconhecido', age=0):
    pessoa = str(input('Nome: '))
    age = leiaint("Idade: ")
    if pessoa == "":
        pessoa  = 'Desconhecido'

    try:
        a = open(f'ex115/{name}.txt', "rt")
        a.close()
    except:
        with open(f'ex115/{archive}.txt', 'a') as archive:
            archive.write(f'{pessoa:<50} {age:>2} anos\n')
    print(f'{pessoa} foi adicionada com sucesso ao registro.')

