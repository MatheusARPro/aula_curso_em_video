import webbrowser


def acessa_site(url):
    try:
        webbrowser.open(url)
    except ConnectionError:
        print(f'O site {url} não está acessível no momento.')
    else:
        print(f'O site {url} está acessível no momento.')


acessa_site('https://pudim.com.br')
