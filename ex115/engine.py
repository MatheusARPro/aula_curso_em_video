from main_menu import set_line
import os

def clear_prompt():
    # Check the operating system and execute the appropriate command
    os.system('cls' if os.name == 'nt' else 'clear')

def run(choice:int):
    clear_prompt()
    set_line(simple=True)
    print(f'\nA opção escolhida foi {choice}\n')
    set_line(simple=True)