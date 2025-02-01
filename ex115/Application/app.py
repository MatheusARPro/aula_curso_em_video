import main_menu
import engine


def app():
    engine.clear_prompt()
    print('Iniciando aplicativo...')
    arquivo = 'Cadastro de Pessoa'
    while True:
        engine.open_archive(arquivo)
        main_menu.show_menu()
        choice = main_menu.set_option()
        if choice != 3:
            engine.run(choice=choice)
            if choice == 1:
                main_menu.option_1(arquivo) 
            if choice == 2:
                main_menu.option_2(arquivo)
        else:
            engine.clear_prompt()
            print('Aplicativo encerrado.')
            break
    

if __name__ == '__main__':
    app()