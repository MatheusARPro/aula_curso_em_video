import main_menu
import os

def set_line(simple:bool=False):
    """Mostra linha entre as opçoes"""
    if simple == True:
        print("-" *40)
    else:
        print("=" *40)

def clear_prompt():
    # Check the operating system and execute the appropriate command
    os.system('cls' if os.name == 'nt' else 'clear')

def run(choice:int):
    clear_prompt()
    set_line(simple=True)
    print(f'\nA opção escolhida foi {choice}\n')
    set_line(simple=True)

def open_archive(name=str):
    try:
        a = open(f'ex115/{name}.txt', "rt")
        a.close()
    except FileNotFoundError:
        with open(f'ex115/{name}.txt', "a+") as archive:
            archive.write('')

def leiaint(texto):
    numero = 0
    inteiro = False
    while True:
        n = str(input(texto))
        if n.isnumeric():
            numero = int(n)
            inteiro = True
        else:
            print('\033[0:31mERRO!\033[mDigite um número inteiro.')
        if inteiro == True:
            break
    return numero
