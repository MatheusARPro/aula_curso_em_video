import main_menu
import engine


def app():
    engine.clear_prompt()
    print('Iniciando aplicativo...')
    while True:
        main_menu.show_menu()
        choice = main_menu.set_option()
        if choice != 3:
            engine.run(choice=choice)
        else:
            engine.clear_prompt()
            print('Aplicativo encerrado.')
            break

if __name__ == '__main__':
    app()